from pathlib import Path
from crypto_funcs import encrypt
import pwinput
import logging

logger = logging.getLogger(__name__)

def main(file_path: str | Path = None, password: str = None, suffix: str = '.enc'):
    if not file_path:
        file_path = input("Enter the path to the CSV file: ")
    if not Path(file_path).is_file():
        logger.error("File not found. Please check the path and try again.")
        return
    file_path = Path(file_path)
    
    if not password:
        password = pwinput.pwinput(prompt="Enter the password for encryption: ", mask='*')

    try:
        with file_path.open('r') as f:
            content = f.read()
        encrypted_content = encrypt(content, password)
        encrypted_file_path = file_path.with_suffix(suffix)
        with encrypted_file_path.open('w') as f:
            f.write(encrypted_content)
        logger.info(f"File encrypted successfully. Encrypted file: {encrypted_file_path}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()