import single_square


class EmptySingleSquare(single_square.SingleSquare):
    def __init__(self, parent):
        super(EmptySingleSquare, self).__init__(parent, "white")
        print ("do empty square stuff in here")
