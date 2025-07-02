import os
from cryptography.fernet import Fernet

class FolderEncrypter:
    def __init__(self, key_path='secret.key'):
        self.key_path = key_path
        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)

    def load_or_generate_key(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(key)
            return key

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = self.fernet.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted_data = self.fernet.decrypt(data)
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)

    def process_folder(self, folder_path, mode):
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if mode == 'encrypt':
                    self.encrypt_file(file_path)
                elif mode == 'decrypt':
                    self.decrypt_file(file_path)

if __name__ == '__main__':
    encrypter = FolderEncrypter()
    print("--- Folder Encrypter ---")
    folder = input("Enter the path to the folder: ")
    mode = input("Encrypt or Decrypt? (e/d): ").lower()

    if mode == 'e':
        encrypter.process_folder(folder, 'encrypt')
        print("Folder encrypted successfully.")
    elif mode == 'd':
        encrypter.process_folder(folder, 'decrypt')
        print("Folder decrypted successfully.")
    else:
        print("Invalid mode.")