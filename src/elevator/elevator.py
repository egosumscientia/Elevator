class Elevator:
    def __init__(self, building):
        self.building = building
        self.current_floor = building.lowest_floor
        self.is_door_open = False
        self.moving = False
        self.internal_calls = set()
        self.external_calls = set()

    def move_up(self):
        if self.current_floor == self.building.highest_floor:
            raise ValueError("The elevator is already at the highest available floor.")
        elif self.is_door_open:
            raise ValueError("The door is open, the Elevator can't move")
        else:
            self.moving = True
            self.current_floor += 1
            self.moving = False

    def move_down(self):
        if self.current_floor == self.building.lowest_floor:
            raise ValueError("The elevator is already at the lowest available floor.")
        elif self.is_door_open:
            raise ValueError("The door is open, the Elevator can't move")
        else:
            self.moving = True
            self.current_floor -= 1
            self.moving = False

    def move_to_floor(self, floor):
        if not self.building.is_valid_floor(floor):
            raise ValueError("The destination floor does not exist in the building.")
        elif self.is_door_open:
            raise ValueError("The door is open, the Elevator can't move")
        elif self.current_floor == floor:
            return

        while self.current_floor < floor:
            self.move_up()
        while self.current_floor > floor:
            self.move_down()

    def open_doors(self):
        if not self.is_door_open:
            self.is_door_open = True
        else:
            raise ValueError("The door is already open.")

    def close_doors(self):
        if self.is_door_open:
            self.is_door_open = False
        else:
            raise ValueError("The door is already closed")

    def external_call_to_floor(self, destination_floor):
        if not self.building.is_valid_floor(destination_floor):
            raise ValueError("The destination floor does not exist in the building.")
        else:
            self.external_calls.add(destination_floor)

    def internal_call_to_floor(self, destination_floor):
        if not self.building.is_valid_floor(destination_floor):
            raise ValueError("The destination floor does not exist in the building.")
        else:
            self.internal_calls.add(destination_floor)