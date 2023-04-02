"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains ...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from song import Song


def construct_top_songs_list(top_tracks_ids: list[str], top_tracks_energy: list[float],
                             top_tracks_danceability: list[float], top_tracks_loudness: list[float],
                             top_tracks_speechiness: list[float], top_tracks_acousticness: list[float],
                             top_tracks_instrumentalness: list[float], top_tracks_valence: list[float],
                             top_tracks_liveness: list[float]
                             ) -> list[Song]:
    """Construct a list of Song objects from the user top tracks csv file, later ot be used for
    song recommendation algorithm.
    """
    top_songs = []
    for i in range(len(top_tracks_ids)):
        song = Song(name=top_tracks_ids[i], danceability=top_tracks_danceability[i], energy=top_tracks_energy[i],
                    loudness=top_tracks_loudness[i], speechiness=top_tracks_speechiness[i],
                    acousticness=top_tracks_acousticness[i], instrumentalness=top_tracks_instrumentalness[i],
                    valence=top_tracks_valence[i], liveness=top_tracks_liveness[i])
        top_songs.append(song)

    return top_songs


class User:
    """An object that represents the user and stores its attributes

        Instance Attributes:
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

        Representation Invariants:
        - len(self.top_listened_songs) == 50
        - all(type(song) == Song for song in self.top_listened_songs)
        - 0.0 <= self.user_danceability <= 1.0
        - 0.0 <= self.user_energy <= 1.0
        - -60.0 <= self.user_loudness <= 10.0
        - 0.0 <= self.user_speechiness <= 1.0
        - 0.0 <= self.user_acousticness <= 1.0
        - 0.0 <= self.user_instrumentalness <= 1.0
        - 0.0 <= self.user_valence <= 1.0
        - 0.0 <= self.user_liveness <= 1.0
    """
    top_listened_songs: list[Song]
    user_danceability: float
    user_energy: float
    user_loudness: float
    user_speechiness: float
    user_acousticness: float
    user_instrumentalness: float
    user_valence: float
    user_liveness: float

    def __init__(self, top_listened_songs: list[Song]) -> None:
        """Initialize a new user with given Spotify username
        """
        self.top_listened_songs = top_listened_songs
        self.create_user_profile()

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

        for song in self.top_listened_songs:
            total_danceability += song.danceability
            total_energy += song.energy
            total_loudness += song.loudness
            total_speechiness += song.speechiness
            total_acousticness += song.acousticness
            total_instrumentalness += song.instrumentalness
            total_valence += song.valence
            total_liveness += song.liveness

        self.user_danceability = total_danceability / len(self.top_listened_songs)
        self.user_energy = total_energy / len(self.top_listened_songs)
        self.user_loudness = total_loudness / len(self.top_listened_songs)
        self.user_speechiness = total_speechiness / len(self.top_listened_songs)
        self.user_acousticness = total_acousticness / len(self.top_listened_songs)
        self.user_instrumentalness = total_instrumentalness / len(self.top_listened_songs)
        self.user_valence = total_valence / len(self.top_listened_songs)
        self.user_liveness = total_liveness / len(self.top_listened_songs)
