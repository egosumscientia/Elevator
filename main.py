from src.elevator.building import Building
from src.elevator.elevator import Elevator
from src.elevator.controller import ElevatorController

building = Building(1,5)
elevator = Elevator(building)
controller = ElevatorController(elevator)

def show_menu():
    print("GENERAL CONTROL PANEL")
    print(" 1. View elevator state")
    print(" 2. Register external call")
    print(" 3. Register internal destination")
    print(" 4. Handle next request")
    print(" 5. Exit")


def execute_program():
    while True:
        show_menu()
        option = input("Select an option (1-5): ").strip()

        match option:
            case "1":
                print("\nView elevator state...")
                print("\n Current floor: " + str(elevator.current_floor))
                print("Open" if elevator.is_door_open else "Closed")
                print("\n Pending external calls: ")
                print(elevator.external_calls)
                print("\n Pending internal requests")
                print(elevator.internal_calls)
            case "2":
                print("\nRegister external call...")
                try:
                    input_floor = input("Select the destiny floor").strip()
                    input_floor = int(input_floor)
                    elevator.external_call_to_floor(input_floor)
                    print(f"Call successfully registered for floor {input_floor}!")
                except ValueError as error:
                    print(error)
            case "3":
                print("\nRegister internal destination...")
                try:
                    destiny_floor = input("Select the destiny floor")
                    destiny_floor = int(destiny_floor)
                    elevator.internal_call_to_floor(destiny_floor)
                    print(f"Call successfully registered for floor {destiny_floor}!")
                except ValueError as error:
                    print(error)
            case "4":
                print("\nHandle next request...")
                controller.start_movement()
            case "5":
                print("\nEXIT...")
                break
            case _:
                print("\n❌ Error: Invalid option. Please type a number between 1 and 5.")


if __name__ == "__main__":
    execute_program()
