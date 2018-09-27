from single_square import SingleSquare


class WalkingSquare(SingleSquare):
    def __init__(self, parent):
        super(WalkingSquare, self).__init__(parent, "yellow")