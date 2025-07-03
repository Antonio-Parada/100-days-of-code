import ast

def analyze_code(file_path):
    """Analyzes a Python file for potential issues."""
    with open(file_path, 'r') as f:
        code = f.read()
    
    tree = ast.parse(code)
    
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for class_node in node.body:
                if isinstance(class_node, ast.FunctionDef) and class_node.name == '__init__':
                    if not class_node.body or (len(class_node.body) == 1 and isinstance(class_node.body[0], ast.Pass)):
                        issues.append(f"Empty __init__ method in class {node.name} at line {class_node.lineno}")
    
    return issues

if __name__ == '__main__':
    issues = analyze_code('test_file.py')
    for issue in issues:
        print(issue)