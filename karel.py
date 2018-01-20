class Karel(object):
    _directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    _facing_dict = {'E': 3, 'S': 2, 'W': 1, 'N': 0}

    def __init__(self, parent=None, avenues=1, streets=1,
                 facing='E', num_of_beeper=0):
        self.parent = parent
        self._beeper_bag = num_of_beeper
        self._x = avenues
        self._y = streets
        self._facing = self._facing_dict[facing.upper()]

    # status
    def get_position(self):
        return self._x, self._y

    def _set_position(self, x, y):
        self._x = x
        self._y = y

    def _get_facing(self):
        return self._facing

    def _get_facing_key(self):
        for key in self._facing_dict.keys():
            if self._facing_dict[key] == self._facing:
                return key

    # actions
    def move(self):
        if self.front_is_clear():
            x, y = self._directions[self._facing]
            self._x += x
            self._y += y
        else:
            # raise move exception
            pass

    def turn_left(self):
        self._facing += 1
        self._facing %= 4

    def pick_beeper(self):
        if self.next_to_a_beeper():
            self.parent.remove_beeper(self._x, self._y)
            self._beeper_bag += 1
        else:
            # raise pick beeper exception
            pass

    def put_beeper(self):
        if self.any_beepers_in_beeper_bag():
            self._beeper_bag -= 1
            self.parent.add_beeper(self._x, self._y)
        else:
            # raise put beeper exception
            pass

    def turn_off(self):
        # print end successfully
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
        if self.direction is Direction.East:
            return True
        else:
            return False

    def not_facing_east(self):
        pass

    def facing_west(self):
        pass

    def not_facing_west(self):
        pass
