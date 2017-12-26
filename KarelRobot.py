from enum import Enum
import pickle


class Direction(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


class World:
    def __init__(self, world_pickle=None, num_streets=10, num_avenues=10):
        if world_pickle is not None :
            with open(world_pickle,'rb') as f:
                world_info = pickle.load(f)
            for key in world_info:
                setattr(self,key,world_info[key])            
        else:
            self.num_streets = num_streets
            self.num_avenues = num_avenues
            self.beepers = {}
            self.karel = None
            self.walls = []

    def add_beeper(self, street, avenue, num_of_beeper):
        self.beepers[(street, avenue)] = num_of_beeper
        
    def add_karel(self, street=1, avenue=1, direction=2, num_of_beeper=0):
            self.karel = Karel((street,avenue), direction, num_of_beeper)

    def add_wall(self, street, avenue, direction):
        self.walls.append(((street, avenue), direction))

    def export_world(self, export_pickle):
        with open(export_pickle, 'wb') as f:
            pickle.dump(self.__dict__, f)
        
    def __repr__(self):    
        return str(self.__dict__)


class Karel:
    def __init__(self, position, direction, num_of_beeper):
        self.position = position
        self.direction = direction
        self.beepers = num_of_beeper
        self.active = True

    # actions
    def move(self):
        pass

    def turn_left(self):
        pass

    def pick_beeper(self):
        pass

    def put_beeper(self):
        pass

    def turn_off(self):
        pass

    # conditions(clear or block)
    def front_is_clear(self):
        pass

    def front_is_blocked(self):
        pass

    def left_is_clear(self):
        pass

    def left_is_blocked(self):
        pass

    def right_is_clear(self):
        pass

    def right_is_blocked(self):
        pass

    def back_is_clear(self):
        pass

    def back_is_blocked(self):
        pass

    # conditions(beepers)
    def next_to_a_beeper(self):
        pass

    def not_next_to_a_beeper(self):
        pass

    def any_beepers_in_beeper_bag(self):
        pass

    def no_beepers_in_beeper_bag(self):
        pass

    # conditions(facing or not)
    def facing_north(self):
        pass

    def not_facing_north(self):
        pass

    def facing_south(self):
        pass

    def not_facing_south(self):
        pass

    def facing_east(self):
        pass

    def not_facing_east(self):
        pass

    def facing_west(self):
        pass

    def not_facing_west(self):
        pass

    def __repr__(self):
        return str(self.__dict__)


class MoveException(Exception):
    pass


class BeeperException(Exception):
    pass


class TurnOffException(Exception):
    pass
