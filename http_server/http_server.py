import socket
import os

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
    request_line = lines[0].split(' ')
    method = request_line[0]
    path = request_line[1]
    http_version = request_line[2]
    return method, path, http_version

def handle_request(method, path):
    if path == '/':
        path = '/index.html'

    file_path = os.path.join(WEB_ROOT, path[1:])

    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        
        _, ext = os.path.splitext(file_path)
        content_type = MIME_TYPES.get(ext, 'application/octet-stream')

        response_headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
        return response_headers.encode('utf-8') + content
    else:
        response_body = b"<h1>404 Not Found</h1>"
        response_headers = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: {len(response_body)}\r\n\r\n"
        return response_headers.encode('utf-8') + response_body

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    continue

                method, path, http_version = parse_request(data)
                print(f"Method: {method}, Path: {path}, HTTP Version: {http_version}")

                response = handle_request(method, path)
                conn.sendall(response)

if __name__ == "__main__":
    run_server()

