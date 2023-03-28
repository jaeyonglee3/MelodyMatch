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


class DecisionTree:
    """A decision tree for organizing our songs.

    Each node in the tree either stores a range of numbers or a set of songs.

    Instance Attributes:
        - move: the current move (guess or status), or '*' if this tree represents the start of a game
        - guesser_win_probability: the probability that the Guesser will win from the current state of the game

    Representation Invariants:
        - self.move == GAME_START_MOVE or self.move is a valid Adversarial Wordle move
        - all(key == self._subtrees[key].move for key in self._subtrees)
        - GAME_START_MOVE not in self._subtrees  # since it can only appear at the very top of a game tree
        - 0.0 <= self.guesser_win_probability <= 1.0
    """
    value: set[Song] | tuple[float, float]  # The vertical bar | means "or"
    guesser_win_probability: Optional[float]

    # Private Instance Attributes:
    #  - _subtrees:
    #      the subtrees of this tree, which represent the decision trees after sorting the song by its attribute value.

    _subtrees: list[Song | tuple[float, float]]

    def __init__(self, move: str | tuple[str, ...] = GAME_START_MOVE, guesser_win_probability: Optional[float] = 0.0) \
            -> None:
        """Initialize a new game tree.

        Note that this initializer uses optional arguments.

        >>> game = GameTree()
        >>> game.move == GAME_START_MOVE
        True
        """
        self.move = move
        self._subtrees = {}
        self.guesser_win_probability = guesser_win_probability


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
