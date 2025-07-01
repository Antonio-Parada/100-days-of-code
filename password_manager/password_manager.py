import random
import string

class SimplePasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        self.passwords[website] = {'username': username, 'password': password}
        print(f"Password for {website} added/updated.")

    def get_password(self, website):
        entry = self.passwords.get(website)
        if entry:
            return f"Website: {website}, Username: {entry['username']}, Password: {entry['password']}"
        else:
            return f"No password found for {website}."

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

if __name__ == "__main__":
    pm = SimplePasswordManager()
    print("--- Simple CLI Password Manager (Conceptual) ---")
    print("Commands: add <website> <username> <password>, get <website>, generate [length], exit")

    while True:
        command_input = input("> ").split(maxsplit=3)
        cmd = command_input[0].lower()

        if cmd == "add":
            if len(command_input) == 4:
                pm.add_password(command_input[1], command_input[2], command_input[3])
            else:
                print("Usage: add <website> <username> <password>")
        elif cmd == "get":
            if len(command_input) == 2:
                print(pm.get_password(command_input[1]))
            else:
                print("Usage: get <website>")
        elif cmd == "generate":
            length = int(command_input[1]) if len(command_input) == 2 else 12
            print(f"Generated password: {pm.generate_random_password(length)}")
        elif cmd == "exit":
            print("Exiting Password Manager.")
            break
        else:
            print("Unknown command.")
