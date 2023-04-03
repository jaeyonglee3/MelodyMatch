"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains the tkinter GUI used to display the results of our recommendation
algorithm.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use by students and faculty
of the CSC111 course department at the University of Toronto. All forms of distribution
of this code, whether as is or with changes, are prohibited. For more information on
copyright for this project's materials, please contact the developers directly.

This file is Copyright (c) 2023 Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from math import ceil, floor
from tkinter import *
from PIL import ImageTk, Image
from song import Song


def create_window(results: list[Song]) -> None:
    """Creates the Tkinter window used to display the results of our recommendation algorithm.
    """
    root = Tk()

    w_ratio = 5 / 6
    h_ratio = 7 / 11

    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    window_width, window_height = floor(screen_width * w_ratio), floor(screen_height * h_ratio)

    x = ceil((screen_width / 2) - (window_width / 2))
    y = ceil((screen_height / 2) - (window_height / 1.85))

    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    root.title('MelodyMatch')
    root['bg'] = '#0b2437'

    logo = PhotoImage(file='gui/symbol.png')
    root.iconphoto(False, logo)

    full_logo = ImageTk.PhotoImage(Image.open('gui/logo.png'))
    full_logo_label = Label(root, image=full_logo, borderwidth=0)
    full_logo_label.pack(pady=window_height * 0.05)

    # List out the songs
    for song in results:
        text_to_display = song.name + ' by ' + song.artist
        title = Label(root, text=text_to_display, bg="#0b2437", fg="white", font=('Verdana', 18))
        title.place(x=5, y=0)
        title.pack()

    root.mainloop()
