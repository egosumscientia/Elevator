# Phase 3 — Doors

## Goal

Add door opening and closing to `Elevator`, with rules that prevent movement while the doors are open.

## Scope

Work in `src/elevator/elevator.py`. Keep door behavior simple and synchronous: no timers, sensors, animations, or automatic door operation.

## Requirements

1. Add a door state to `Elevator`. The doors start closed.
2. Add `open_doors()`:
   - Open the doors when they are closed.
   - Reject the action with `ValueError` if they are already open.
3. Add `close_doors()`:
   - Close the doors when they are open.
   - Reject the action with `ValueError` if they are already closed.
4. Prevent `move_up()`, `move_down()`, and `move_to_floor(floor)` from moving while the doors are open. A rejected movement must not change the floor or door state.
5. Keep all Phase 2 floor limits and destination validation working.

## Work order

1. Add the initial door state.
2. Implement and review `open_doors()`.
3. Implement and review `close_doors()`.
4. Add the movement restriction.
5. Test valid door actions, repeated actions, movement with open doors, and normal movement with closed doors.

The user writes the implementation. Review one part at a time before moving to the next.

## Completion criteria

Doors start closed; opening and closing update their state correctly; invalid door actions raise `ValueError`; movement is blocked while doors are open; Phase 2 behavior still works when doors are closed.