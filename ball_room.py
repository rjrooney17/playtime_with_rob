import Tkinter as tk
from room import Room

class BallRoom(Room):
    shape = (7, 8)
    def __init__(self, parent):
        super(BallRoom, self).__init__(parent, BallRoom.shape, "Ball Room")

        self.lbl2 = tk.Label(self.frame, text="Wierd shape")
        self.lbl2.grid()