import re

class RegexQueryTool:
    def __init__(self):
        pass

    def search_text(self, pattern, text):
        matches = []
        for i, line in enumerate(text.splitlines()):
            for match in re.finditer(pattern, line, re.IGNORECASE):
                matches.append({
                    "line_number": i + 1,
                    "start_index": match.start(),
                    "end_index": match.end(),
                    "matched_text": match.group()
                })
        return matches

    def run_interactive(self):
        print("--- Regex Query Tool ---")
        print("Enter a regex pattern and text to search. Type 'q' to quit.")

        while True:
            try:
                pattern = input("Enter regex pattern: ")
                if pattern.lower() == 'q':
                    break

                text = input("Enter text to search (multi-line input, press Enter twice to finish):\n")
                lines = []
                while True:
                    line = input()
                    if not line:
                        break
                    lines.append(line)
                text = "\n".join(lines)

                matches = self.search_text(pattern, text)

                if matches:
                    print("\n--- Matches Found ---")
                    for match in matches:
                        print(f"Line {match['line_number']}: '{match['matched_text']}' (Start: {match['start_index']}, End: {match['end_index']})")
                    print("---------------------")
                else:
                    print("No matches found.")

            except re.error as e:
                print(f"Invalid regex pattern: {e}")
            except EOFError:
                print("Exiting tool.")
                break

if __name__ == '__main__':
    tool = RegexQueryTool()
    tool.run_interactive()
