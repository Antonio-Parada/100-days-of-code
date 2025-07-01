import re

class SimpleLexer:
    def __init__(self):
        self.tokens = []
        self.rules = [
            ('NUMBER', r'\d+'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('WHITESPACE', r'\s+')
        ]
        self.token_regex = self._build_token_regex()

    def _build_token_regex(self):
        # Build a single regex from all rules, ignoring whitespace
        return '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.rules if name != 'WHITESPACE')

    def tokenize(self, code):
        self.tokens = []
        line_num = 1
        line_start = 0
        
        for match in re.finditer(self.token_regex, code):
            token_type = match.lastgroup
            token_value = match.group(token_type)

            if token_type == 'WHITESPACE':
                # Handle newlines for line numbering
                new_lines = token_value.count('\n')
                line_num += new_lines
                if new_lines > 0:
                    line_start = match.end()
                continue

            column = match.start() - line_start + 1
            self.tokens.append({'type': token_type, 'value': token_value, 'line': line_num, 'column': column})
        
        return self.tokens

if __name__ == "__main__":
    lexer = SimpleLexer()
    print("--- Simple CLI Programming Language Lexer (Tokenizer) ---")
    print("This script tokenizes simple arithmetic expressions and identifiers.")
    print("Type code to tokenize (or 'exit' to quit).")

    while True:
        user_input = input("Enter code: ")
        if user_input.lower() == "exit":
            print("Exiting Lexer.")
            break
        
        tokens = lexer.tokenize(user_input)
        print("Tokens:")
        for token in tokens:
            print(f"  {token}")
