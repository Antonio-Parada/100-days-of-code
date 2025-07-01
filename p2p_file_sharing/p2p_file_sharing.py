import socket
import threading
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            conn.sendall(data) # Echo back

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    print("This is a basic P2P file sharing placeholder. It demonstrates basic socket communication.")
    print("To run as server: python p2p_file_sharing.py server")
    print("To run as client: python p2p_file_sharing.py client")

    if len(os.sys.argv) > 1:
        if os.sys.argv[1] == 'server':
            start_server()
        elif os.sys.argv[1] == 'client':
            start_client()
    else:
        print("Please specify 'server' or 'client' to run.")
