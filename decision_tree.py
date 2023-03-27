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


        Representation Invariants:
        - self.address not in self.channels
        - all(self in channel.endpoints for channel in self.channels.values())

        """
    address: NodeAddress
    channels: dict[NodeAddress, Channel]







def read_and_write_csv(csv: str) -> None:
    """Reads data from our songs dataset"""
