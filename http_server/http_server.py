import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080         # Port to listen on (non-privileged ports are > 1023)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")
                # Simple HTTP response
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello, World!</h1>"
                conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    run_server()

