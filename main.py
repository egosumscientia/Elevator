from src.elevator.building import Building
from src.elevator.elevator import Elevator
from src.elevator.controller import ElevatorController

building = Building(1, 5)
elevator = Elevator(building)
controller = ElevatorController(elevator)

print("=== INITIAL STATE ===")
print(elevator.current_floor)       # Expected: 1
print(elevator.moving)             # Expected: False
print(elevator.is_door_open)       # Expected: False

print("\n=== MOVEMENT ===")
elevator.move_up()
print(elevator.current_floor)       # Expected: 2

elevator.move_down()
print(elevator.current_floor)       # Expected: 1

elevator.move_to_floor(5)
print(elevator.current_floor)       # Expected: 5

print("\n=== BUILDING LIMITS ===")
try:
    elevator.move_up()
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

elevator.move_to_floor(1)

try:
    elevator.move_down()
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

print("\n=== DOORS ===")
elevator.open_doors()
print(elevator.is_door_open)        # Expected: True

try:
    elevator.open_doors()
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

try:
    elevator.move_up()
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

elevator.close_doors()
print(elevator.is_door_open)        # Expected: False

try:
    elevator.close_doors()
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

print("\n=== REQUESTS ===")
elevator.external_call_to_floor(4)
elevator.internal_call_to_floor(3)

print(elevator.external_calls)      # Expected: {4}
print(elevator.internal_calls)      # Expected: {3}
print(elevator.current_floor)       # Expected: 1

print("\n=== INVALID REQUESTS ===")
try:
    elevator.external_call_to_floor(6)
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

try:
    elevator.internal_call_to_floor(0)
except ValueError as error:
    print(type(error).__name__)      # Expected: ValueError

print("\n=== CONTROLLER DID NOT ALTER REQUEST REGISTRATION ===")
print(elevator.external_calls)      # Expected: {4}
print(elevator.internal_calls)      # Expected: {3}
print(elevator.current_floor)       # Expected: 1