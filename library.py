import Tkinter as tk

from room import Room

class Library(Room):
    shape = (5, 7)
    def __init__(self, parent):
        super(Library, self).__init__(parent, Library.shape, "Library ")

        self.lbl2 = tk.Label(self.frame, text="Wierd shape")
        self.lbl2.grid()