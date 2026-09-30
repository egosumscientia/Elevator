from src.elevator.building import Building
from src.elevator.elevator import Elevator


building = Building(lowest_floor=1, highest_floor=5)
elevator = Elevator(building)

initial_floor = elevator.current_floor

# Initial request state
assert elevator.external_calls == set()
assert elevator.internal_calls == set()

# External floor calls
elevator.external_call_to_floor(4)
elevator.external_call_to_floor(2)

assert elevator.external_calls == {2, 4}
assert elevator.current_floor == initial_floor

# Duplicate external call
elevator.external_call_to_floor(4)

assert elevator.external_calls == {2, 4}

# Invalid external calls
for invalid_floor in (0, 6):
    try:
        elevator.external_call_to_floor(invalid_floor)
        assert False, f"Expected ValueError for external floor {invalid_floor}"
    except ValueError:
        pass

assert elevator.external_calls == {2, 4}

# Internal destination requests
elevator.internal_call_to_floor(5)
elevator.internal_call_to_floor(3)

assert elevator.internal_calls == {3, 5}
assert elevator.current_floor == initial_floor

# Duplicate internal destination
elevator.internal_call_to_floor(5)

assert elevator.internal_calls == {3, 5}

# Invalid internal destinations
for invalid_floor in (0, 6):
    try:
        elevator.internal_call_to_floor(invalid_floor)
        assert False, f"Expected ValueError for internal floor {invalid_floor}"
    except ValueError:
        pass

assert elevator.internal_calls == {3, 5}

# Requests must remain independent
assert elevator.external_calls == {2, 4}
assert elevator.internal_calls == {3, 5}

# Registering requests must not affect physical elevator state
assert elevator.current_floor == initial_floor
assert elevator.moving is False
assert elevator.is_door_open is False

print("Phase 4 request tests passed.")