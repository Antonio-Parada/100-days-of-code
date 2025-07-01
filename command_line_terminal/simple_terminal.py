import os
import subprocess

class SimpleTerminal:
    def __init__(self):
        self.current_directory = os.getcwd()

    def execute_command(self, command_line):
        parts = command_line.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if cmd == "echo":
            print(args)
        elif cmd == "cd":
            try:
                os.chdir(args)
                self.current_directory = os.getcwd()
                print(f"Changed directory to: {self.current_directory}")
            except FileNotFoundError:
                print(f"Directory not found: {args}")
            except Exception as e:
                print(f"Error changing directory: {e}")
        elif cmd == "ls" or cmd == "dir": # Basic listing
            try:
                # Use subprocess to run actual system command for listing
                if os.name == 'nt': # For Windows
                    subprocess.run(['cmd', '/c', 'dir'], cwd=self.current_directory)
                else: # For Linux/macOS
                    subprocess.run(['ls'], cwd=self.current_directory)
            except Exception as e:
                print(f"Error listing directory: {e}")
        elif cmd == "exit":
            return False # Signal to exit
        else:
            print(f"Unknown command: {cmd}")
        return True

if __name__ == "__main__":
    terminal = SimpleTerminal()
    print("--- Simple CLI Terminal Simulation ---")
    print("Commands: echo <text>, cd <directory>, ls/dir, exit")

    while True:
        user_input = input(f"{terminal.current_directory}> ")
        if not terminal.execute_command(user_input):
            print("Exiting terminal.")
            break
