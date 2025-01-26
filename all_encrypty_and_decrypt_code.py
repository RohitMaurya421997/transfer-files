import os
import hashlib
import base64
from cryptography.fernet import Fernet

def generate_fernet_key(custom_key):
    """Generates a valid Fernet key from a custom string."""
    hashed_key = hashlib.sha256(custom_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key[:32])



def encrypt_files(directory, custom_key):
    fernet_key = generate_fernet_key(custom_key)
    fernet = Fernet(fernet_key)


