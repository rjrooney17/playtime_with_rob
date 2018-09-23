
from room import Room

class Hall(Room):
    shape = (7, 6)

    def __init__(self, parent):
        super(Hall, self).__init__(parent, Hall.shape, "Hall")