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

    def move_to_floor(self, floor):
        if not self.building.is_valid_floor(floor):
            raise ValueError("The destination floor does not exist in the building.")
        elif self.current_floor == floor:
            return
        while self.current_floor < floor:
            self.move_up()
        while self.current_floor > floor:
            self.move_down()

