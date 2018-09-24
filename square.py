import Tkinter as tk


class Square(object):
    def __init__(self, parent, background):
        self.shape = (1, 1)
        self.frame = tk.Frame(parent)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.lbl = tk.Label(self.frame, relief=tk.RIDGE, bg=background)
        self.lbl.grid(sticky="nesw")

    def grid(self, **kwargs):
        self.frame.grid(row=kwargs["row"], column=kwargs["column"], sticky="nesw")


class WalkingSquare(Square):
    def __init__(self, parent):
        super(WalkingSquare, self).__init__(parent, "yellow")

    def place_player(self, player):
        self.lbl.grid_remove()
        canvas = tk.Canvas(self.frame, height=1, width=1, relief=tk.RIDGE, bg="yellow")
        canvas.create_oval(5, 5, 10, 10, fill=player.color)
        canvas.grid(sticky="nesw")


class EmptySquare(Square):
    def __init__(self, parent):
        super(EmptySquare, self).__init__(parent, "white")

