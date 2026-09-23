# Phase 2 — Manual Movement

## Objective

Add manual movement capabilities to the elevator while always respecting the floor limits defined by `Building`.

Doors, user requests, queues, and automatic control logic are not part of this phase.

---

## Main File

`src/elevator/elevator.py`

The existing `Elevator` class will be extended with movement methods.

---

## Current State

The `Elevator` class already has:

- A reference to a `Building` object.
- A `current_floor` attribute.
- A `moving` attribute.
- The elevator starts at `building.lowest_floor`.
- The elevator starts stopped.

---

## 1. `move_up()` Method

Move the elevator exactly one floor upward.

### Rules

- Increase `current_floor` by one.
- Never move above `building.highest_floor`.
- If the elevator is already at the highest floor, the movement must be rejected.
- `moving` must represent whether the elevator is currently moving.
- After the movement finishes, `moving` must indicate that the elevator is stopped.

---

## 2. `move_down()` Method

Move the elevator exactly one floor downward.

### Rules

- Decrease `current_floor` by one.
- Never move below `building.lowest_floor`.
- If the elevator is already at the lowest floor, the movement must be rejected.
- `moving` must represent whether the elevator is currently moving.
- After the movement finishes, `moving` must indicate that the elevator is stopped.

---

## 3. `move_to_floor(floor)` Method

Move the elevator from its current floor to a destination floor.

### Rules

- Receive the destination floor as an argument.
- Validate that the destination floor belongs to the building.
- Reuse the validation logic already implemented in `Building`.
- If the destination is above the current floor, move upward one floor at a time.
- If the destination is below the current floor, move downward one floor at a time.
- If the elevator is already at the requested floor, no movement is required.
- The elevator must never leave the valid floor range.
- When movement finishes, `current_floor` must equal the destination floor.
- When movement finishes, the elevator must be stopped.

---

## Implementation Order

The phase will be implemented and reviewed step by step:

1. Implement `move_up()`.
2. Test `move_up()`.
3. Implement `move_down()`.
4. Test `move_down()`.
5. Implement `move_to_floor(floor)`.
6. Test complete movement between different floors.
7. Test boundary cases and invalid destinations.

Do not move to the next method until the current one is approved.

---

## Expected Manual Tests

At minimum, verify that:

- The elevator starts on floor 1.
- It can move from floor 1 to floor 2.
- It can continue moving upward to the highest floor.
- It cannot move above the highest floor.
- It can move downward one floor.
- It can continue moving downward to the lowest floor.
- It cannot move below the lowest floor.
- It can move to a valid higher destination floor.
- It can move to a valid lower destination floor.
- It can receive its current floor as the destination.
- It rejects a floor that does not belong to the building.
- `current_floor` contains the correct value after each movement.
- `moving` indicates that the elevator is stopped after movement finishes.

---

## Out of Scope for This Phase

Do NOT implement yet:

- Doors.
- Door sensors.
- Internal buttons.
- Floor calls.
- Request queues.
- Automatic direction logic.
- `ElevatorController`.
- Timers.
- Graphical interface.
- Physical travel-time simulation.

---

## Phase 2 Completion Criteria

Phase 2 is complete when the elevator can move manually upward, downward, and to any valid floor without ever leaving the limits defined by `Building`.