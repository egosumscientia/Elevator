from src.elevator.building import Building
from src.elevator.elevator import Elevator
from src.elevator.controller import ElevatorController


building = Building(1, 5)
elevator = Elevator(building)
controller = ElevatorController(elevator)

# Elevator starts at floor 1
elevator.external_call_to_floor(5)
elevator.internal_call_to_floor(3)

print(controller.get_nearest_destination_floor())
# Expected: 3

# Move elevator manually to floor 3
elevator.move_to_floor(3)

# Test tie: floors 2 and 4 are both 1 floor away
elevator.external_calls.clear()
elevator.internal_calls.clear()

elevator.external_call_to_floor(2)
elevator.internal_call_to_floor(4)

print(controller.get_nearest_destination_floor())
# Expected: 4 (upper floor wins the tie)

# Test no pending requests
elevator.external_calls.clear()
elevator.internal_calls.clear()

print(controller.get_nearest_destination_floor())
# Expected: None