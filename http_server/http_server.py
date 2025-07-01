import socket
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080         # Port to listen on (non-privileged ports are > 1023)
WEB_ROOT = os.path.join(os.path.dirname(__file__), 'static')

MIME_TYPES = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.ico': 'image/x-icon',
}

def parse_request(request_data):
    lines = request_data.split('\r\n')
    if not lines:
        return None, None, None, {}, ""

    request_line = lines[0].split(' ')
    if len(request_line) != 3:
        return None, None, None, {}, "" # Malformed request line

    method = request_line[0]
    path = request_line[1]
    http_version = request_line[2]

    headers = {}
    body_start_index = -1
    for i, line in enumerate(lines[1:]):
        if not line:
            body_start_index = i + 2 # +2 for request line and empty line after headers
            break
        if ': ' in line:
            key, value = line.split(': ', 1)
            headers[key.lower()] = value.strip()
    
    body = '\r\n'.join(lines[body_start_index:]) if body_start_index != -1 else ""

    return method, path, http_version, headers, body

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
    # For demonstration, just echo the body back
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

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        logging.info(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                logging.info(f"Connected by {addr}")
                data = conn.recv(4096).decode('utf-8') # Increased buffer size
                if not data:
                    continue

                method, path, http_version, headers, body = parse_request(data)
                
                if not method or not path or not http_version:
                    send_response(conn, 400, 'text/html', b"<h1>400 Bad Request</h1>")
                    continue

                logging.info(f"Received {method} request for {path} (HTTP/{http_version}) with headers: {headers}")

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

if __name__ == "__main__":
    run_server()

