"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This is the main module where the entire program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from user import User, construct_top_songs_list


def load_user() -> User:
    """ This function runs user_data.py which will start the Bottle server used to log in with
    Spotify credentials on the user's browser.

    After retrieving all necessary information, this function returns an instance of the User class.
    """
    import user_data
    user_data.run_server()
    top_songs = construct_top_songs_list(user_data.top_tracks_ids, user_data.top_tracks_energy,
                                         user_data.top_tracks_danceability, user_data.top_tracks_loudness,
                                         user_data.top_tracks_speechiness, user_data.top_tracks_acousticness,
                                         user_data.top_tracks_instrumentalness, user_data.top_tracks_valence,
                                         user_data.top_tracks_liveness)

    user_profile = User(top_songs)  # Create an instance of the "User" class
    return user_profile


def run() -> None:
    """Run the entire program"""
    user = load_user()
    return ...
