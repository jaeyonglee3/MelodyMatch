"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module is the main module where the program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
# top_track_ids = []
# top_track_energy_scores = []


def load_spotify_data():
    """Start the bottle server to log in with Spotify credentials on browser
    Retrieve and save all necessery information to appropriate variables.
    """
    import user_data
    # global top_track_ids, top_track_energy_scores

    top_track_ids = user_data.top_tracks_ids
    top_track_energy_scores = user_data.top_tracks_energy
    # todo call a method like construct_user_profile() here or something that makes a User object for the code to use


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
    load_spotify_data()

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
