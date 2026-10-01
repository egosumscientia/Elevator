class ElevatorController:
    def __init__(self, elevator):
        self.elevator = elevator

    def return_external_calls(self):
        return self.elevator.external_calls

    def return_internal_calls(self):
        return self.elevator.internal_calls

    def get_nearest_destination_floor(self):
        new_set = self.elevator.external_calls | self.elevator.internal_calls
        current_floor = self.elevator.current_floor

        minor_distance = float('inf')
        selected_floor_so_far = None

        for floor in new_set:
            distance = abs(floor - current_floor)
            if distance < minor_distance:
                minor_distance = distance
                selected_floor_so_far = floor
            elif distance == minor_distance and floor > selected_floor_so_far:
               selected_floor_so_far = floor

        return selected_floor_so_far