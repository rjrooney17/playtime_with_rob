from room import Room

class Stairs(Room):
    shape = (7, 5)
    def __init__(self, parent):
        super(Stairs, self).__init__(parent, Stairs.shape, "Stairs")