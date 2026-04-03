from pathlib import Path
from crypto_funcs import decrypt
import pwinput

def main(file_path: str = None, password: str = None, suffix: str = '.csv'):
    if not file_path:
        file_path = input("Enter the path to the encrypted file: ")
    if not Path(file_path).is_file():
        print("File not found. Please check the path and try again.")
        return
    file_path = Path(file_path)
    if not password:
        password = pwinput.pwinput("Enter the password for decryption: ", "*")

    try:
        with file_path.open('r') as f:
            encrypted_content = f.read()
        decrypted_content = decrypt(encrypted_content, password)
        if decrypted_content is not None:
            with open(file_path.with_suffix(suffix), 'w') as f:
                f.write(decrypted_content)
        else:
            print("Decryption failed. Please check your password and try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()