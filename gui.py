import tkinter as tk
from tkinter import messagebox
import board


class gui:
    def __init__(self, width, height, framerate):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.root = tk.Tk()
        self.CANVAS = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.pack()
        self.initialise_window()
        self.d = board.board(self.CANVAS, self.WIDTH, self.HEIGHT, self.FRAMERATE)
        self.window_destroy = False

    def initialise_window(self):

        def func_message():
            messagebox.showinfo(title="Engine", message="You have opened something")

        def quitting():
            self.window_destroy = True

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=quitting)
        menubar.add_cascade(label="File", menu=filemenu)

    def update_frames(self):
        self.d.update_frames(self.window_destroy)
