# Decision Tree

import csv


def read_and_write_csv(csv_file: str) -> None:
    """Reads data from the CSV file that the input refers to and loads it into a new CSV file
    called songs_final.csv. songs_final.csv will include only the songs and catergories we plan to use.

    Preconditions:
       - csv_file refers to a valid CSV file in the format described in the project proposal
    """
    with open(csv_file) as file:
        reader = csv.reader(file, delimiter=',')
