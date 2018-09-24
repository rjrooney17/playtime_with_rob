
class Player(object):
    PLAYER_CONFIGURATIONS = {
        "Miss Scarlet": { "initial_position": (0, 16), "color": "red" },
        "Professor Plum": { "initial_position": (5, 0), "color": "purple" },
        "Mrs. Peacock": { "initial_position": (18, 0), "color": "orange" },
        "Mr. Green": { "initial_position": (24, 9), "color": "green" },
        "Colonel Mustard":{ "initial_position": (7, 23), "color": "yellow" },
        "Mrs. White": { "initial_position": (24, 14), "color": "white" }
    }

    def __init__(self, name, parent):
        assert name in Player.PLAYER_CONFIGURATIONS
        self.parent = parent
        self.name = name
        config = Player.PLAYER_CONFIGURATIONS[name]
        self.position = config["initial_position"]
        self.color = config["color"]