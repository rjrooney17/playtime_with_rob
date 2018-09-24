import Tkinter as tk
from room import Room

class DiningRoom(Room):
    shape = (7, 8)
    def __init__(self, parent):
        #Use the parent frame for most of the dining room
        super(DiningRoom, self).__init__(parent, (6,8), "Dining Room")

        self.extra_frame = tk.Frame(self.parent, borderwidth=1, relief=tk.GROOVE, background="blue")

    def grid(self, **kwargs):
        super(DiningRoom, self).grid(**kwargs)

        extra_row = int(self.frame.grid_info()['row']) + int(self.frame.grid_info()['rowspan'])
        extra_column = int(self.frame.grid_info()['column']) + 3

        self.extra_frame.grid(row=extra_row, column=extra_column, rowspan=1, columnspan=4, sticky="nesw")