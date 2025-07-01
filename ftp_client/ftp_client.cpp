#include <iostream>
#include <string>
#include <vector>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <cstring> // For memset
#include <fstream> // For file operations
#include <algorithm> // For std::replace

#pragma comment(lib, "Ws2_32.lib")

// Function to handle connection to FTP server
int connect_to_server(const std::string& ip_address, int port) {
    SOCKET sock = INVALID_SOCKET;
    struct sockaddr_in serv_addr;

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        std::cerr << "\n Socket creation error: " << WSAGetLastError() << "\n" << std::endl;
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, ip_address.c_str(), &serv_addr.sin_addr) <= 0) {
        std::cerr << "\nInvalid address/ Address not supported \n" << std::endl;
        closesocket(sock);
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) == SOCKET_ERROR) {
        std::cerr << "\nConnection Failed: " << WSAGetLastError() << "\n" << std::endl;
        closesocket(sock);
        return -1;
    }
    std::cout << "Connected to " << ip_address << ":" << port << std::endl;
    return sock;
}

std::string receive_response(SOCKET sock) {
    char buffer[4096];
    std::string response = "";
    int bytes_received;
    do {
        bytes_received = recv(sock, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received > 0) {
            buffer[bytes_received] = '\0';
            response += buffer;
        } else if (bytes_received == 0) {
            std::cout << "Connection closed by remote host." << std::endl;
            return "";
        } else {
            std::cerr << "recv failed: " << WSAGetLastError() << std::endl;
            return "";
        }
    } while (bytes_received == sizeof(buffer) - 1 && response.find("\n") == std::string::npos); // Read until newline or buffer full
    return response;
}

void send_command(SOCKET sock, const std::string& command) {
    std::string cmd_with_newline = command + "\r\n";
    if (send(sock, cmd_with_newline.c_str(), cmd_with_newline.length(), 0) == SOCKET_ERROR) {
        std::cerr << "send failed: " << WSAGetLastError() << std::endl;
    }
}

SOCKET open_data_connection(SOCKET control_sock) {
    send_command(control_sock, "PASV");
    std::string response = receive_response(control_sock);
    std::cout << "PASV response: " << response << std::endl;

    // Parse IP and port from PASV response (e.g., 227 Entering Passive Mode (h1,h2,h3,h4,p1,p2).)
    size_t start = response.find("(");
    size_t end = response.find(")");
    if (start == std::string::npos || end == std::string::npos) {
        std::cerr << "Failed to parse PASV response." << std::endl;
        return INVALID_SOCKET;
    }

    std::string ip_port_str = response.substr(start + 1, end - start - 1);
    std::replace(ip_port_str.begin(), ip_port_str.end(), ',', '.');

    std::vector<std::string> parts;
    size_t prev_pos = 0;
    size_t comma_pos;
    while ((comma_pos = ip_port_str.find('.', prev_pos)) != std::string::npos) {
        parts.push_back(ip_port_str.substr(prev_pos, comma_pos - prev_pos));
        prev_pos = comma_pos + 1;
    }
    parts.push_back(ip_port_str.substr(prev_pos));

    if (parts.size() != 6) {
        std::cerr << "Failed to parse IP and port from PASV response." << std::endl;
        return INVALID_SOCKET;
    }

    std::string ip_address = parts[0] + "." + parts[1] + "." + parts[2] + "." + parts[3];
    int port = std::stoi(parts[4]) * 256 + std::stoi(parts[5]);

    std::cout << "Connecting to data port: " << ip_address << ":" << port << std::endl;

    return connect_to_server(ip_address, port);
}

int main() {
    WSADATA wsaData;
    int iResult;

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0) {
        std::cerr << "WSAStartup failed: " << iResult << std::endl;
        return 1;
    }

    std::cout << "FTP Client project started!" << std::endl;
    std::cout << "Enter 'connect <ip_address> <port>' to connect to an FTP server." << std::endl;
    std::cout << "Enter 'login <username> <password>' to authenticate." << std::endl;
    std::cout << "Enter 'list' to list files." << std::endl;
    std::cout << "Enter 'retr <filename>' to download a file." << std::endl;
    std::cout << "Enter 'quit' to exit." << std::endl;

    SOCKET client_socket = INVALID_SOCKET;
    std::string command;

    while (true) {
        std::cout << "> ";
        std::getline(std::cin, command);

        if (command == "quit") {
            if (client_socket != INVALID_SOCKET) {
                closesocket(client_socket);
            }
            break;
        } else if (command.rfind("connect ", 0) == 0) { // Check if command starts with "connect "
            std::string args = command.substr(8);
            size_t space_pos = args.find(' ');
            if (space_pos != std::string::npos) {
                std::string ip_address = args.substr(0, space_pos);
                int port = std::stoi(args.substr(space_pos + 1));
                if (client_socket != INVALID_SOCKET) {
                    closesocket(client_socket);
                }
                client_socket = connect_to_server(ip_address, port);
                if (client_socket != INVALID_SOCKET) {
                    std::cout << "Server response: " << receive_response(client_socket) << std::endl;
                }
            } else {
                std::cout << "Usage: connect <ip_address> <port>" << std::endl;
            }
        } else if (command.rfind("login ", 0) == 0) {
            if (client_socket == INVALID_SOCKET) {
                std::cout << "Not connected to an FTP server. Please connect first." << std::endl;
                continue;
            }
            std::string args = command.substr(6);
            size_t space_pos = args.find(' ');
            if (space_pos != std::string::npos) {
                std::string username = args.substr(0, space_pos);
                std::string password = args.substr(space_pos + 1);

                send_command(client_socket, "USER " + username);
                std::cout << "Server response: " << receive_response(client_socket) << std::endl;

                send_command(client_socket, "PASS " + password);
                std::cout << "Server response: " << receive_response(client_socket) << std::endl;
            } else {
                std::cout << "Usage: login <username> <password>" << std::endl;
            }
        } else if (command == "list") {
            if (client_socket == INVALID_SOCKET) {
                std::cout << "Not connected to an FTP server. Please connect first." << std::endl;
                continue;
            }
            SOCKET data_sock = open_data_connection(client_socket);
            if (data_sock != INVALID_SOCKET) {
                send_command(client_socket, "LIST");
                std::cout << "Server response: " << receive_response(client_socket) << std::endl;

                std::string list_data = receive_response(data_sock);
                std::cout << "Directory listing:\n" << list_data << std::endl;
                closesocket(data_sock);
                std::cout << "Server response: " << receive_response(client_socket) << std::endl; // Final response after data transfer
            }
        } else if (command.rfind("retr ", 0) == 0) {
            if (client_socket == INVALID_SOCKET) {
                std::cout << "Not connected to an FTP server. Please connect first." << std::endl;
                continue;
            }
            std::string filename = command.substr(5);
            SOCKET data_sock = open_data_connection(client_socket);
            if (data_sock != INVALID_SOCKET) {
                send_command(client_socket, "RETR " + filename);
                std::cout << "Server response: " << receive_response(client_socket) << std::endl;

                std::ofstream outfile(filename, std::ios::binary);
                if (!outfile.is_open()) {
                    std::cerr << "Failed to open file for writing: " << filename << std::endl;
                    closesocket(data_sock);
                    continue;
                }

                char data_buffer[4096];
                int bytes_read;
                while ((bytes_read = recv(data_sock, data_buffer, sizeof(data_buffer), 0)) > 0) {
                    outfile.write(data_buffer, bytes_read);
                }
                outfile.close();
                closesocket(data_sock);
                std::cout << "File " << filename << " downloaded successfully." << std::endl;
                std::cout << "Server response: " << receive_response(client_socket) << std::endl; // Final response after data transfer
            }
        } else if (command.rfind("stor ", 0) == 0) {
            if (client_socket == INVALID_SOCKET) {
                std::cout << "Not connected to an FTP server. Please connect first." << std::endl;
                continue;
            }
            std::string filename = command.substr(5);
            std::ifstream infile(filename, std::ios::binary);
            if (!infile.is_open()) {
                std::cerr << "Failed to open file for reading: " << filename << std::endl;
                continue;
            }

            SOCKET data_sock = open_data_connection(client_socket);
            if (data_sock != INVALID_SOCKET) {
                send_command(client_socket, "STOR " + filename);
                std::cout << "Server response: " << receive_response(client_socket) << std::endl;

                char data_buffer[4096];
                while (infile.read(data_buffer, sizeof(data_buffer))) {
                    send(data_sock, data_buffer, sizeof(data_buffer), 0);
                }
                send(data_sock, data_buffer, infile.gcount(), 0); // Send remaining bytes

                infile.close();
                closesocket(data_sock);
                std::cout << "File " << filename << " uploaded successfully." << std::endl;
                std::cout << "Server response: " << receive_response(client_socket) << std::endl; // Final response after data transfer
            }
        } else {
            std::cout << "Unknown command." << std::endl;
        }
    }

    WSACleanup();
    return 0;
}

