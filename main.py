"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This is the main module where the entire program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from user import generate_user
from decision_tree import load_tree_with_songs
from song import load_songs

import launch_web_server_ui
import application_ui


def get_spotify_data() -> None:
    """Obtains authorization to access user's Spotify account to retrieve necessary data"""
    launch_web_server_ui.create_window()


def run() -> None:
    try:
        songs = load_songs()
        tree = load_tree_with_songs(songs)
        user = generate_user()
        results = tree.find_songs_for_user(tree, user)
        application_ui.create_window(list(results))
    except FileNotFoundError:
        print('The necessary data could not be found! Make sure you run get_spotify_data() first.')
