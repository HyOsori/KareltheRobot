import karel


class World:
    walls_list = []
    boundaries = []
    beepers_dict = {}

    def __init__(self, avenues=10, streets=10, walls=[], beepers={}, robot=None):
        self.avenues = avenues
        self.streets = streets
        self.robot = robot
        self.num_cols = 2 * avenues + 1
        self.num_rows = 2 * streets + 1
        World.walls_list = walls
        for (col, row) in World.walls_list:
            if not (col + row) % 2:
                # wall is on wrong position
                pass
        World.beepers_dict = beepers
        self.set_boundaries()

    def set_boundaries(self):
        for col in range(1, self.num_cols - 1, 2):
            if (col, 0) not in World.boundaries:
                World.boundaries.append((col, 0))
            if (col, self.num_rows) not in World.boundaries:
                World.boundaries.append((col, self.num_rows - 1))
        for row in range(1, self.num_rows - 1, 2):
            if (0, row) not in World.boundaries:
                World.boundaries.append((0, row))
            if (self.num_cols, row) not in World.boundaries:
                World.boundaries.append((self.num_cols - 1, row))

    def reset_world(self, avenues=10, streets=10):
        self.avenues = avenues
        self.streets = streets
        self.num_cols = 2 * avenues + 1
        self.num_rows = 2 * streets + 1
        World.boundaries = []
        World.walls_list = []
        World.beepers_dict = {}
        self.set_boundaries()

    def toggle_walls(self, col, row):
        if (col + row) % 2:
            if (col, row) in World.walls_list:
                World.walls_list.remove((col, row))
            else:
                World.walls_list.append((col, row))
        else:
            # wall is on wrong position
            pass

    def set_beepers(self, avenue, street, num_of_beeper):
        if (avenue, street) in World.beepers_dict:
            if num_of_beeper == 0:
                del World.beepers_dict[(avenue, street)]
            else:
                World.beepers_dict[(avenue, street)] = num_of_beeper
        elif num_of_beeper > 0:
            World.beepers_dict[(avenue, street)] = num_of_beeper
        else:
            # wrong number of beeper
            pass

    def is_clear(self, col, row):
        if (col, row) in World.walls_list:
            return False
        if (col, row) in World.boundaries:
            return False
        else:
            return True

    def add_beeper(self, avenue, street):
        if (avenue, street) in World.beepers_dict:
            World.beepers_dict[(avenue, street)] += 1
        else:
            World.beepers_dict[(avenue, street)] = 1

    def remove_beeper(self, avenue, street):
        if (avenue, street) in World.beepers_dict:
            World.beepers_dict[(avenue, street)] -= 1
            if World.beepers_dict[(avenue, street)] == 0:
                del World.beepers_dict[(avenue, street)]
        else:
            # remove beeper not exist
            pass

    def add_robot(self, avenue=1, street=1, facing_key='E', beepers=0):
        self.robot = karel.Karel(avenue, street, facing_key, beepers)
        return self.robot
