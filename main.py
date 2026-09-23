from src.elevator.building import Building
from src.elevator.elevator import Elevator

building01 = Building(1, 3)
elevator01 = Elevator(building01)

print(elevator01.current_floor, elevator01.moving)  # 1 False

elevator01.move_up()
elevator01.move_up()
print(elevator01.current_floor, elevator01.moving)  # 3 False

elevator01.move_down()
print(elevator01.current_floor, elevator01.moving)  # 2 False

elevator01.move_down()
print(elevator01.current_floor, elevator01.moving)  # 1 False

elevator01.move_down()  # ValueError esperado: ya está en el piso mínimo