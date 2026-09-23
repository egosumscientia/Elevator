from src.elevator.building import Building
from src.elevator.elevator import Elevator

building = Building(1, 5)
elevator = Elevator(building)

print("Start:", elevator.current_floor, elevator.moving)

elevator.move_to_floor(4)
print("Move up to 4:", elevator.current_floor, elevator.moving)

elevator.move_to_floor(2)
print("Move down to 2:", elevator.current_floor, elevator.moving)

elevator.move_to_floor(2)
print("Stay on 2:", elevator.current_floor, elevator.moving)

try:
    elevator.move_to_floor(6)
except ValueError as error:
    print("Invalid destination:", error)

print("After invalid destination:", elevator.current_floor, elevator.moving)