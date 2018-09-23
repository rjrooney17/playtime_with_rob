from room import Room

class BilliardRoom(Room):
    shape = (5, 6)
    def __init__(self, parent):
        super(BilliardRoom, self).__init__(parent, BilliardRoom.shape, "BilliardRoom")