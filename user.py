"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains ...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from decision_tree import Song

class User:

    """An object that represents the user and stores its attributes

        Instance Attributes:
        - username:
            Spotify username of the user
        - top_listened_songs:
            The user's top 50 most-listened songs
        - user_danceability:
            Average danceability of the 50 most-listened songs of the user
        - user_energy:
            Average energy of the 50 most-listened songs of the user
        - user_loudness:
            Average loudness of the 50 most-listened songs of the user
        - user_speechiness:
            Average speechiness of the 50 most-listened songs of the user
        - user_acousticness:
            Average acousticness of the 50 most-listened songs of the user
        - user_instrumentalness:
            Average instrumentalness of the 50 most-listened songs of the user
        - user_valence:
            Average valence of the 50 most-listened songs of the user
        - user_liveness:
            Average liveness of the 50 most-listened songs of the user
        - user_tempo:
            Average tempo of the 50 most-listened songs of the user


        Representation Invariants:
        - type(self.username) == str
        - len(self.top_listened_songs) == 50
        - all(type(song) == Song for song in self.top_listened_songs)
    """

    username: str
    top_listened_songs: list[Song]
    user_danceability: float
    user_energy: float
    user_loudness: float
    user_speechiness: float
    user_acousticness: float
    user_instrumentalness: float
    user_valence: float
    user_liveness: float
    user_tempo: float

    def __init__(self, username: str) -> None:
        """Initialize a new user with given Spotify username
        """
        self.username = username
        self.find_top_songs()
        self.create_user_profile()

    def find_top_songs(self) -> list[Song]:
        """Return the user's 50 most-listened songs"""
        print("API call to find the user's top 50 songs")
        return [Song()]

    def create_user_profile(self) -> None:
        """Create the user's profile by finding the average values of the 50 most-listened songs of the user"""
        total_danceability = 0
        total_energy = 0
        total_loudness = 0
        total_speechiness = 0
        total_acousticness = 0
        total_instrumentalness = 0
        total_valence = 0
        total_liveness = 0
        total_tempo = 0

        for song in self.top_listened_songs:
            total_danceability += song.danceability
            total_energy += song.energy
            total_loudness += song.loudness
            total_speechiness += song.speechiness
            total_acousticness += song.acousticness
            total_instrumentalness += song.instrumentalness
            total_valence += song.valence
            total_liveness += song.liveness
            total_tempo += song.tempo

        self.user_danceability = total_danceability / len(self.top_listened_songs)
        self.user_energy = total_energy / len(self.top_listened_songs)
        self.user_loudness = total_loudness / len(self.top_listened_songs)
        self.user_speechiness = total_speechiness / len(self.top_listened_songs)
        self.user_acousticness = total_acousticness / len(self.top_listened_songs)
        self.user_instrumentalness = total_instrumentalness / len(self.top_listened_songs)
        self.user_valence = total_valence / len(self.top_listened_songs)
        self.user_liveness = total_liveness / len(self.top_listened_songs)
        self.user_tempo = total_tempo / len(self.top_listened_songs)
