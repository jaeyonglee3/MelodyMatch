"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains the DecisionTree class...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from __future__ import annotations
import random
from user import User
from typing import Optional

from song import Song


DECISION_TREE_ROOT = (0, 0)

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

    def get_subtrees(self) -> list[DecisionTree]:
        """Return the subtrees of a Decision Tree"""
        return self._subtrees

    def add_subtree(self, subtree: DecisionTree) -> None:
        """Add a subtree to this game tree."""
        self._subtrees.append(subtree)

    # def insert_songs(self, list_songs: list[Song]) -> None:
    #     """Insert a list of songs into the decision tree so that each song gets sorted into a specific song set.
    #     >>> tree = generate_decision_tree([0], (0,0), 1)
    #     >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
    #     >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    #     >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    #     >>> tree.insert_songs([song1, song2, song3])
    #     """
    #     for song in list_songs:
    #         self.insert_song(song, 1)

    def insert_songs(self, list_songs: list[Song]) -> None:
        """Insert a list of songs into the decision tree so that each song gets sorted into a specific song set.
        >>> tree = generate_decision_tree((0,0), 1)
        >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
        >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_songs([song1, song2, song3])
        >>> l = get_song_sets(tree)
        >>> [song for song in l[0][1]][0].name
        'I hate MAT137'
        >>> [song for song in l[1][1]][0].name
        'I love IMM250'
        """
        i = [0]
        for song in list_songs:
            self.insert_song(i, song, 1)

    # def insert_song(self, song: Song, depth: int = 1) -> None:
    #     """Insert a song into the decision tree by recursing through the tree until it gets added to a specific song
    #     set.
    #
    #     >>> tree = generate_decision_tree([0], (0,0), 1)
    #     >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
    #     >>> tree.insert_song(song1, 1)
    #     >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    #     >>> tree.insert_song(song2, 1)
    #     >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    #     >>> tree.insert_song(song3, 1)
    #     """
    #     score = 0
    #
    #     if depth == 10:
    #         self.value[1].add(song)
    #     else:
    #         if depth == 1:
    #             score = song.danceability
    #
    #         elif depth == 2:
    #             score = song.energy
    #
    #         elif depth == 3:
    #             score = song.loudness
    #
    #             if -60 <= score <= -42.5:
    #                 self._subtrees[0].insert_song(song, depth + 1)
    #             elif -42.4 <= score <= -25:
    #                 self._subtrees[1].insert_song(song, depth + 1)
    #             elif -24.9 <= score <= -7.5:
    #                 self._subtrees[2].insert_song(song, depth + 1)
    #             else:
    #                 self._subtrees[3].insert_song(song, depth + 1)
    #
    #         elif depth == 4:
    #             score = song.speechiness
    #
    #         elif depth == 5:
    #             score = song.acousticness
    #
    #         elif depth == 6:
    #             score = song.instrumentalness
    #
    #         elif depth == 7:
    #             score = song.valence
    #
    #         elif depth == 8:
    #             score = song.liveness
    #
    #     if depth != 3 and depth <= 9:
    #         if 0 <= score <= 0.25:
    #             self._subtrees[0].insert_song(song, depth + 1)
    #         elif 0.26 <= score <= 0.5:
    #             self._subtrees[1].insert_song(song, depth + 1)
    #         elif 0.51 <= score <= 0.75:
    #             self._subtrees[2].insert_song(song, depth + 1)
    #         else:
    #             self._subtrees[3].insert_song(song, depth + 1)

    #todo: remove index attribute
    def insert_song(self, index: list, song: Song, depth: int = 1) -> None:
        """Insert a song into the decision tree by recursing through the tree until it gets added to a specific song
        set.

        >>> tree = generate_decision_tree((0,0), 1)
        >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
        >>> tree.insert_song([0], song1, 1)
        >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_song([0], song2, 1)
        >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
        >>> tree.insert_song([0], song3, 1)
        """
        score = 0

        if depth == 9:
            if len(self._subtrees) == 0:
                i = len(index)
                self.add_subtree(DecisionTree(value=(i, {song}), subtrees=[]))
                index.append(0)
            else:
                self._subtrees[0].value[1].add(song)
        else:
            if depth == 1:
                score = song.danceability

            elif depth == 2:
                score = song.energy

            elif depth == 3:
                score = song.loudness

                if -60 <= score <= -42.5:
                    self._subtrees[0].insert_song(index, song, depth + 1)
                elif -42.4 <= score <= -25:
                    self._subtrees[1].insert_song(index, song, depth + 1)
                elif -24.9 <= score <= -7.5:
                    self._subtrees[2].insert_song(index, song, depth + 1)
                else:
                    self._subtrees[3].insert_song(index, song, depth + 1)

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
                self._subtrees[0].insert_song(index, song, depth + 1)
            elif 0.26 <= score <= 0.5:
                self._subtrees[1].insert_song(index, song, depth + 1)
            elif 0.51 <= score <= 0.75:
                self._subtrees[2].insert_song(index, song, depth + 1)
            else:
                self._subtrees[3].insert_song(index, song, depth + 1)

    def find_songs_for_user(self, user: User, depth: int = 1) -> list[Song]:
        """Return a list of songs tailored to the User's calculated preference values.
        >>> tree = generate_decision_tree((0,0), 1)
        >>> user =
        >>> self.find_songs_for_user(user)
        """
        score = 0

        if depth == 10:
            return list(self.value[1])
        else:
            if depth == 1:
                score = user.user_danceability

            elif depth == 2:
                score = user.user_energy

            elif depth == 3:
                score = user.user_loudness

                if -60 <= score <= -42.5:
                    return self._subtrees[0].find_songs_for_user(user, depth + 1)
                elif -42.4 <= score <= -25:
                    return self._subtrees[1].find_songs_for_user(user, depth + 1)
                elif -24.9 <= score <= -7.5:
                    return self._subtrees[2].find_songs_for_user(user, depth + 1)
                else:
                    return self._subtrees[3].find_songs_for_user(user, depth + 1)

            elif depth == 4:
                score = user.user_speechiness

            elif depth == 5:
                score = user.user_acousticness

            elif depth == 6:
                score = user.user_instrumentalness

            elif depth == 7:
                score = user.user_valence

            elif depth == 8:
                score = user.user_liveness

        if depth != 3 and depth <= 9:
            if 0 <= score <= 0.25:
                return self._subtrees[0].find_songs_for_user(user, depth + 1)
            elif 0.26 <= score <= 0.5:
                return self._subtrees[1].find_songs_for_user(user, depth + 1)
            elif 0.51 <= score <= 0.75:
                return self._subtrees[2].find_songs_for_user(user, depth + 1)
            else:
                return self._subtrees[3].find_songs_for_user(user, depth + 1)


def generate_decision_tree(value: tuple[int, set[Song]] | tuple, depth: int = 1) \
        -> DecisionTree:
    """Add all the tuples and empty song sets into the decision tree.

    >>> tree = generate_decision_tree((0,0), 1)
    >>> get_song_sets(tree)
    >>> read_and_write_csv("/Users/jaeyonglee/Desktop/csc111-group-project/data/songs_normalize.csv")
    >>> songs = songs_final_csv_to_songs()
    >>> songs = list(songs)
    >>> tree = generate_decision_tree((0,0), 1)
    >>> tree.insert_songs(songs)
    >>> list_of_leafs = get_song_sets(tree)
    >>> songs = [tuple[1] for tuple in list_of_leafs if tuple[1] != set()]
    >>> sum([len(set) for set in songs])
    """
    decision_tree = DecisionTree(value=value, subtrees=[])

    if depth == 9:
        return decision_tree
    else:
        if depth == 3:  # Loudness
            ranges = [(-60.0, -42.5), (-42.4, -25.0), (-24.9, -7.50), (-7.40, 10.0)]
            subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]

        else:  # Everything else
            ranges = [(0.00, 0.25), (0.26, 0.50), (0.51, 0.75), (0.76, 1.00)]
            subtrees = [generate_decision_tree(value, depth + 1) for value in ranges]

        for subtree in subtrees:
            decision_tree.add_subtree(subtree)

        return decision_tree


def load_tree_with_songs(songs: list[Song]) -> DecisionTree:
    """Generate a tree and insert the given songs"""
    tree = generate_decision_tree((0, 0), 1)
    tree.insert_songs(songs)
    return tree


def get_song_sets(decision_tree: DecisionTree) -> list:
    """Return a list of all the leaf values in the decision tree which are sets of Song objects
    that have been sorted.

    >>> tree = generate_decision_tree((0,0), 1)
    >>> song1 = Song('I hate MAT137', 0, 0, -60, 0, 0, 0, 0, 0)
    >>> song2 = Song('I hate MAT223', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    >>> song3 = Song('I hate IMM250', 0.5, 0.3, -8, 1.0, 0.9, 0.4, 0.3, 0.2)
    >>> song4 = Song('I love IMM250', 1.0, 1.0, 10, 1.0, 1.0, 1.0, 1.0, 1.0)
    >>> tree.insert_songs([song1, song4])
    >>> l = get_song_sets(tree)
    >>> [song for song in l[0][1]][0].name
    'I hate MAT137'
    >>> [song for song in l[1][1]][0].name
    'I love IMM250'

    """
    song_sets = []

    if not decision_tree.get_subtrees() and isinstance(decision_tree.value[1], set):
        song_sets.append(decision_tree.value)
    else:
        for subtree in decision_tree.get_subtrees():
            song_sets.extend(get_song_sets(subtree))

    return song_sets
