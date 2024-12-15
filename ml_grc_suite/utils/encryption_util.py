
# encryption_util.py - Data Encryption Utility for ML-GRC Suite

from cryptography.fernet import Fernet

def generate_key():
    """Generate and return a key for encryption."""
    key = Fernet.generate_key()
    return key

def save_key(key, file_path):
    """Save the encryption key to a file."""
    try:
        with open(file_path, "wb") as file:
            file.write(key)
        print(f"Encryption key saved to {file_path}.")
    except Exception as e:
        raise Exception(f"Error saving encryption key: {e}")

def load_key(file_path):
    """Load an encryption key from a file."""
    try:
        with open(file_path, "rb") as file:
            key = file.read()
        print(f"Encryption key loaded from {file_path}.")
        return key
    except Exception as e:
        raise Exception(f"Error loading encryption key: {e}")

def encrypt_data(data, key):
    """Encrypt data using the provided key."""
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data
    except Exception as e:
        raise Exception(f"Error encrypting data: {e}")

def decrypt_data(encrypted_data, key):
    """Decrypt data using the provided key."""
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception as e:
        raise Exception(f"Error decrypting data: {e}")
