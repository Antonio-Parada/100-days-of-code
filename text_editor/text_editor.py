import os

class SimpleTextEditor:
    def __init__(self):
        self.current_file = None
        self.content = []

    def open_file(self, filepath):
        if not os.path.exists(filepath):
            print(f"File '{filepath}' not found. Creating a new file.")
            self.current_file = filepath
            self.content = []
            return

        try:
            with open(filepath, 'r') as f:
                self.content = [line.rstrip('\n') for line in f.readlines()]
            self.current_file = filepath
            print(f"Successfully opened '{filepath}'.")
        except Exception as e:
            print(f"Error opening file: {e}")

    def save_file(self):
        if not self.current_file:
            print("No file open. Use 'open <filepath>' first.")
            return
        try:
            with open(self.current_file, 'w') as f:
                for line in self.content:
                    f.write(line + '\n')
            print(f"Successfully saved to '{self.current_file}'.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def display_content(self):
        if not self.content:
            print("[Empty file]")
            return
        for i, line in enumerate(self.content):
            print(f"{i+1}: {line}")

    def insert_line(self, line_num, text):
        if 0 <= line_num <= len(self.content):
            self.content.insert(line_num, text)
            print(f"Line inserted at position {line_num + 1}.")
        else:
            print("Invalid line number.")

    def delete_line(self, line_num):
        if 0 <= line_num < len(self.content):
            deleted_line = self.content.pop(line_num)
            print(f"Deleted line {line_num + 1}: '{deleted_line}'.")
        else:
            print("Invalid line number.")

    def replace_line(self, line_num, new_text):
        if 0 <= line_num < len(self.content):
            old_text = self.content[line_num]
            self.content[line_num] = new_text
            print(f"Replaced line {line_num + 1} (old: '{old_text}', new: '{new_text}').")
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    editor = SimpleTextEditor()
    print("--- Simple CLI Text Editor ---")
    print("Commands: open <filepath>, save, show, insert <line_num> <text>, delete <line_num>, replace <line_num> <text>, exit")

    while True:
        command_input = input("> ").split(maxsplit=2)
        cmd = command_input[0].lower()

        if cmd == "open":
            if len(command_input) == 2:
                editor.open_file(command_input[1])
            else:
                print("Usage: open <filepath>")
        elif cmd == "save":
            editor.save_file()
        elif cmd == "show":
            editor.display_content()
        elif cmd == "insert":
            if len(command_input) == 3:
                try:
                    line_num = int(command_input[1]) - 1
                    editor.insert_line(line_num, command_input[2])
                except ValueError:
                    print("Invalid line number.")
            else:
                print("Usage: insert <line_num> <text>")
        elif cmd == "delete":
            if len(command_input) == 2:
                try:
                    line_num = int(command_input[1]) - 1
                    editor.delete_line(line_num)
                except ValueError:
                    print("Invalid line number.")
            else:
                print("Usage: delete <line_num>")
        elif cmd == "replace":
            if len(command_input) == 3:
                try:
                    line_num = int(command_input[1]) - 1
                    editor.replace_line(line_num, command_input[2])
                except ValueError:
                    print("Invalid line number.")
            else:
                print("Usage: replace <line_num> <text>")
        elif cmd == "exit":
            print("Exiting editor.")
            break
        else:
            print("Unknown command.")
