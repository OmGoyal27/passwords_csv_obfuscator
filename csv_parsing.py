import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

csv_file_path = 'data.csv'      # Temporary file path for the CSV file

def get_csv_data_raw():
    try:
        with open(csv_file_path, mode='r') as csv_file:
            return csv_file.readlines()
    except FileNotFoundError:
        logging.error(f"File {csv_file_path} not found.")
        return None
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
        return None

def get_csv_headers():
    csv_data = get_csv_data_raw()
    if csv_data is None:
        return None
    csv_reader = csv.reader(csv_data)
    headers = next(csv_reader)  # Get the first row as headers
    return headers