import csv
import logging

logger = logging.getLogger(__name__)

csv_file_path = 'data.csv'      # Temporary file path for the CSV file

def get_csv_data_raw():
    try:
        with open(csv_file_path, mode='r') as csv_file:
            return csv_file.readlines()
    except FileNotFoundError:
        logger.error(f"File {csv_file_path} not found.")
        return None
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")
        return None

def get_csv_data_dict() -> list[dict[str, str]] | None:
    csv_data = get_csv_data_raw()
    if csv_data is None:
        return None
    csv_reader = csv.DictReader(csv_data)
    return list(csv_reader)  # Convert the reader to a list of dictionaries

def get_csv_headers():
    csv_data = get_csv_data_raw()
    if csv_data is None:
        return None
    csv_reader = csv.reader(csv_data)
    headers = next(csv_reader)  # Get the first row as headers
    return headers

def get_csv_rows():
    csv_data = get_csv_data_raw()
    if csv_data is None:
        return None
    csv_reader = csv.reader(csv_data)
    next(csv_reader)  # Skip headers
    rows = list(csv_reader)  # Get the remaining rows
    return rows

def write_csv_data(headers, rows, file_path: str):
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)  # Write headers
            csv_writer.writerows(rows)    # Write data rows
        logger.info(f"Data successfully written to {csv_file_path}.")
    except Exception as e:
        logger.error(f"An error occurred while writing to the file: {e}")

def is_header_format_valid(headers: list[str]) -> bool:
    if not headers:
        logger.warning("Headers are empty.")
        return False
    
    must_have = ["url", "username", "password"]

    for header in must_have:
        if header not in headers:
            logger.warning(f"Missing required header: {header}")
            return False
    
    return True