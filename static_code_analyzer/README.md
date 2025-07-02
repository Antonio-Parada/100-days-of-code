# Static Code Analyzer Project

## Description

This project is a static code analyzer for Python. It parses Python code to identify syntax errors and unused function and class definitions, helping to improve code quality and maintainability.

## Features

- **AST-Based Parsing:** Uses Python's `ast` module for accurate and robust code analysis.
- **Syntax Error Detection:** Automatically catches syntax errors during the parsing phase.
- **Unused Code Detection:** Identifies top-level functions and classes that are defined but never used within the analyzed file.

## How to Run

1.  Execute the script from your terminal:
    ```bash
    python static_analyzer.py
    ```
2.  The script will automatically create a test file (`test_code_ast.py`), analyze it, print the results, and then clean up the test file.

