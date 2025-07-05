import ast

# --- Node-based checks ---

def check_empty_init(node):
    if isinstance(node, ast.ClassDef):
        for class_node in node.body:
            if isinstance(class_node, ast.FunctionDef) and class_node.name == '__init__':
                if not class_node.body or (len(class_node.body) == 1 and isinstance(class_node.body[0], ast.Pass)):
                    return f"Empty __init__ method in class {node.name} at line {class_node.lineno}"
    return None

def check_useless_pass(node):
    if hasattr(node, 'body') and isinstance(node.body, list):
        has_pass = any(isinstance(child, ast.Pass) for child in node.body)
        # A docstring is not considered a statement for this check's purpose
        has_other_statements = any(not isinstance(child, (ast.Pass, ast.Expr)) or (isinstance(child, ast.Expr) and not isinstance(child.value, ast.Str)) for child in node.body)

        if has_pass and has_other_statements:
            for child in node.body:
                if isinstance(child, ast.Pass):
                    # Check if the pass statement is not the only statement on the line
                    # This is hard to do with AST, so we'll stick to the block check
                    return f"Useless pass statement at line {child.lineno}"
    return None


def check_many_arguments(node):
    if isinstance(node, ast.FunctionDef):
        if len(node.args.args) > 10:
            return f"Function {node.name} has too many arguments ({len(node.args.args)}) at line {node.lineno}"
    return None

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

def check_unused_variables(node):
    if not isinstance(node, ast.FunctionDef):
        return None

    assigned_vars = {}
    used_vars = set()

    # Collect assigned variables in the function body
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            if isinstance(n.ctx, ast.Store):
                # Ignore function arguments and class attributes
                if n.id not in [arg.arg for arg in node.args.args]:
                     assigned_vars[n.id] = n.lineno
            elif isinstance(n.ctx, ast.Load):
                used_vars.add(n.id)

    issues = []
    for var, lineno in assigned_vars.items():
        if var not in used_vars:
            issues.append(f"Unused variable '{var}' at line {lineno}")
            
    return issues

# --- Tree-based checks ---

def check_unused_imports(node):
    if not isinstance(node, ast.Module):
        return None

    imports = {}
    for item in node.body:
        if isinstance(item, ast.Import):
            for alias in item.names:
                imports[alias.asname or alias.name] = item.lineno
        elif isinstance(item, ast.ImportFrom):
            if item.module is None and item.level > 0: # relative import
                continue
            for alias in item.names:
                imports[alias.asname or alias.name] = item.lineno

    used_names = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            used_names.add(n.id)
        elif isinstance(n, ast.Attribute):
            # For 'os.path', we need to get 'os'
            curr = n
            while isinstance(curr, ast.Attribute):
                curr = curr.value
            if isinstance(curr, ast.Name):
                used_names.add(curr.id)


    issues = []
    for name, lineno in imports.items():
        if name not in used_names:
            # Handle 'import os.path' used as 'os'
            if '.' in name and name.split('.')[0] in used_names:
                continue
            issues.append(f"Unused import '{name}' at line {lineno}")
            
    return issues

# --- File-based checks ---

def check_long_lines(file_path, max_length=80):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines):
        if len(line.rstrip('\n')) > max_length:
            issues.append(f"Line {i+1} is too long ({len(line.rstrip('\n'))} > {max_length} characters)")
    return issues

def check_todo_fixme(file_path):
    issues = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if "TODO" in line:
                issues.append(f"TODO comment found at line {i+1}")
            if "FIXME" in line:
                issues.append(f"FIXME comment found at line {i+1}")
    return issues

# --- Check lists ---

NODE_CHECKS = [
    check_empty_init,
    check_useless_pass,
    check_many_arguments,
    check_missing_docstrings,
    check_print_statements,
    check_unused_variables,
]

TREE_CHECKS = [
    check_unused_imports,
]

FILE_CHECKS = [
    check_long_lines,
    check_todo_fixme,
]

# --- Analyzer ---

def analyze_code(file_path):
    """Analyzes a Python file for potential issues."""
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    try:
        tree = ast.parse(code, filename=file_path)
    except SyntaxError as e:
        return [f"Syntax error in {file_path}: {e}"]

    issues = []
    
    # Run node-based checks
    for node in ast.walk(tree):
        for check in NODE_CHECKS:
            result = check(node)
            if result:
                if isinstance(result, list):
                    issues.extend(result)
                else:
                    issues.append(result)

    # Run tree-based checks
    for check in TREE_CHECKS:
        result = check(tree)
        if result:
            if isinstance(result, list):
                issues.extend(result)
            else:
                issues.append(result)

    # Run file-based checks
    for check in FILE_CHECKS:
        issues.extend(check(file_path))
        
    return issues

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_to_analyze = sys.argv[1]
    else:
        file_to_analyze = 'test_file.py'
        
    issues = analyze_code(file_to_analyze)
    for issue in issues:
        print(issue)