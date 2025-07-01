import psutil
import time
import os

def get_network_usage():
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    return bytes_sent, bytes_recv

def bytes_to_gb(bytes_val):
    return round(bytes_val / (1024**3), 2)

if __name__ == "__main__":
    print("Basic Bandwidth Monitor (requires psutil: pip install psutil)")
    print("Press Ctrl+C to stop.")

    initial_bytes_sent, initial_bytes_recv = get_network_usage()
    start_time = time.time()

    try:
        while True:
            time.sleep(1) # Update every second
            current_bytes_sent, current_bytes_recv = get_network_usage()

            # Calculate difference from initial readings
            total_sent = current_bytes_sent - initial_bytes_sent
            total_recv = current_bytes_recv - initial_bytes_recv

            # Calculate current rates (bytes per second)
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                sent_rate = (current_bytes_sent - (psutil.net_io_counters().bytes_sent - total_sent)) / elapsed_time
                recv_rate = (current_bytes_recv - (psutil.net_io_counters().bytes_recv - total_recv)) / elapsed_time
            else:
                sent_rate = 0
                recv_rate = 0

            os.system('cls' if os.name == 'nt' else 'clear') # Clear console
            print("--- Network Usage ---")
            print(f"Total Sent: {bytes_to_gb(total_sent)} GB")
            print(f"Total Received: {bytes_to_gb(total_recv)} GB")
            print(f"Sent Rate: {bytes_to_gb(sent_rate * 1)} GB/s") # Displaying as GB/s for clarity
            print(f"Received Rate: {bytes_to_gb(recv_rate * 1)} GB/s")

    except KeyboardInterrupt:
        print("\nBandwidth monitoring stopped.")
