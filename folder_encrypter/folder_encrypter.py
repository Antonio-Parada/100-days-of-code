from cryptography.fernet import Fernet
import os
import argparse
from tqdm import tqdm

def generate_key(key_path="secret.key"):
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved to {key_path}")

def load_key(key_path="secret.key"):
    """Loads the encryption key from the specified path."""
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found at {key_path}. Please generate a key first.")
    return open(key_path, "rb").read()

def process_file(file_path, key, mode):
    """Encrypts or decrypts a single file."""
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        if mode == 'encrypt':
            processed_data = f.encrypt(file_data)
        elif mode == 'decrypt':
            processed_data = f.decrypt(file_data)
        else:
            return

        with open(file_path, "wb") as file:
            file.write(processed_data)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def process_folder(folder_path, key, mode):
    """Encrypts or decrypts all files in a given folder and its subfolders."""
    file_paths = [os.path.join(root, file) for root, _, files in os.walk(folder_path) for file in files]
    
    if not file_paths:
        print(f"No files found in {folder_path}")
        return

    with tqdm(total=len(file_paths), desc=f"{mode.capitalize()}ing files") as pbar:
        for file_path in file_paths:
            process_file(file_path, key, mode)
            pbar.update(1)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a folder.")
    parser.add_argument("action", choices=["encrypt", "decrypt", "generatekey"], help="Action to perform")
    parser.add_argument("path", nargs='?', help="Path to the folder or key file")
    parser.add_argument("--key", default="secret.key", help="Path to the encryption key file")

    args = parser.parse_args()

    if args.action == "generatekey":
        generate_key(args.path or "secret.key")
        return

    if not args.path:
        parser.error("The 'path' argument is required for encrypt/decrypt actions.")

    try:
        key = load_key(args.key)
        if args.action == "encrypt":
            process_folder(args.path, key, 'encrypt')
        elif args.action == "decrypt":
            process_folder(args.path, key, 'decrypt')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()