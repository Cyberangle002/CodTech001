from cryptography.fernet import Fernet
import os

def decrypt_file(file_path):
    key_path = "secret.key"

    if not os.path.exists(key_path):
        print("❌ secret.key not found! Keep it in the same folder.")
        return

    try:
        with open(key_path, "rb") as key_file:
            key = key_file.read()

        fernet = Fernet(key)

        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        # Remove .enc extension
        original_file = file_path.replace(".enc", "")

        with open(original_file, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"✅ File decrypted successfully: {original_file}")

    except Exception as e:
        print("❌ Decryption failed!")
        print("Reason:", str(e))

def main():
    print("=== File Decryption Tool ===")
    file_path = input("Enter encrypted file path (.enc): ").strip()

    if not file_path.endswith(".enc"):
        print("❌ Please provide a .enc file")
        return

    if not os.path.exists(file_path):
        print("❌ Encrypted file not found!")
        return

    decrypt_file(file_path)

if __name__ == "__main__":
    main()
