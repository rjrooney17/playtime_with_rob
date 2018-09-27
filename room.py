import Tkinter as tk

class Room(object):
    def __init__(self, parent, shape, text):
        self.parent = parent
        self.shape = shape
        self.frame = tk.Frame(parent, borderwidth=1, relief=tk.GROOVE, background="green")
        self.lbl = tk.Label(self.frame, text=text)
        self.lbl.place(relx=.5, rely=.5, anchor="center")

    def grid(self, **kwargs):
        self.frame.grid(row=kwargs["row"], column=kwargs["column"], rowspan=self.shape[0], columnspan=self.shape[1], sticky="nesw")