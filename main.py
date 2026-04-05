import encrypt
import decrypt
from csv_parsing import get_csv_headers, is_header_format_valid, csv_file_path
import logging
from typing import Literal
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pre_check_before_encryption(file_path: str) -> bool:
    headers = get_csv_headers()
    if headers is None:
        logging.error("Failed to read the CSV file. Please check the file path and try again.")
        return False

    if not is_header_format_valid(headers):
        logging.error("CSV file format is invalid. Please ensure it contains 'url', 'username', and 'password' headers.")
        return False
    
    return True

def main_terminal_default(action: Literal['E', 'D'] = None, file_path: str = None):
    global csv_file_path
    if action is None:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? (E/D): ")
    else:
        choice = action
    
    choice = choice.strip().upper()
    if not file_path:
        file_path = input("Enter the path to the CSV file: ")

    if choice == 'D':
        decrypt.main(file_path)

    elif choice == 'E':
        csv_file_path = file_path  # Update the global variable with the user-provided path
        response_of_checks = pre_check_before_encryption(file_path)

        if not response_of_checks:
            logging.error("Pre-checks failed. Encryption aborted.")
            choice_for_overwrite = input("Do you want to proceed with encryption anyway? (Y/N): ").strip().upper()
            if choice_for_overwrite != 'Y':
                return
        
        encrypt.main(file_path=file_path)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt CSV files containing credentials.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', help='Encrypt a CSV file', type=str, metavar='FILE_PATH', default=None)
    group.add_argument('-d', '--decrypt', help='Decrypt a CSV file', type=str, metavar='FILE_PATH', default=None)
    parser.add_argument('-p', '--password', help='Password for encryption/decryption (optional)', type=str, default=None)
    args = parser.parse_args()

    if not args.encrypt and not args.decrypt:
        main_terminal_default()
        return
    
    if args.encrypt:
        choice = 'E'
        filepath = args.encrypt
    else:
        choice = 'D'
        filepath = args.decrypt

    main_terminal_default(action=choice, file_path=filepath)

if __name__ == "__main__":
    main()