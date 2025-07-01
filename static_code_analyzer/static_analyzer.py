import os

class SimpleStaticAnalyzer:
    def __init__(self):
        self.issues = []

    def analyze_python_file(self, filepath):
        if not os.path.exists(filepath):
            self.issues.append(f"Error: File '{filepath}' not found.")
            return

        print(f"\nAnalyzing file: {filepath}...")
        with open(filepath, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            line_num = i + 1
            stripped_line = line.strip()

            # Check for missing colon in if/for/while/def/class statements
            if stripped_line.startswith(("if ", "for ", "while ", "def ", "class ")):
                if not stripped_line.endswith(":"):
                    self.issues.append(f"Line {line_num}: Missing colon at end of statement: '{stripped_line}'")

            # Check for inconsistent indentation (very basic, assumes 4 spaces)
            if line.startswith(" ") and not line.startswith("    ") and not stripped_line == "":
                if not line.startswith("\t"):
                    self.issues.append(f"Line {line_num}: Inconsistent indentation (expected 4 spaces or tab): '{line.rstrip()}'")

        if self.issues:
            print("\n--- Analysis Results: Issues Found ---")
            for issue in self.issues:
                print(issue)
            print("-------------------------------------")
            self.issues = [] # Clear issues for next analysis
        else:
            print("No issues found.")

if __name__ == "__main__":
    analyzer = SimpleStaticAnalyzer()
    print("--- Simple CLI Static Code Analyzer (Conceptual) ---")
    print("This script performs basic checks on Python files.")
    print("Commands: analyze <filepath>, exit")

    # Create a dummy Python file for testing
    dummy_code = """
def my_function(arg):
    if arg > 0
        print("Positive")
    else:
        print("Negative")

class MyClass:
  def __init__(self):
    pass
"""
    with open("test_code.py", "w") as f:
        f.write(dummy_code)
    print("Created test_code.py for testing.")

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "analyze":
            if len(command_input) == 2:
                analyzer.analyze_python_file(command_input[1])
            else:
                print("Usage: analyze <filepath>")
        elif cmd == "exit":
            print("Exiting Static Analyzer.")
            break
        else:
            print("Unknown command.")