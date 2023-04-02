"""
BRUH ...
"""
from math import ceil, floor
from tkinter import *
from PIL import ImageTk, Image
from song import Song


def create_window(results: list[Song]):
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
    one_song = results[0].artist
    desc = Label(root,
                 text=one_song,
                 bg='#0b2437',
                 fg='White',
                 font=('Verdana', 18))
    desc.pack()

    root.mainloop()
