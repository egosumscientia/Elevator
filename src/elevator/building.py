class Building:
    def __init__(self, lowest_floor: int, highest_floor: int):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor

        if self.highest_floor < self.lowest_floor:
            raise ValueError(
                "Highest floor must be greater than or equal to lowest floor.")

    def is_valid_floor(self, floor: int) -> bool:
        return self.lowest_floor <= floor <= self.highest_floor






