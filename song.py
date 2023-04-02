"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

Module Description
==================

This Python module contains the Song class.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
and faculty members who are part of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2023 Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from typing import Optional
import csv


class Song:
    """An object that represents a specific song and stores its various song attributes.

        Instance Attributes
        - name:
            Name of the song.
        - genre:
            Genre of the track.
        - artist:
            Name of the artist that created the song.
        - danceability:
            Describes how suitable a track is for dancing based on a combination of musical elements including tempo,
            rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most
            danceable.
        - energy:
            Represents a perceptual measure of intensity and activity. A value of 0.0 represents the lowest energy and
            1.0 represents the highest energy.
        - loudness:
            The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and
            is the quality of a sound that is the primary psychological correlate of physical strength (amplitude).
            Values range between -60 and 10 db where -60 db is the quietest and 10 db is the loudest.
        - speechiness:
            Detects the presence of spoken words in a track. The more exclusively speech-like the
            recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66
            describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe
            tracks that may contain both music and speech, either in sections or layered, including such cases as rap
            music. Values below 0.33 most likely represent music and other non-speech-like tracks.
        - acousticness:
            A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 0.0 represents low confidence the
            track is acoustic and 1.0 represents high confidence the track is acoustic.
        - instrumentalness:
            Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this
            context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0,
            the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent
            instrumental tracks, but confidence is higher as the value approaches 1.0.
        - valence:
            A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence
            sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative
            (e.g. sad, depressed, angry).
        - liveness:
            Detects the presence of an audience in the recording. Higher liveness values represent an increased
            probability that the track was performed live. A value above 0.8 provides strong likelihood that the track
            is live.

        Representation Invariants:
        - 0.0 <= self.danceability <= 1.0
        - 0.0 <= self.energy <= 1.0
        - -60.0 <= self.loudness <= 10.0
        - 0.0 <= self.speechiness <= 1.0
        - 0.0 <= self.acousticness <= 1.0
        - 0.0 <= self.instrumentalness <= 1.0
        - 0.0 <= self.valence <= 1.0
        - 0.0 <= self.liveness <= 1.0
        """
    name: str
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    liveness: float
    genre: str
    artist: str

    def __init__(self, name: str, danceability: float, energy: float, loudness: float, speechiness: float,
                 acousticness: float, instrumentalness: float, valence: float, liveness: float,
                 genre: Optional[str] = None, artist: Optional[str] = None) -> None:
        """Initialize a Song object"""

        self.name = name
        self.danceability = danceability
        self.energy = energy
        self.loudness = loudness
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.valence = valence
        self.liveness = liveness
        self.genre = genre
        self.artist = artist


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
        writer.writerow(['Name', 'Genre', 'Artist', 'Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness',
                         'Instrumentalness', 'Valence', 'Liveness'])
        # Skips the Header
        next(reader)

        names_so_far = set()
        for row in reader:
            # Avoids Duplicate Songs
            if row[1] not in names_so_far:
                names_so_far.add(row[1])
                row_to_write = [row[1], row[17], row[0], row[6], row[7], row[9],
                                row[11], row[12], row[13], row[15], row[14]]
                writer.writerow(row_to_write)


def read_and_write_large_csv() -> None:
    """Loads and formats data from data/tracks_features.csv, and writes a new CSV file called large_songs_final.csv.
    large_songs_final.csv will include only the songs and catergories we plan to use.
    """
    with open('data/tracks_features.csv', errors='ignore') as input_file, \
            open('data/songs_normalize.csv', 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file, delimiter=',')
        # Writes the Header
        writer.writerow(['Name', 'Genre', 'Artist', 'Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness',
                         'Instrumentalness', 'Valence', 'Liveness'])
        # Skips the Header
        next(reader)

        names_so_far = set()
        for row in reader:
            # Avoids Duplicate Songs
            if row[1] not in names_so_far:
                names_so_far.add(row[1])
                row_to_write = [row[1], 'N/A', row[4].split("'")[1], row[9], row[10], row[12],
                                row[14], row[15], row[16], row[18], row[17]]
                writer.writerow(row_to_write)


def songs_final_csv_to_songs() -> set[Song]:
    """Reads rows from songs_final.csv and converts each row into a Song object.
    All Song objects will be put into a set."""
    with open('data/songs_final.csv') as file:
        final_csv_reader = csv.reader(file)

        # Skips Header
        next(final_csv_reader)

        songs_so_far = set()
        for song in final_csv_reader:
            songs_so_far.add(Song(name=song[0],
                                  danceability=round(float(song[3]), 2),
                                  energy=round(float(song[4]), 2),
                                  loudness=round(float(song[5]), 1),
                                  speechiness=round(float(song[6]), 2),
                                  acousticness=round(float(song[7]), 2),
                                  instrumentalness=round(float(song[8]), 2),
                                  valence=round(float(song[9]), 2),
                                  liveness=round(float(song[10]), 2),
                                  genre=song[1],
                                  artist=song[2]
                                  )
                             )
        return songs_so_far


def load_songs() -> list[Song]:
    """NEW ... returns a list of songs from read from the csv"""
    read_and_write_large_csv()
    songs = list(songs_final_csv_to_songs())
    return songs
