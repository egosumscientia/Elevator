class Elevator:
    def __init__(self, building):
        self.building = building
        self.current_floor = building.lowest_floor
        self.moving = False

