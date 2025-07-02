import os
import ast

class CodeVisitor(ast.NodeVisitor):
    """
    Traverses the AST to find all defined and used names.
    """
    def __init__(self):
        self.defined_names = set()
        self.used_names = set()

    def visit_FunctionDef(self, node):
        self.defined_names.add(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.defined_names.add(node.name)
        self.generic_visit(node)

    def visit_Name(self, node):
        # We are interested in names that are being loaded (read)
        if isinstance(node.ctx, ast.Load):
            self.used_names.add(node.id)
        self.generic_visit(node)

class AstStaticAnalyzer:
    """
    Analyzes Python files using the Abstract Syntax Tree (AST) module.
    """
    def __init__(self):
        self.issues = []

    def analyze_python_file(self, filepath):
        """
        Analyzes a single Python file for syntax errors and unused definitions.
        """
        if not os.path.exists(filepath):
            self.issues.append(f"Error: File '{filepath}' not found.")
            self.print_issues()
            return

        print(f"\nAnalyzing file: {filepath}...")
        with open(filepath, 'r') as f:
            source_code = f.read()

        try:
            tree = ast.parse(source_code, filename=filepath)
        except SyntaxError as e:
            self.issues.append(f"SyntaxError in {filepath} at line {e.lineno}, col {e.offset}: {e.msg}")
            self.print_issues()
            return

        visitor = CodeVisitor()
        visitor.visit(tree)

        # Find unused top-level functions and classes.
        # This is a simplified check and may not be perfectly accurate in all scenarios
        # (e.g., dynamic usage, decorators, use in other files).
        unused_definitions = visitor.defined_names - visitor.used_names
        for name in sorted(list(unused_definitions)): # sorted for consistent output
            # Find the line number for the unused definition
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name == name:
                    self.issues.append(f"Line {node.lineno}: Unused definition: '{name}'")
                    break
        
        self.print_issues()

    def print_issues(self):
        if self.issues:
            print("\n--- Analysis Results: Issues Found ---")
            for issue in self.issues:
                print(issue)
            print("-------------------------------------")
        else:
            print("No issues found.")
        self.issues = [] # Clear for the next analysis

if __name__ == "__main__":
    analyzer = AstStaticAnalyzer()
    print("--- AST-based Static Code Analyzer ---")
    print("This script uses AST to find syntax errors and unused definitions.")

    # Create a dummy Python file with various issues for testing
    dummy_code = '''
import os

class UnusedClass:
    def __init__(self):
        pass

def used_function():
    print("This function is used.")

def unused_function(arg):
    if arg > 0: # Missing colon here
        print("Positive")

def main():
    used_function()

# Note: 'main', 'UnusedClass', and 'unused_function' will be flagged as unused
# because they are not called within the scope of this file analysis.
'''
    test_file = "test_code_ast.py"
    with open(test_file, "w") as f:
        f.write(dummy_code)
    print(f"Created {test_file} for testing.")

    # Analyze the dummy file directly
    analyzer.analyze_python_file(test_file)

    # Clean up the created test file
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"Cleaned up {test_file}.")
