# Decision Tree

import csv, random
from typing import Optional

class Song:
    """An object that represents a specific song.

        Instance Attributes
        - artist:
            Name of the artist that created the song.
        - name:
            Name of the song.
        - duration:
            Duration of the track in milliseconds.
        - explicit:
            Boolean that states whether the song contains swear words or not

        Representation Invariants:
        - self.address not in self.channels
        - all(self in channel.endpoints for channel in self.channels.values())

        """
    address: NodeAddress
    channels: dict[NodeAddress, Channel]


def read_and_write_csv(csv_file: str) -> None:
    """Reads data from the CSV file that the input refers to and loads it into a new CSV file
    called songs_final.csv. songs_final.csv will include only the songs and catergories we plan to use.

    Preconditions:
       - csv_file refers to a valid CSV file in the format described in the project proposal
    """
    with open(csv_file) as file:
        reader = csv.reader(file, delimiter=',')
