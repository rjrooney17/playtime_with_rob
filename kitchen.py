from room import Room

class Kitchen(Room):
    shape = (6, 6)
    def __init__(self, parent):
        super(Kitchen, self).__init__(parent, Kitchen.shape, "Kitchen")