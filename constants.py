from enum import Enum, auto


class Position:
    def __init__(self, street, avenue):
        self.street = street
        self.avenue = avenue
    
    def __repr__(self):
        return str((self.street, self.avenue))


class Direction(Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()
