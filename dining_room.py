import Tkinter as tk
from room import Room

class DiningRoom(Room):
    shape = (7, 8)
    def __init__(self, parent):
        super(DiningRoom, self).__init__(parent, DiningRoom.shape, "Dining Room")

        self.lbl2 = tk.Label(self.frame, text="Wierd shape")
        self.lbl2.grid()