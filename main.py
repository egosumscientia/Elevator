
from src.elevator.building import Building
from src.elevator.elevator import Elevator


building01 = Building(1,5)
print(building01.is_valid_floor(4))

elevator01 = Elevator(building01)
print(elevator01.moving)
print(elevator01.current_floor)