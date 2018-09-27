import Tkinter as tk


class SingleSquare(object):
    def __init__(self, parent, background):
        self.shape = (1, 1)
        # self.frame = tk.Frame(parent, background="black")
        self.lbl = tk.Label(parent, height=1, width=1, relief=tk.SUNKEN, bg=background)
        # self.lbl.grid()

    def grid(self, **kwargs):
        #self.frame.grid(row=kwargs["row"], column=kwargs["column"], sticky="nesw")
        self.lbl.grid(row=kwargs["row"], column=kwargs["column"], sticky="nesw")