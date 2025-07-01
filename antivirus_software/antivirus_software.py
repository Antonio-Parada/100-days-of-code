import os
import hashlib

class SimpleAntivirus:
    def __init__(self):
        # A very simple signature database (MD5 hashes of known "malware" files)
        self.malware_signatures = {
            "e4d909c290d0fb1ca0687464b2b1373c": "malware_a.exe",
            "a1b2c3d4e5f67890a1b2c3d4e5f67890": "virus.dll",
            "f0e1d2c3b4a59687f0e1d2c3b4a59687": "trojan.tmp"
        }

    def _calculate_md5(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def scan_file(self, filepath):
        if not os.path.exists(filepath):
            return f"File '{filepath}' not found."

        print(f"Scanning file: {filepath}...")
        file_hash = self._calculate_md5(filepath)

        if file_hash in self.malware_signatures:
            malware_name = self.malware_signatures[file_hash]
            return f"Threat detected! File: '{filepath}', Malware: {malware_name} (MD5: {file_hash})"
        else:
            return f"File: '{filepath}' is clean."

    def scan_directory(self, directory_path):
        if not os.path.isdir(directory_path):
            return f"Directory '{directory_path}' not found."

        print(f"\nScanning directory: {directory_path}...")
        threats_found = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                filepath = os.path.join(root, file)
                result = self.scan_file(filepath)
                if "Threat detected!" in result:
                    threats_found.append(result)
        
        if threats_found:
            print("\n--- Scan Summary: THREATS FOUND ---")
            for threat in threats_found:
                print(threat)
            print("----------------------------------")
        else:
            print("\n--- Scan Summary: No threats found. ---")

if __name__ == "__main__":
    antivirus = SimpleAntivirus()
    print("--- Simple CLI Antivirus Software (Conceptual) ---")
    print("This script simulates scanning files based on MD5 hashes.")
    print("It does NOT provide real-time protection or advanced threat detection.")
    print("Commands: scan_file <filepath>, scan_dir <directory_path>, exit")

    # Create some dummy files for testing
    if not os.path.exists("test_files"):
        os.makedirs("test_files")
    with open("test_files/clean_file.txt", "w") as f: f.write("This is a clean file.")
    with open("test_files/malware_a.exe", "w") as f: f.write("This is a dummy malware file A.")
    with open("test_files/virus.dll", "w") as f: f.write("This is a dummy virus file.")
    
    # Manually update the hashes for the dummy malware files
    # You would typically get these from a real malware database
    antivirus.malware_signatures[antivirus._calculate_md5("test_files/malware_a.exe")] = "malware_a.exe"
    antivirus.malware_signatures[antivirus._calculate_md5("test_files/virus.dll")] = "virus.dll"

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "scan_file":
            if len(command_input) == 2:
                print(antivirus.scan_file(command_input[1]))
            else:
                print("Usage: scan_file <filepath>")
        elif cmd == "scan_dir":
            if len(command_input) == 2:
                antivirus.scan_directory(command_input[1])
            else:
                print("Usage: scan_dir <directory_path>")
        elif cmd == "exit":
            print("Exiting Antivirus Software.")
            break
        else:
            print("Unknown command.")