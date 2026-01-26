from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and return a Fernet key"""
    return Fernet.generate_key()

def encrypt_file(file_path):
    try:
        key = generate_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        encrypted_file_path = file_path + ".enc"

        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        with open("secret.key", "wb") as key_file:
            key_file.write(key)

        print("✅ File encrypted successfully!")
        print(f"📁 Encrypted file: {encrypted_file_path}")
        print("🔑 Encryption key saved as: secret.key")

    except Exception as e:
        print("❌ Encryption failed!")
        print("Reason:", str(e))

def main():
    print("=== File Encryption Tool ===")
    file_path = input("Enter file path to encrypt: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return

    encrypt_file(file_path)

if __name__ == "__main__":
    main()
