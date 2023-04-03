"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This is the main module where the entire program is run.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use by students and faculty
of the CSC111 course department at the University of Toronto. All forms of distribution
of this code, whether as is or with changes, are prohibited. For more information on
copyright for this project's materials, please contact the developers directly.

This file is Copyright (c) 2023 Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from user import generate_user
from decision_tree import load_tree_with_songs
from song import load_songs

import launch_web_server_ui
import application_ui


def get_spotify_data() -> None:
    """Obtains authorization to access user's Spotify data.
    """
    launch_web_server_ui.create_window()


def run(use_example_data: bool) -> None:
    """Runs the recommendation algorithm and displays results.

    The use_example_data parameter determines whether to use data obtained from a Spotify account or
    the sample data provided.
    """
    try:
        songs = load_songs()
        tree = load_tree_with_songs(songs)
        user = generate_user(use_example_data)
        results = tree.find_songs_for_user(tree, user)
        application_ui.create_window(list(results))
    except FileNotFoundError:
        print('The necessary data could not be found! Make sure you run get_spotify_data() first. \n'
              'Did you want to use our provided example dataset? \n'
              'Make sure to call run() with the boolean argument True.')
