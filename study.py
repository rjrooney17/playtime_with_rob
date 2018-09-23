
from room import Room

class Study(Room):
    shape = (4, 7)
    def __init__(self, parent):
        super(Study, self).__init__(parent, Study.shape, "Study")