from pathlib import Path
from crypto_funcs import encrypt

def main(suffix: str = '.enc'):
    file_path = input("Enter the path to the CSV file: ")
    if not Path(file_path).is_file():
        print("File not found. Please check the path and try again.")
        return
    file_path = Path(file_path)
    password = input("Enter the password for encryption: ")

    try:
        with file_path.open('r') as f:
            content = f.read()
        encrypted_content = encrypt(content, password)
        encrypted_file_path = file_path.with_suffix(suffix)
        with encrypted_file_path.open('w') as f:
            f.write(encrypted_content)
        print(f"File encrypted successfully. Encrypted file: {encrypted_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()