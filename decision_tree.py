"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains ...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from __future__ import annotations
import csv
import itertools
import random
# from user import User
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


class DecisionTree:
    """A decision tree for organizing our songs.

    Each node in the tree either stores a range of numbers or a set of songs.

    Instance Attributes:
        - value: the current range of numbers or a set of songs if its is the leaf of the tree.

    Representation Invariants:
        - all(key == self._subtrees[key].value for key in self._subtrees)
    """
    value: Optional[tuple[int, set[Song]] | tuple]

    # Private Instance Attributes:
    #  - _subtrees:
    #      the subtrees of this tree, which represent the decision trees after sorting the song by its attribute value.

    _subtrees: [list[DecisionTree]]

    def __init__(self, subtrees: list, value: tuple[int, set[Song]] | tuple = DECISION_TREE_ROOT) -> None:
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

    def insert_songs(self, list_songs: list[Song]) -> None:
        """Insert a list of songs into the decision tree so that each song gets sorted into a specific song set.
        >>> tree = generate_decision_tree([0], (0,0), 1)
        >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
        >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_songs([song1, song2, song3])
        """
        for song in list_songs:
            self.insert_song(song)

    def insert_song(self, song: Song, depth: int = 1) -> None:
        """Insert a song into the decision tree by recursing through the tree until it gets added to a specific song
        set.

        >>> tree = generate_decision_tree((0,0), 1)
        >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
        >>> tree.insert_song(song1, 1)
        >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_song(song2, 1)
        >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_song(song3, 1)
        """
        score = 0

        if depth == 10:
            self.value[1].add(song)
        else:
            if depth == 1:
                score = song.danceability

            elif depth == 2:
                score = song.energy

            elif depth == 3:
                score = song.loudness

                if -60 <= score <= -42.5:
                    self._subtrees[0].insert_song(song, depth + 1)
                elif -42.4 <= score <= -25:
                    self._subtrees[1].insert_song(song, depth + 1)
                elif -24.9 <= score <= -7.5:
                    self._subtrees[2].insert_song(song, depth + 1)
                else:
                    self._subtrees[3].insert_song(song, depth + 1)

            elif depth == 4:
                score = song.speechiness

            elif depth == 5:
                score = song.acousticness

            elif depth == 6:
                score = song.instrumentalness

            elif depth == 7:
                score = song.valence

            elif depth == 8:
                score = song.liveness

        if depth != 3 and depth <= 9:
            if 0 <= score <= 0.25:
                self._subtrees[0].insert_song(song, depth + 1)
            elif 0.26 <= score <= 0.5:
                self._subtrees[1].insert_song(song, depth + 1)
            elif 0.51 <= score <= 0.75:
                self._subtrees[2].insert_song(song, depth + 1)
            else:
                self._subtrees[3].insert_song(song, depth + 1)


# def generate_decision_tree(value: tuple[int, set[Song]] | tuple, depth: int = 1, i: int = 0) -> DecisionTree:
#     """Add all the tuples and empty song sets into the decision tree."""
#     decision_tree = DecisionTree(value=value, subtrees=[])
#
#     if depth == 9:
#         decision_tree.add_subtree(DecisionTree(value=(i, set()), subtrees=[]))
#         return decision_tree
#     else:
#         if depth == 3:  # Loudness
#             ranges = [(-60.0, -42.5), (-42.4, -25.0), (-24.9, -7.50), (-7.40, 10.0)]
#             subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]
#
#         else:  # Everything else
#             ranges = [(0.00, 0.25), (0.26, 0.50), (0.51, 0.75), (0.76, 1.00)]
#             subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]
#
#         for subtree in subtrees:
#             decision_tree.add_subtree(subtree)
#
#         return decision_tree

def generate_decision_tree(indexes_so_far: list, value: tuple[int, set[Song]] | tuple, depth: int = 1, index: int = 0) -> DecisionTree:
    """Add all the tuples and empty song sets into the decision tree.

    >>> tree = generate_decision_tree([0], (0,0), 1, 0)
    >>> get_song_sets(tree)
    """
    decision_tree = DecisionTree(value=value, subtrees=[])

    if depth == 9:
        index = indexes_so_far[len(indexes_so_far) - 1] + 1
        indexes_so_far.append(index)
        decision_tree.add_subtree(DecisionTree(value=(index, set()), subtrees=[]))
        return decision_tree
    else:
        if depth == 3:  # Loudness
            ranges = [(-60.0, -42.5), (-42.4, -25.0), (-24.9, -7.50), (-7.40, 10.0)]
            subtrees = [generate_decision_tree(indexes_so_far, value, depth + 1, index) for value in ranges]

        else:  # Everything else
            ranges = [(0.00, 0.25), (0.26, 0.50), (0.51, 0.75), (0.76, 1.00)]
            subtrees = [generate_decision_tree(indexes_so_far, value, depth + 1, index) for value in ranges]

        for subtree in subtrees:
            decision_tree.add_subtree(subtree)

        return decision_tree


def get_song_sets(decision_tree: DecisionTree) -> list:
    """Return a list of all the leaf values in the decision tree which are sets of Song objects
    that have been sorted."""
    song_sets = []

    if not decision_tree._subtrees:
        song_sets.append(decision_tree.value)
    else:
        for subtree in decision_tree._subtrees:
            song_sets.extend(get_song_sets(subtree))

    return song_sets


#todo: delete function later
def check_correctedness(decision_tree: DecisionTree) -> bool:
    """Temporary. Checks if leaves are correct."""
    leaves = get_song_sets(decision_tree)
    value = 1

    for leaf in leaves:
        if leaf[0] != value:
            return False
        value += 1

    return True


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

        for row in reader:
            row_to_write = [row[1], row[17], row[0], row[6], row[7], row[9],
                            row[11], row[12], row[13], row[15], row[14]]
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
