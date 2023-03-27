# Decision Tree

import csv, random
from typing import Optional

class Song:
    """An object that represents a specific song.

        Instance Attributes
        - name:
            Name of the song.
        - artist:
            Name of the artist that created the song.
        - year:
            Song's year of release.
        - duration:
            Duration of the track in milliseconds.
        - explicit:
            Boolean that states whether the song contains swear words or not.
        - popularity:
            Popularity of the song. The higher the value, the more popular the song is.
        - danceability:
            Describes how suitable a track is for dancing based on a combination of musical elements including tempo,
            rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most
            danceable.
        - energy:
            Represents a perceptual measure of intensity and activity. A value of 0.0 represents the lowest energy and
            1.0 represents the highest energy.
        - key:
            The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭,
            2 = D, and so on. If no key was detected, the value is -1.
        - loudness:
            The overall loudness of a track in decibels (dB).
            Loudness values are averaged across the entire track and is the quality of a sound that is the primary
            psychological correlate of physical strength (amplitude). Values range between -60 and 0 db, where -60 db is
            the quietest and 0 db is the loudest
        -speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the
            recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66
            describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe
            tracks that may contain both music and speech, either in sections or layered, including such cases as rap
            music. Values below 0.33 most likely represent music and other non-speech-like tracks.
        - mode:
            Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content
            is derived. Major is represented by 1 and minor is 0.









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
