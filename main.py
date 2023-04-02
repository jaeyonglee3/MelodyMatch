"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This is the main module where the entire program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
import application_ui
from user import User, construct_top_songs_list
import decision_tree
from decision_tree import load_tree_with_songs
from song import Song
import user_data
# from application_ui import UserInterface

import application_ui
import application_ui2
from song import load_songs


def get_spotify_data() -> None:
    """idk"""
    application_ui.create_window()


def run() -> None:
    songs = load_songs()
    tree = load_tree_with_songs(songs)
    # now you need a user, call generate user from user_data.py
    # now you need to call tree.find_songs_for_user(user) and visualize the results, maybe pass it into create_window
    application_ui2.create_window()
