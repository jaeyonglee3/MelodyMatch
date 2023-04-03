"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains the tkinter GUI used for starting the web server used to obtain
authorization to access data from the user's Spotify account.

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

import user_data


def create_initial_window() -> None:
    """Creates the Tkinter window used to start the local web-server used to obtain authoirzation to retrieve
    the user's top 50 most-listened to songs from their Spotify account.
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

    # Description
    desc = Label(root,
                 text='Welcome to MelodyMatch! \n\n'
                      "MelodyMatch is a personalized music recommendation app that analyzes your spotify "
                      "\nlistening history to suggest new songs that match your taste. By connecting "
                      "\nyour Spotify account, MelodyMatch will analyze your listening history\n data to suggest"
                      "new songs that are tailored to your taste."
                      "\n\nMelodyMatch is the perfect tool for discovering your next favorite song!\n\n",
                 bg='#0b2437',
                 fg='White',
                 font=('Verdana', 18))
    desc.pack()
    desc.place(relx=.5, rely=.5, anchor=CENTER)

    start_button = Button(root, text='Connect Spotify Account', font=('Verdana', 12, 'bold'), command=start_button_event)
    start_button.pack()
    start_button.config(width=15, height=2)
    start_button.place(x=530, rely=.7, anchor=CENTER)

    inst_button = Button(root, text='How Does This Work?', font=('Verdana', 12), command=create_instructions_window)
    inst_button.pack()
    inst_button.config(width=15, height=2)
    inst_button.place(x=695, rely=.7, anchor=CENTER)

    root.mainloop()


def start_button_event() -> None:
    """The event that happens when the "start" button on the GUI is pressed.

    The button will start the local web-server.
    """
    user_data.run_server()


def create_instructions_window() -> None:
    """Creates the Tkinter window used to start the local web-server used to obtain authoirzation to retrieve
    the user's top 50 most-listened to songs from their Spotify account.
    """
    image = Image.open("gui/instructions.jpg")

    width, height = image.size
    aspect_ratio = width / height

    # Set the maximum width and height of the image in the window
    max_width = 650
    max_height = 650

    if width > height:
        new_width = max_width
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = max_height
        new_width = int(new_height * aspect_ratio)

    image = image.resize((new_width, new_height), Image.ANTIALIAS)

    window = Toplevel()
    window.title('MelodyMatch - Instructions')
    img = ImageTk.PhotoImage(image)
    label = Label(window, image=img)
    label.image = img
    label.pack()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120
    })
