"""
BRUH
"""
from math import ceil, floor
from tkinter import *
from PIL import ImageTk, Image

import user_data


def create_window():
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
                 text='hello',
                 bg='#0b2437',
                 fg='White',
                 font=('Verdana', 18))
    desc.pack()

    button = Button(root, text='Start', font=('Verdana', 12), command=start_button_event)
    button.pack()
    button.config(width=10, height=2)

    root.mainloop()


def start_button_event() -> None:
    """The event that happens when the following button is pressed"""
    # main.run_program()
    user_data.load_user()
