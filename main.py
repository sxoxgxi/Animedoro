import time
import threading
import tkinter as tk
from tkinter import PhotoImage


class AnimedoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Animedoro")
        self.root.call('wm', 'iconphoto', self.root._w,
                       PhotoImage(file="clock.png"))
        self.root.mainloop()

    def start(self):
        pass

    def timer_thread(self):
        pass

    def reset(self):
        pass

    def skip(self):
        pass


AnimedoroTimer()
