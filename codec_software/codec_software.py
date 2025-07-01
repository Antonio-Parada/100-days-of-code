def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift) # Decrypt by shifting back

if __name__ == "__main__":
    print("--- Simple CLI Codec Software (Caesar Cipher) ---")
    print("Commands: encrypt <text> <shift>, decrypt <text> <shift>, exit")

    while True:
        command_input = input("> ").split(maxsplit=2)
        cmd = command_input[0].lower()

        if cmd == "encrypt":
            if len(command_input) == 3:
                try:
                    text = command_input[1]
                    shift = int(command_input[2])
                    encrypted_text = caesar_cipher_encrypt(text, shift)
                    print(f"Encrypted: {encrypted_text}")
                except ValueError:
                    print("Shift must be an integer.")
            else:
                print("Usage: encrypt <text> <shift>")
        elif cmd == "decrypt":
            if len(command_input) == 3:
                try:
                    text = command_input[1]
                    shift = int(command_input[2])
                    decrypted_text = caesar_cipher_decrypt(text, shift)
                    print(f"Decrypted: {decrypted_text}")
                except ValueError:
                    print("Shift must be an integer.")
            else:
                print("Usage: decrypt <text> <shift>")
        elif cmd == "exit":
            print("Exiting Codec Software.")
            break
        else:
            print("Unknown command.")
