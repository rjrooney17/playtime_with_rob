from room import Room

class Lounge(Room):
    shape = (6, 7)

    def __init__(self, parent):
        super(Lounge, self).__init__(parent, Lounge.shape, "Lounge")