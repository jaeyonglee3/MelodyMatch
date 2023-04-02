"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

Module Description
==================

This is the main module where the entire program is run.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
and faculty members who are part of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2023 Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from user import User, construct_top_songs_list
import decision_tree
from decision_tree import read_and_write_csv, songs_final_csv_to_songs, generate_decision_tree
from song import Song


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


def run() -> set[Song]:
    """The function (for now) to run and test the whole program

    >>> songs = run()
    >>> list = [(song.artist, song.name) for song in songs]  # this makes a list of (artist, title) of recommended songs
    """
    # read_and_write_csv("/Users/jaeyonglee/Desktop/csc111-group-project/data/songs_normalize.csv")
    read_and_write_csv("/Users/kevinhu/PycharmProjects/csc111-group-project/data/songs_normalize.csv")
    songs = songs_final_csv_to_songs()
    songs = list(songs)
    tree = generate_decision_tree((0, 0), 1)
    tree.insert_songs(songs)

    user = load_user()
    return tree.find_songs_for_user(tree, user)

# def run() -> None:
#     """Run the entire program"""
#     user = load_user()
