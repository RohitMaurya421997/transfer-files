import os
import hashlib
import base64
from cryptography.fernet import Fernet

def generate_fernet_key(custom_key):
    """Generates a valid Fernet key from a custom string."""
    hashed_key = hashlib.sha256(custom_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key[:32])

def encrypt_file(file_path, fernet):
    """Encrypts a single file."""
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, fernet):
    """Decrypts a single file."""
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_files(directory, custom_key):
    """Encrypts all .py, .html, and .pyc files in the specified directory using a custom key."""
    fernet_key = generate_fernet_key(custom_key)
    fernet = Fernet(fernet_key)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.html', '.pyc')):
                file_path = os.path.join(root, file)
                print(f"Encrypting: {file_path}")
                encrypt_file(file_path, fernet)

def decrypt_files(directory, custom_key):
    """Decrypts all .py, .html, and .pyc files in the specified directory using a custom key."""
    fernet_key = generate_fernet_key(custom_key)
    fernet = Fernet(fernet_key)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.html', '.pyc')):
                file_path = os.path.join(root, file)
                print(f"Decrypting: {file_path}")
                decrypt_file(file_path, fernet)

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        exit(1)

    custom_key = input("Enter your custom key (any string): ").strip()
    target_directory = input(f"Enter the directory to {mode} .py, .html, and .pyc files: ")

    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        try:
            if mode == "encrypt":
                encrypt_files(target_directory, custom_key)
                print("Encryption complete.")
            elif mode == "decrypt":
                decrypt_files(target_directory, custom_key)
                print("Decryption complete.")
        except Exception as e:
            print(f"An error occurred during {mode}: {e}")
    else:
        print("Invalid directory. Please try again.")
