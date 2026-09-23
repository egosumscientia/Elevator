class Elevator:
    def __init__(self, building):
        self.building = building
        self.current_floor = building.lowest_floor
        self.moving = False

    def move_up(self):
        if self.current_floor == self.building.highest_floor:
            raise ValueError("The elevator is already at the highest available floor.")
        else:
            self.moving = True
            self.current_floor += 1
            self.moving = False

    def move_down(self):
        if self.current_floor == self.building.lowest_floor:
            raise ValueError("The elevator is already at the lowest available floor.")
        else:
            self.moving = True
            self.current_floor -= 1
            self.moving = False