from constants import Position, Direction


class Karel:
    def __init__(self, position, direction, num_of_beeper):
        self.position = position
        self.direction = direction
        self.beepers = num_of_beeper
        self.active = True

    # actions
    def move(self):
        if self.front_is_clear():
            if self.direction is Direction.East:
                self.position.street -= 1
            elif self.direction is Direction.North:
                self.position.avenue += 1
            elif self.direction is Direction.South:
                self.position.avenue -= 1
            else:
                self.position.street += 1
        pass

    def turn_left(self):
        pass

    def pick_beeper(self):
        pass

    def put_beeper(self):
        pass

    def turn_off(self):
        self.active = False

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

    def __repr__(self):
        return str(self.__dict__)
