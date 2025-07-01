import ast

class UMLGenerator:
    def __init__(self):
        pass

    def generate_uml_from_code(self, code):
        tree = ast.parse(code)
        
        print("\n--- UML Diagram (Conceptual) ---")
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                print(f"Class: {node.name}")
                print("  Attributes:")
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                print(f"    - {target.id}")
                    elif isinstance(item, ast.FunctionDef):
                        print(f"  Method: {item.name}()")
        print("--------------------------------")

if __name__ == "__main__":
    generator = UMLGenerator()
    print("--- Simple CLI UML Diagram Generator (Conceptual) ---")
    print("This script parses Python code and extracts class information.")
    print("It does NOT generate visual UML diagrams.")
    print("Type 'exit' to quit.")

    sample_code = """
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Hello, {self.name}"

class AnotherClass(MyClass):
    def __init__(self, name, value, extra):
        super().__init__(name, value)
        self.extra = extra

    def calculate(self):
        return self.value * 2
"""

    print("\nSample Code to Analyze:")
    print(sample_code)
    generator.generate_uml_from_code(sample_code)

    while True:
        user_input = input("\nEnter Python code (or 'exit' to quit):\n")
        if user_input.lower() == "exit":
            print("Exiting UML Generator.")
            break
        generator.generate_uml_from_code(user_input)
