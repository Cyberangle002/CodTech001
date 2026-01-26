import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file"""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for block in iter(lambda: file.read(4096), b""):
                sha256.update(block)

        return sha256.hexdigest()

    except Exception as e:
        print("❌ Error reading file:", str(e))
        return None

def main():
    print("=== File Integrity Checker ===")
    file_path = input("Enter file path: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return

    print("\n1. Generate File Hash")
    print("2. Verify File Integrity")
    choice = input("Choose option (1/2): ").strip()

    if choice == "1":
        hash_value = calculate_hash(file_path)
        if hash_value:
            print("\n✅ File Hash (SHA-256):")
            print(hash_value)

    elif choice == "2":
        old_hash = input("Enter old hash value: ").strip()
        new_hash = calculate_hash(file_path)

        if not new_hash:
            return

        if old_hash == new_hash:
            print("\n✅ File is NOT modified.")
        else:
            print("\n⚠️ File HAS been modified!")

    else:
        print("❌ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
