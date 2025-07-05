import os

def generate_tree(start_path, indent=""):
    if not os.path.isdir(start_path):
        print(f"{indent}-- {os.path.basename(start_path)}")
        return

    print(f"{indent}+- {os.path.basename(start_path)}/")
    for item in os.listdir(start_path):
        path = os.path.join(start_path, item)
        generate_tree(path, indent + "|  ")

if __name__ == "__main__":
    # Example usage: Generate tree for the current directory
    # You can change '.' to any other path you want to visualize
    generate_tree(".")
