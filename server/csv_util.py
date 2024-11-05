# create a function to read csv file content using the csv reader lib

import csv
from typing import List

def read_csv_file(file_path: str) -> List[List[str]]:
    """
    Read the content of a CSV file and return it as a list of lists.
    
    :param file_path: The path to the CSV file.
    :return: The content of the CSV file as a list of lists.
    """
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        return [row for row in csv_reader]

def fetch_airports_list() -> List[dict]:
    """
    Read the content of the 'origin_airport.csv' file and return it as a list of dictionaries.
    
    :return: The content of the 'origin_airport.csv' file as a list of dictionaries.
    """
    airports = read_csv_file('origin_airport.csv')
    return [{"id": row[0], "name": row[1]} for row in airports]