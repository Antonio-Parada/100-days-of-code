import socket
import sys

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        s.close()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    if len(sys.argv) < 3:
        print("Usage: python scanner.py <host> <start_port> [end_port]")
        sys.exit()

    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = start_port
    if len(sys.argv) == 4:
        end_port = int(sys.argv[3])

    print(f"Scanning ports on {host} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    main()