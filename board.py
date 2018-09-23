
import Tkinter as tk

from hall import Hall
from study import Study
from lounge import Lounge
from library import Library
from stairs import Stairs
from dining_room import DiningRoom
from billiard_room import BilliardRoom
from conservatory import Conservatory
from ball_room import BallRoom
from kitchen import Kitchen

class SingleSquare(object):
    def __init__(self, parent, background):
        self.shape = (1, 1)
        self.frame = tk.Frame(parent, background="black")
        self.lbl = tk.Label(self.frame, height=1, width=1, relief=tk.RIDGE, bg=background)
        self.lbl.grid()

    def grid(self, **kwargs):
        self.frame.grid(row=kwargs["row"], column=kwargs["column"], sticky="nesw")

class WalkingSquare(SingleSquare):
    def __init__(self, parent):
        super(WalkingSquare, self).__init__(parent, "yellow")

class Empty(SingleSquare):
    def __init__(self, parent):
        super(Empty, self).__init__(parent, "white")




class Board(object):
    def __init__(self, parent):
        self.shape = (25, 24)
        assert self.shape[0] == len(walking_squares)
        for r in walking_squares:
            assert self.shape[1] == len(r), "Mismatched shapes {}".format(len(r))

        # Visualization, get it outta here
        parent.grid_columnconfigure(0, minsize=5)
        frame = tk.Frame(parent, border=3, relief=tk.GROOVE)
        frame.grid()

        self.squares = [[None for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for r in range(len(walking_squares)):
            for c in range(len(walking_squares[r])):
                if walking_squares[r][c]:
                    sq = WalkingSquare(frame)
                    self.squares[r][c] = sq
                else:
                    sq = Empty(frame)
                sq.grid(row=r, column=c, sticky="nesw")

        self.init_rooms(frame)

    def init_rooms(self, frame):
        study = Study(frame)
        study.grid(row=0, column=0)

        hall = Hall(frame)
        hall.grid(row=0, column=9)

        lounge = Lounge(frame)
        lounge.grid(row=0, column=17)

        library = Library(frame)
        library.grid(row=6, column=0)

        stairs = Stairs(frame)
        stairs.grid(row=8, column=9)

        dining_room = DiningRoom(frame)
        dining_room.grid(row=9, column=16)

        billiard_room = BilliardRoom(frame)
        billiard_room.grid(row=12, column=0)

        conservatory = Conservatory(frame)
        conservatory.grid(row=19, column=0)

        ball_room = BallRoom(frame)
        ball_room.grid(row=17, column=8)

        kitchen = Kitchen(frame)
        kitchen.grid(row=18, column=18)

walking_squares = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
