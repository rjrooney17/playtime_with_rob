import Tkinter as tk

from room import Room

class Conservatory(Room):
    shape = (5, 6)
    def __init__(self, parent):
        super(Conservatory, self).__init__(parent, Conservatory.shape, "Conservatory")

        self.lbl2 = tk.Label(self.frame, text="Wierd shape")
        self.lbl2.grid()