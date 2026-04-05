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

def main_terminal_default(action: Literal['E', 'D'] = None):
    if action is None:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? (E/D): ")
    else:
        choice = action
    
    choice = choice.strip().upper()
    if choice == 'D':
        decrypt.main()
    elif choice == 'E':
        file_path = input("Enter the path to the CSV file: ")
        csv_file_path = file_path  # Update the global variable with the user-provided path

        response_of_checks = pre_check_before_encryption(file_path)

        if not response_of_checks:
            logging.error("Pre-checks failed. Encryption aborted.")
            choice_for_overwrite = input("Do you want to proceed with encryption anyway? (Y/N): ").strip().upper()
            if choice_for_overwrite != 'Y':
                return
        
        encrypt.main(file_path=file_path)

if __name__ == "__main__":
    main_terminal_default()