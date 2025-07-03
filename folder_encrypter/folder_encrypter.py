from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the encryption key from the current directory."""
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    """Encrypts a single file."""
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Decrypts a single file."""
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    """Encrypts all files in a given folder and its subfolders."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    """Decrypts all files in a given folder and its subfolders."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

if __name__ == "__main__":
    # Example Usage:
    # 1. Generate a key (do this once)
    # generate_key()

    # 2. Load the key
    # key = load_key()

    # 3. Create a dummy folder and file for testing
    # os.makedirs("test_folder", exist_ok=True)
    # with open("test_folder/test_file.txt", "w") as f:
    #     f.write("This is a test file.")

    # 4. Encrypt the folder
    # encrypt_folder("test_folder", key)
    # print("Folder encrypted.")

    # 5. Decrypt the folder
    # decrypt_folder("test_folder", key)
    # print("Folder decrypted.")
