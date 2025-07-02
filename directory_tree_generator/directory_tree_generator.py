import os

class DirectoryTreeGenerator:
    def __init__(self):
        pass

    def generate_tree(self, path, indent="", last=False):
        if not os.path.exists(path):
            print(f"Error: Path not found: {path}")
            return

        name = os.path.basename(path)
        print(f"{indent}{'+-- ' if last else '|-- '}{name}/")

        if os.path.isdir(path):
            files = sorted(os.listdir(path))
            for i, file in enumerate(files):
                filepath = os.path.join(path, file)
                is_last = (i == len(files) - 1)
                self.generate_tree(filepath, indent + ("    " if last else "|   "), is_last)

if __name__ == '__main__':
    generator = DirectoryTreeGenerator()
    print("--- Interactive Directory Tree Generator ---")
    
    while True:
        path = input("Enter directory path (or 'q' to quit): ")
        if path.lower() == 'q':
            break
        
        generator.generate_tree(path)

    print("Exiting Directory Tree Generator.")
