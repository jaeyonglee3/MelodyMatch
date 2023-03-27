# Decision Tree

import csv, random
from typing import Optional

# class Song:
#     """An object that represents a specific song.
#
#         Instance Attributes
#         - artist:
#             Name of the artist that created the song.
#         - name:
#             Name of the song.
#         - duration:
#             Duration of the track in milliseconds.
#         - explicit:
#             Boolean that states whether the song contains swear words or not
#
#         Representation Invariants:
#         - self.address not in self.channels
#         - all(self in channel.endpoints for channel in self.channels.values())
#
#         """
#     address: NodeAddress
#     channels: dict[NodeAddress, Channel]


def read_and_write_csv(csv_file: str) -> None:
    """Loads data from a CSV file, and writes a new CSV file called songs_final.csv.
    songs_final.csv will include only the songs and catergories we plan to use.

    Preconditions:
       - csv_file refers to a valid CSV file in the format described in the project proposal
    """
    with open(csv_file) as input_file, open('data/songs_final.csv', 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file, delimiter=',')
        # Writes the Header
        writer.writerow(['Artist', 'Song', 'Liveness', 'Explicit', 'Year', 'Popularity', 'Danceability',
                         'Energy', 'Speechiness', 'Loudness'])
        # Skips the Header
        next(reader)

        for row in reader:
            row_to_write = [row[0], row[1], row[14], row[3], row[4], row[5], row[6], row[7], row[11], row[9]]
            writer.writerow(row_to_write)
