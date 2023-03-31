"""
THIS MODULE IS FOR EXPERIMENTAL PURPOSES ONLY

messing around with running the gui and the program on separate threads
so that we can properly kill the server without using ctrl + c
"""
import threading
import time
import bottle
import tkinter as tk


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        bottle.run()

    def stop(self):
        bottle.BaseRequest.MEMFILE_MAX = 0


class Gui:
    def __init__(self):
        self.server_thread = ServerThread()
        self.server_thread.start()

        self.root = tk.Tk()
        self.stop_button = tk.Button(self.root, text="Stop server", command=self.stop_server)
        self.stop_button.pack()
        self.root.mainloop()

    def stop_server(self):
        print("Hello")
        self.server_thread.stop()


Gui()
