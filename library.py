import Tkinter as tk

from room import Room

class Library(Room):
    shape = (5, 7)
    def __init__(self, parent):
        # Use the parent frame to cover most of the library shape
        super(Library, self).__init__(parent, (5,6), "Library ")

        self.entrance_frame = tk.Frame(self.parent, borderwidth=1, relief=tk.GROOVE, background="blue")

    def grid(self, **kwargs):
        super(Library, self).grid(**kwargs)

        entrance_row = int(self.frame.grid_info()['row']) + 1
        entrance_column = int(self.frame.grid_info()['column']) + int(self.frame.grid_info()['columnspan'])

        self.entrance_frame.grid(row=entrance_row, column=entrance_column, rowspan=3, columnspan=1, sticky="nesw")