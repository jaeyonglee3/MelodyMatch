"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains ...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from __future__ import annotations
import csv
import random
from typing import Optional, Any


DECISION_TREE_ROOT = (0, 0)


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
        - tempo:
            The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the
            speed or pace of a given piece and derives directly from the average beat duration.

        Representation Invariants:
        - 0.0 <= self.danceability <= 1.0
        - 0.0 <= self.energy <= 1.0
        - -60.0 <= self.loudness <= 10.0
        - 0.0 <= self.speechiness <= 1.0
        - 0.0 <= self.acousticness <= 1.0
        - 0.0 <= self.instrumentalness <= 1.0
        - 0.0 <= self.valence <= 1.0
        - 0.0 <= self.liveness <= 1.0
        - self.tempo >= 0
        """
    name: str
    genre: str
    artist: str
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    liveness: float
    tempo: float


class DecisionTree:
    """A decision tree for organizing our songs.

    Each node in the tree either stores a range of numbers or a set of songs.

    Instance Attributes:
        - value: the current range of numbers or a set of songs if its is the leaf of the tree.

    Representation Invariants:
        - all(key == self._subtrees[key].value for key in self._subtrees)
    """
    value: Optional[set[Song] | tuple]

    # Private Instance Attributes:
    #  - _subtrees:
    #      the subtrees of this tree, which represent the decision trees after sorting the song by its attribute value.

    _subtrees: [list[DecisionTree]]

    def __init__(self, subtrees: list, value: set[Song] | tuple = DECISION_TREE_ROOT) -> None:
        """Initialize a new game tree.
        """
        self.value = value
        self._subtrees = subtrees

    def is_empty(self):
        """Return whether the tree is empty or not"""
        return self.value is None

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            str_so_far = '  ' * depth + f'{self.value}\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is modified.
                str_so_far += subtree._str_indented(depth + 1)
            return str_so_far

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def __len__(self) -> int:
        """Return the number of items contained in this tree.
        """
        if self.is_empty():
            return 0
        else:
            return 1 + sum(subtree.__len__() for subtree in self._subtrees)

    def add_subtree(self, subtree: DecisionTree) -> None:
        """Add a subtree to this game tree."""
        self._subtrees.append(subtree)


def generate_decision_tree(value: set[Song] | tuple, depth: int = 1) -> DecisionTree:
    """Add all the tuples and empty song sets into the decision tree."""
    decision_tree = DecisionTree(value=value, subtrees=[])

    if depth == 10:
        return decision_tree
    else:
        if depth == 3:
            ranges = [(-60, -37), (-36, -13), (-12, 10)]
            subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]

        elif depth == 9:
            ranges = [(0, 83), (84, 167), (168, 250)]
            subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]

        else:
            ranges = [(0.0, 0.3), (0.4, 0.7), (0.8, 1.0)]
            subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]

        for subtree in subtrees:
            decision_tree.add_subtree(subtree)

        return decision_tree


def insert_song() -> None:
    """Insert a song into the decision tree by recursing through the tree until it gets added to a specific song
    set.
    """
    # recursive


def insert_songs() -> None:
    """Insert a list of songs into the decision tree so that each song gets sorted into a specific song set."""
    # for loop and call recursive helper


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
