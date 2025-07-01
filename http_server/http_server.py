def parse_request(request_data_raw):
    # Find the end of headers (double CRLF)
    header_end = request_data_raw.find(b'\r\n\r\n')
    if header_end == -1:
        return None, None, None, {}, b"" # Malformed request

    header_part = request_data_raw[:header_end].decode('utf-8', errors='ignore')
    body_part_raw = request_data_raw[header_end + 4:]

    lines = header_part.split('\r\n')
    if not lines:
        return None, None, None, {}, b"" # Empty request

    request_line = lines[0].split(' ')
    if len(request_line) != 3:
        return None, None, None, {}, b"" # Malformed request line

    method = request_line[0]
    path = request_line[1]
    http_version = request_line[2]

    headers = {}
    for line in lines[1:]:
        if ': ' in line:
            key, value = line.split(': ', 1)
            headers[key.lower()] = value.strip()
    
    # Parse body based on Content-Type
    parsed_body = {}
    content_type = headers.get('content-type', '')

    if 'application/x-www-form-urlencoded' in content_type:
        body_str = body_part_raw.decode('utf-8', errors='ignore')
        for param in body_str.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                parsed_body[key] = value
    elif 'application/json' in content_type:
        try:
            body_str = body_part_raw.decode('utf-8', errors='ignore')
            parsed_body = json.loads(body_str)
        except json.JSONDecodeError:
            logging.warning("Failed to parse JSON body.")
            parsed_body = {}
    elif 'multipart/form-data' in content_type:
        parsed_body['raw_multipart_body'] = body_part_raw # Pass raw body for multipart handling
    else:
        parsed_body['raw_body'] = body_part_raw # For other content types, pass raw body

    return method, path, http_version, headers, parsed_body

MIDDLEWARE = []

def use_middleware(middleware_func):
    MIDDLEWARE.append(middleware_func)

def session_middleware(method, path, http_version, headers, body):
    session_id = None
    if 'cookie' in headers:
        cookies = headers['cookie'].split('; ')
        for cookie in cookies:
            if cookie.startswith('session_id='):
                session_id = cookie.split('=', 1)[1]
                break
    
    if session_id not in SESSIONS:
        session_id = str(uuid.uuid4())
        SESSIONS[session_id] = {}
        logging.info(f"New session created: {session_id}")
    
    headers['x-session-id'] = session_id # Add session ID to headers for handlers
    return None # Continue to next middleware or handler

use_middleware(session_middleware)

def send_response(conn, status_code, content_type, content, headers=None):
    status_messages = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error"
    }
    status_message = status_messages.get(status_code, "Unknown")
    
    response_headers = f"HTTP/1.1 {status_code} {status_message}\r\n"
    response_headers += f"Content-Type: {content_type}\r\n"
    response_headers += f"Content-Length: {len(content)}\r\n"
    if headers:
        for key, value in headers.items():
            response_headers += f"{key}: {value}\r\n"
    
    # Add session cookie if a new session was created or updated
    if 'x-session-id' in headers and headers['x-session-id'] not in SESSIONS:
        response_headers += f"Set-Cookie: session_id={headers['x-session-id']}; Path=/; HttpOnly\r\n"

    response_headers += "\r\n"
    
    conn.sendall(response_headers.encode('utf-8') + content)

def handle_get_request(path):
    if path == '/':
        path = '/index.html'

    file_path = os.path.join(WEB_ROOT, path[1:])

    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            _, ext = os.path.splitext(file_path)
            content_type = MIME_TYPES.get(ext, 'application/octet-stream')
            return 200, content_type, content, {}
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return 500, 'text/html', b"<h1>500 Internal Server Error</h1>", {}
    else:
        return 404, 'text/html', b"<h1>404 Not Found</h1>", {}

def handle_post_request(path, body, headers):
    logging.info(f"Received POST request for path: {path} with body: {body} and headers: {headers}")
    content_type = headers.get('content-type', '')

    if 'multipart/form-data' in content_type:
        raw_multipart_body = body.get('raw_multipart_body', b'')
        boundary = content_type.split('boundary=')[1].encode('latin-1') # Boundary is in bytes
        
        parts = raw_multipart_body.split(b'--' + boundary)
        for part in parts:
            if b'Content-Disposition: form-data;' in part:
                filename_match = re.search(b'filename="(.*?)"\r\n', part)
                if filename_match:
                    filename = filename_match.group(1).decode('utf-8')
                    file_content_start = part.find(b'\r\n\r\n') + 4
                    file_content = part[file_content_start:]
                    
                    upload_path = os.path.join(UPLOAD_DIR, filename)
                    try:
                        with open(upload_path, 'wb') as f:
                            f.write(file_content)
                        logging.info(f"File uploaded: {upload_path}")
                        response_content = f"<h1>File Uploaded Successfully!</h1><p>File: {filename}</p>".encode('utf-8')
                        return 200, 'text/html', response_content, {}
                    except Exception as e:
                        logging.error(f"Error saving uploaded file {filename}: {e}")
                        response_content = f"<h1>File Upload Failed!</h1><p>Error: {e}</p>".encode('utf-8')
                        return 500, 'text/html', response_content, {}
                else:
                    # Handle other form fields in multipart
                    name_match = re.search(b'name="(.*?)"\r\n', part)
                    if name_match:
                        name = name_match.group(1).decode('utf-8')
                        value_start = part.find(b'\r\n\r\n') + 4
                        value = part[value_start:].decode('utf-8').strip()
                        logging.info(f"Form field: {name} = {value}")

    response_content = f"<h1>POST Request Received</h1><p>You sent: {body}</p>".encode('utf-8')
    return 200, 'text/html', response_content, {}

def handle_put_request(path, body, headers):
    logging.info(f"Received PUT request for path: {path} with body: {body} and headers: {headers}")
    response_content = b"<h1>PUT Request Received (Not Fully Implemented)</h1>"
    return 405, 'text/html', response_content, {}

def handle_delete_request(path, headers):
    logging.info(f"Received DELETE request for path: {path} with headers: {headers}")
    response_content = b"<h1>DELETE Request Received (Not Fully Implemented)</h1>"
    return 405, 'text/html', response_content, {}

# Simple routing mechanism
ROUTES = {
    'GET': {
        '/': handle_get_request,
        '/index.html': handle_get_request,
    },
    'POST': {
        '/submit': handle_post_request,
    },
    'PUT': {
        '/upload': handle_put_request,
    },
    'DELETE': {
        '/delete': handle_delete_request,
    },
}

def handle_client(conn, addr):
    try:
        logging.info(f"Connected by {addr}")
        # Read initial part of the request to get headers
        initial_data = conn.recv(4096) # Read some initial bytes
        
        # Find the end of headers
        header_end = initial_data.find(b'\r\n\r\n')
        if header_end == -1:
            # If headers are larger than initial_data, read more
            # This is a simplification; a real server would loop until headers are complete
            logging.warning("Headers too large for initial read or malformed request.")
            send_response(conn, 400, 'text/html', b"<h1>400 Bad Request - Headers Too Large or Malformed</h1>")
            return

        # Extract header part and body part
        header_part_raw = initial_data[:header_end]
        body_part_initial_raw = initial_data[header_end + 4:]

        # Decode header part to parse method, path, http_version, and headers
        header_part_str = header_part_raw.decode('utf-8', errors='ignore')
        header_lines = header_part_str.split('\r\n')
        request_line = header_lines[0].split(' ')
        method = request_line[0]
        path = request_line[1]
        http_version = request_line[2]

        headers = {}
        for line in header_lines[1:]:
            if ': ' in line:
                key, value = line.split(': ', 1)
                headers[key.lower()] = value.strip()

        # Read remaining body if Content-Length is present
        content_length = int(headers.get('content-length', 0))
        remaining_body_size = content_length - len(body_part_initial_raw)
        
        full_body_raw = body_part_initial_raw
        if remaining_body_size > 0:
            full_body_raw += conn.recv(remaining_body_size)

        method, path, http_version, headers, body = parse_request(initial_data) # Pass raw data to parse_request
        
        if not method or not path or not http_version:
            send_response(conn, 400, 'text/html', b"<h1>400 Bad Request</h1>")
            return

        logging.info(f"Received {method} request for {path} (HTTP/{http_version}) with headers: {headers}")

        # Apply middleware
        for middleware_func in MIDDLEWARE:
            middleware_response = middleware_func(method, path, http_version, headers, body)
            if middleware_response:
                send_response(conn, *middleware_response)
                return

        handler = ROUTES.get(method, {}).get(path)

        if handler:
            if method == 'GET':
                status_code, content_type, content, custom_headers = handler(path)
            elif method == 'POST' or method == 'PUT':
                status_code, content_type, content, custom_headers = handler(path, body, headers)
            elif method == 'DELETE':
                status_code, content_type, content, custom_headers = handler(path, headers)
            else:
                status_code, content_type, content, custom_headers = 405, 'text/html', b"<h1>405 Method Not Allowed</h1>", {}
        else:
            # Fallback for static files if not explicitly routed
            if method == 'GET':
                status_code, content_type, content, custom_headers = handle_get_request(path)
            else:
                status_code, content_type, content, custom_headers = 404, 'text/html', b"<h1>404 Not Found</h1>", {}
        
        send_response(conn, status_code, content_type, content, custom_headers)
    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logging.info(f"Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(conn, addr))
            client_handler.daemon = True # Allow main program to exit even if threads are running
            client_handler.start()

    except KeyboardInterrupt:
        logging.info("Server shutting down gracefully...")
    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        server_socket.close()
        logging.info("Server socket closed.")

if __name__ == "__main__":
    run_server()

