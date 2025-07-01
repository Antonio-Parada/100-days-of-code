import os
import hashlib
import shutil
import time

class SimpleVCS:
    def __init__(self, repo_path=".simple_vcs"):
        self.repo_path = repo_path
        self.objects_path = os.path.join(repo_path, "objects")
        self.refs_path = os.path.join(repo_path, "refs")
        self.head_path = os.path.join(repo_path, "HEAD")

    def init(self):
        if os.path.exists(self.repo_path):
            print("Repository already initialized.")
            return
        os.makedirs(self.objects_path)
        os.makedirs(self.refs_path)
        with open(self.head_path, "w") as f:
            f.write("ref: refs/heads/master")
        print(f"Initialized empty SimpleVCS repository in {self.repo_path}")

    def _hash_object(self, data):
        sha1 = hashlib.sha1(data.encode()).hexdigest()
        object_path = os.path.join(self.objects_path, sha1)
        with open(object_path, "w") as f:
            f.write(data)
        return sha1

    def add(self, filepath):
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' not found.")
            return
        with open(filepath, "r") as f:
            content = f.read()
        blob_hash = self._hash_object(content)
        print(f"Added '{filepath}' (blob: {blob_hash})")

    def commit(self, message):
        if not os.path.exists(self.repo_path):
            print("Repository not initialized. Use 'init' first.")
            return

        # Create a dummy tree object (simplified)
        tree_content = ""
        for root, _, files in os.walk("."):
            if self.repo_path in root: # Skip VCS internal files
                continue
            for file in files:
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath):
                    with open(filepath, "r") as f:
                        file_hash = hashlib.sha1(f.read().encode()).hexdigest()
                        tree_content += f"blob {file_hash} {file}\n"
        tree_hash = self._hash_object(tree_content)

        # Create commit object
        parent_commit = None
        head_ref_content = open(self.head_path, "r").read().strip()
        if head_ref_content.startswith("ref:"):
            branch_ref_path = os.path.join(self.repo_path, head_ref_content.split(": ")[1])
            if os.path.exists(branch_ref_path):
                parent_commit = open(branch_ref_path, "r").read().strip()

        commit_content = f"tree {tree_hash}\n"
        if parent_commit:
            commit_content += f"parent {parent_commit}\n"
        commit_content += f"author User <user@example.com> {int(time.time())} +0000\n"
        commit_content += f"committer User <user@example.com> {int(time.time())} +0000\n\n"
        commit_content += message

        commit_hash = self._hash_object(commit_content)

        # Update HEAD to point to the new commit
        if head_ref_content.startswith("ref:"):
            branch_ref_path = os.path.join(self.repo_path, head_ref_content.split(": ")[1])
            with open(branch_ref_path, "w") as f:
                f.write(commit_hash)
        else:
            with open(self.head_path, "w") as f:
                f.write(commit_hash)

        print(f"Committed: {commit_hash}\nMessage: {message}")

    def log(self):
        if not os.path.exists(self.head_path):
            print("No commits yet.")
            return

        current_commit_hash = open(self.head_path, "r").read().strip()
        if current_commit_hash.startswith("ref:"):
            branch_ref_path = os.path.join(self.repo_path, current_commit_hash.split(": ")[1])
            if os.path.exists(branch_ref_path):
                current_commit_hash = open(branch_ref_path, "r").read().strip()
            else:
                print("No commits yet.")
                return

        print("\n--- Commit History ---")
        while current_commit_hash:
            commit_object_path = os.path.join(self.objects_path, current_commit_hash)
            if not os.path.exists(commit_object_path):
                print("Corrupted repository: Commit object not found.")
                break
            
            with open(commit_object_path, "r") as f:
                commit_content = f.read()
            
            lines = commit_content.split('\n')
            tree_line = next((line for line in lines if line.startswith("tree ")), None)
            parent_line = next((line for line in lines if line.startswith("parent ")), None)
            author_line = next((line for line in lines if line.startswith("author ")), None)
            message_lines = [line for line in lines if not line.startswith(("tree ", "parent ", "author ", "committer ")) and line.strip() != ""]

            print(f"Commit: {current_commit_hash}")
            if author_line: print(f"Author: {author_line.replace("author ", "")}")
            if message_lines: print(f"Message: {'\n'.join(message_lines)}")
            print("----------------------")

            if parent_line:
                current_commit_hash = parent_line.replace("parent ", "")
            else:
                current_commit_hash = None

if __name__ == "__main__":
    vcs = SimpleVCS()
    print("--- Simple CLI Version Control System (Conceptual) ---")
    print("Commands: init, add <filepath>, commit <message>, log, exit")

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "init":
            vcs.init()
        elif cmd == "add":
            if len(command_input) == 2:
                vcs.add(command_input[1])
            else:
                print("Usage: add <filepath>")
        elif cmd == "commit":
            if len(command_input) == 2:
                vcs.commit(command_input[1])
            else:
                print("Usage: commit <message>")
        elif cmd == "log":
            vcs.log()
        elif cmd == "exit":
            print("Exiting VCS simulation.")
            break
        else:
            print("Unknown command.")
