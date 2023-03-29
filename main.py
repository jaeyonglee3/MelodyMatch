"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module is the main module where the program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
track_names = []


def load_spotify_data():
    """Start the bottle server to log in with Spotify credentials on browser
    Retrieve and save all necessery information to appropriate variables.
    """
    import user_data
    global track_names

    track_names = user_data.track_names
    # todo call a method like construct_user_profile() here or something that makes a User object for the code to use


if __name__ == '__main__':
    import doctest
    import python_ta
    import python_ta.contracts

    load_spotify_data()
    doctest.testmod(verbose=True)

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'data_computations', 'recommendation_system'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': [],
    })
