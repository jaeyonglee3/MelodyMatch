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
    top_songs = construct_top_songs_list(user_data.top_tracks_ids, user_data.top_tracks_energy,
                                         user_data.top_tracks_danceability, user_data.top_tracks_loudness,
                                         user_data.top_tracks_speechiness, user_data.top_tracks_acousticness,
                                         user_data.top_tracks_instrumentalness, user_data.top_tracks_valence,
                                         user_data.top_tracks_liveness, user_data.top_tracks_tempo)

    user_profile = User('username', top_songs)
    return user_profile


def run() -> None:
    """Run the entire program"""
    raise NotImplementedError


# def get_top_tracks():
#     """Return the top 50 tracks of the user from the Spotify API calls"""
#     for song in top_track_ids:
#         print(str(song))
#
#     return
#
#
# def get_energy_scores():
#     """Return the energy scores of the top 50 tracks of the user from the Spotify API calls"""
#     for score in top_track_energy_scores:
#         print(str(score))
#
#     return


if __name__ == '__main__':
    load_user()

    # PythonTA stuff
    # import doctest
    # import python_ta
    # import python_ta.contracts
    # doctest.testmod(verbose=True)
    #
    # python_ta.contracts.DEBUG_CONTRACTS = False
    # python_ta.contracts.check_all_contracts()
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts', 'data_computations', 'recommendation_system'],
    #     'allowed-io': [],
    #     'max-line-length': 100,
    #     'disable': [],
    # })
