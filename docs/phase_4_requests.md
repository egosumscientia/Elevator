# Phase 4 --- Requests

## Goal

Add request handling to the elevator system so that it can represent:

-   Calls made from building floors.
-   Destination selections made from inside the elevator.

This phase introduces requests as data and validates them, but it does
**not** yet implement automatic scheduling, request queues, or
controller decision logic.

## Scope

Work primarily with the existing `Building` and `Elevator` model.

The elevator must be able to receive valid floor requests while
preserving all behavior completed in Phases 1--3.

Do not implement `ElevatorController` yet.

## Requirements

### 1. External floor calls

Add a way to represent a request made from a floor of the building.

Examples:

-   A person on floor 1 calls the elevator.
-   A person on floor 4 calls the elevator.

Rules:

-   The requested floor must exist in the building.
-   Invalid floors must be rejected with `ValueError`.
-   Creating or registering a request must not immediately move the
    elevator.
-   A floor call represents a request only; movement will be handled
    later.

### 2. Internal destination requests

Add a way to represent a destination selected from inside the elevator.

Examples:

-   The elevator is on floor 1 and the passenger selects floor 5.
-   The elevator is on floor 4 and the passenger selects floor 2.

Rules:

-   The destination must exist in the building.
-   Invalid destinations must be rejected with `ValueError`.
-   Registering a destination must not immediately move the elevator.
-   The request must remain separate from the physical movement methods
    already implemented.

### 3. Request state

The system must have a clear way to store the requests that have been
received.

At this stage, keep the model simple.

The stored state must allow later phases to determine which floors have
been requested.

Do not implement advanced ordering or scheduling logic yet.

### 4. Preserve previous behavior

All behavior from previous phases must continue working:

-   The elevator starts at the lowest floor.
-   `move_up()` and `move_down()` respect building limits.
-   `move_to_floor(floor)` validates destinations.
-   Doors start closed.
-   Doors can be opened and closed.
-   Repeated invalid door actions raise `ValueError`.
-   The elevator cannot move while the doors are open.

## Work Order

Implement and review the phase one part at a time:

1.  Decide how requests will be represented and stored.
2.  Implement external floor calls.
3.  Test valid and invalid external calls.
4.  Implement internal destination requests.
5.  Test valid and invalid internal destinations.
6.  Verify that registering requests does not move the elevator.
7.  Verify that all Phase 1--3 behavior still works.

The user writes the implementation. Review one part at a time before
moving to the next.

The assistant provides the manual test code.

## Out of Scope

Do **not** implement yet:

-   Automatic movement in response to requests.
-   Request prioritization.
-   Request ordering algorithms.
-   Direction-based scheduling.
-   Automatic door operation.
-   `ElevatorController`.
-   Multiple elevators.
-   Timers or travel-time simulation.
-   Graphical interface.
-   Persistent storage.
-   Networking or APIs.

These responsibilities belong to later phases.

## Completion Criteria

Phase 4 is complete when:

-   Valid external floor calls can be registered.
-   Invalid external floor calls are rejected.
-   Valid internal destination requests can be registered.
-   Invalid internal destinations are rejected.
-   Requests can be inspected after they are registered.
-   Registering a request does not automatically move the elevator.
-   Existing movement and door behavior remains correct.
-   No controller or automatic scheduling logic has been introduced.
