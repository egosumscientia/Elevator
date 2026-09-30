from src.elevator.building import Building
from src.elevator.elevator import Elevator

building = Building(1, 5)
elevator = Elevator(building)

# Door starts closed
print("Initial door state:", elevator.is_door_open)

# Open doors
elevator.open_doors()
print("After opening:", elevator.is_door_open)

# Try opening again
try:
    elevator.open_doors()
except ValueError as error:
    print("Open again:", error)

# Close doors
elevator.close_doors()
print("After closing:", elevator.is_door_open)

# Try closing again
try:
    elevator.close_doors()
except ValueError as error:
    print("Close again:", error)

# Block move_up with open doors
elevator.open_doors()

print("Floor before blocked movement:", elevator.current_floor)

try:
    elevator.move_up()
except ValueError as error:
    print("Blocked move_up:", error)

print("Floor after blocked move_up:", elevator.current_floor)
print("Door still open:", elevator.is_door_open)

# Block move_to_floor with open doors
try:
    elevator.move_to_floor(4)
except ValueError as error:
    print("Blocked move_to_floor:", error)

print("Floor after blocked move_to_floor:", elevator.current_floor)
print("Door still open:", elevator.is_door_open)

# Close doors and verify normal movement
elevator.close_doors()
elevator.move_to_floor(3)

print("Moved normally to:", elevator.current_floor)

# Block move_down with open doors
elevator.open_doors()

try:
    elevator.move_down()
except ValueError as error:
    print("Blocked move_down:", error)

print("Floor after blocked move_down:", elevator.current_floor)
print("Door still open:", elevator.is_door_open)

# Close doors and move normally
elevator.close_doors()
elevator.move_down()

print("Floor after valid move_down:", elevator.current_floor)
print("Door closed:", elevator.is_door_open)