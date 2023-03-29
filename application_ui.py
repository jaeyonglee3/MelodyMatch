"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains ...

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
import main
from math import ceil, floor
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Sets Window Size and Position
# Width and Height depend on screen size
w_ratio = 5 / 6
h_ratio = 7 / 11
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = floor(screen_width * w_ratio), floor(screen_height * h_ratio)
x = ceil((screen_width/2) - (window_width/2))
y = ceil((screen_height/2) - (window_height/1.85))
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Window Titlebar: Name and Symbol
root.title('MelodyMatch')
logo = PhotoImage(file='gui/symbol.png')
root.iconphoto(False, logo)

# Background Colour
root['bg'] = '#0b2437'

# Logo
full_logo = ImageTk.PhotoImage(Image.open('gui/logo.png'))
full_logo_label = Label(root, image=full_logo, borderwidth=0)
full_logo_label.pack(pady=window_height * 0.08)

# Description
desc = Label(root,
             text='Welcome to MelodyMatch! \n\n'
                  "MelodyMatch is a personalized music recommendation app that analyzes your spotify \nlistening "
                  "history to suggest new songs that match your individual taste. By connecting \nyour Spotify "
                  "account, MelodyMatch will access your listening history. MelodyMatch then \nanalyzes your data to "
                  "suggest new songs and artists that are tailored specifically to your\n taste. MelodyMatch provides "
                  "an intuitive user experience, with a clean interface that is \neasy to navigate. Whether you're "
                  "looking to add new tracks to your favorite playlist or \nwant to explore new genres, MelodyMatch is "
                  "the perfect tool for discovering your next \nfavorite song.\n\n",
             bg='#0b2437',
             fg='White',
             font=('Arial', 14))
desc.pack()


# Button
def button_event() -> None:
    """The event that happens when the following button is pressed"""
    main.run()


button = Button(root, text='Start', font=('Arial', 10))
button.pack()
button.config(width=10, height=2)

root.mainloop()
