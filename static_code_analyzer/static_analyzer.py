import ast

def check_empty_init(node):
    if isinstance(node, ast.ClassDef):
        for class_node in node.body:
            if isinstance(class_node, ast.FunctionDef) and class_node.name == '__init__':
                if not class_node.body or (len(class_node.body) == 1 and isinstance(class_node.body[0], ast.Pass)):
                    return f"Empty __init__ method in class {node.name} at line {class_node.lineno}"
    return None

def check_useless_pass(node):
    if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.ClassDef) or isinstance(node, ast.Module):
        if len(node.body) > 1:
            for i, child in enumerate(node.body):
                if isinstance(child, ast.Pass) and i < len(node.body) -1:
                    return f"Useless pass statement at line {child.lineno}"
    return None

def check_many_arguments(node):
    if isinstance(node, ast.FunctionDef):
        if len(node.args.args) > 10:
            return f"Function {node.name} has too many arguments ({len(node.args.args)}) at line {node.lineno}"
    return None

def check_long_lines(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines):
        if len(line) > 80:
            issues.append(f"Line {i+1} is too long ({len(line)} characters)")
    return issues

def check_missing_docstrings(node):
    if isinstance(node, ast.FunctionDef) and node.name != '__init__':
        if not ast.get_docstring(node):
            return f"Missing docstring for {node.name} at line {node.lineno}"
    elif isinstance(node, ast.ClassDef):
        if not ast.get_docstring(node):
            return f"Missing docstring for {node.name} at line {node.lineno}"
    elif isinstance(node, ast.Module):
        if not ast.get_docstring(node):
            return f"Missing docstring for module at line 1"
    return None

def check_print_statements(node):
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        if isinstance(node.value.func, ast.Name) and node.value.func.id == 'print':
            return f"Use of print statement at line {node.lineno}"
    return None

def check_todo_fixme(file_path):
    issues = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if "TODO" in line:
                issues.append(f"TODO comment found at line {i+1}")
            if "FIXME" in line:
                issues.append(f"FIXME comment found at line {i+1}")
    return issues

CHECKS = [
    check_empty_init,
    check_useless_pass,
    check_many_arguments,
    check_missing_docstrings,
    check_print_statements,
]

def analyze_code(file_path):
    """Analyzes a Python file for potential issues."""
    with open(file_path, 'r') as f:
        code = f.read()
    
    tree = ast.parse(code)
    
    issues = []
    for node in ast.walk(tree):
        for check in CHECKS:
            issue = check(node)
            if issue:
                issues.append(issue)
    
    issues.extend(check_long_lines(file_path))
    issues.extend(check_todo_fixme(file_path))
    
    return issues

if __name__ == '__main__':
    issues = analyze_code('test_file.py')
    for issue in issues:
        print(issue)
