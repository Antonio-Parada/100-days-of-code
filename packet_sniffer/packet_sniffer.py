import socket
import struct
import sys

# This script requires elevated privileges (e.g., running as administrator/root)
# to create raw sockets and capture network traffic.

def eth_addr(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0] , a[1] , a[2], a[3] , a[4] , a[5])
    return b

def main():
    try:
        # Create a raw socket
        # For Windows, use socket.IPPROTO_IP for raw IP packets
        # For Linux, use socket.ntohs(0x0003) for all Ethernet protocols
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print("Starting packet sniffer... (Press Ctrl+C to stop)")

    while True:
        packet = s.recvfrom(65565)

        # packet string from tuple
        packet = packet[0]

        # parse ethernet header
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = struct.unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol))

        # Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8:
            # Parse IP header
            # take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]

            # now unpack them :) 
            iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            iph_length = ihl * 4

            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);

            print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))

            # TCP protocol
            if protocol == 6:
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]

                # unpack them
                tcph = struct.unpack('!HHLLBBHHH' , tcp_header)

                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4

                print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP Header Length : ' + str(tcph_length))

                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(packet) - h_size

                # get data from packet
                data = packet[h_size:]

                print('Data : ' + str(data))

            # ICMP protocol
            elif protocol == 1:
                u = iph_length + eth_length
                icmp_header = packet[u:u+4]

                # unpack them
                icmph = struct.unpack('!BBH' , icmp_header)

                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]

                print('Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum))

                h_size = eth_length + iph_length + 4
                data_size = len(packet) - h_size

                # get data from packet
                data = packet[h_size:]

                print('Data : ' + str(data))

            # UDP protocol
            elif protocol == 17:
                u = iph_length + eth_length
                udp_header = packet[u:u+8]

                # unpack them
                udph = struct.unpack('!HHHH' , udp_header)

                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]

                print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum))

                h_size = eth_length + iph_length + 8
                data_size = len(packet) - h_size

                # get data from packet
                data = packet[h_size:]

                print('Data : ' + str(data))

            # Some other IP protocol like IGMP
            else:
                print('Protocol other than TCP/UDP/ICMP')

            print()

if __name__ == "__main__":
    main()
