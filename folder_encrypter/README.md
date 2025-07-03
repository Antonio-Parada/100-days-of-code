# Folder Encrypter

This project is a folder encrypter that can encrypt and lock a selected folder.

## Usage

1.  **Generate a key (do this once):**
    ```python
    from folder_encrypter import generate_key
    generate_key()
    ```
    This will create a `secret.key` file in the same directory.

2.  **Load the key:**
    ```python
    from folder_encrypter import load_key
    key = load_key()
    ```

3.  **Encrypt a folder:**
    ```python
    from folder_encrypter import encrypt_folder
    encrypt_folder("path/to/your/folder", key)
    ```

4.  **Decrypt a folder:**
    ```python
    from folder_encrypter import decrypt_folder
    decrypt_folder("path/to/your/folder", key)
    ```

**Note:** The encryption/decryption functions operate on all files within the specified folder and its subfolders. Be careful when using them.