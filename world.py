from karel import Karel
from constants import Position, Direction
import pickle


class World:
    def __init__(self, world_pickle=None, num_streets=10, num_avenues=10):
        if world_pickle is not None:
            with open(world_pickle, 'rb') as f:
                world_info = pickle.load(f)
            for key in world_info:
                setattr(self, key, world_info[key])
        else:
            self.num_streets = num_streets
            self.num_avenues = num_avenues
            self.beepers = {}
            self.karel = None
            self.walls = []

    def add_beeper(self, street, avenue, num_of_beeper):
        self.beepers[(street, avenue)] = num_of_beeper
        
    def add_karel(self, street=1, avenue=1, direction=Direction.West, num_of_beeper=0):
            self.karel = Karel(Position(street,avenue), direction, num_of_beeper)

    def add_wall(self, street, avenue, direction):
        self.walls.append(((street, avenue), direction))

    def export_world(self, export_pickle):
        with open(export_pickle, 'wb') as f:
            pickle.dump(self.__dict__, f)
        
    def __repr__(self):    
        return str(self.__dict__)
