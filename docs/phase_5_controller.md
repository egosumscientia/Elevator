# Phase 5 — Controller

## Goal

Introduce an `ElevatorController` responsible for separating control and decision logic from the physical elevator model.

The existing `Elevator` class represents the elevator state and provides the operations that can physically change that state.

The controller will be responsible for deciding how those existing operations should be used in response to pending requests.

This phase introduces the controller layer, but it does **not** yet introduce the console interface or advanced elevator scheduling algorithms.

## Current System State

Before Phase 5, the system already supports:

- A `Building` with configurable lower and upper floor limits.
- Validation of floors through the building.
- An `Elevator` that starts at the lowest floor.
- Movement one floor up or down.
- Movement to a specific valid floor.
- Building boundary enforcement.
- Doors that start closed.
- Opening and closing doors.
- Rejection of repeated invalid door actions.
- Prevention of movement while the doors are open.
- External calls made from building floors.
- Internal destination selections.
- Validation of requested floors.
- Independent storage of external and internal requests.
- Duplicate requests prevented through set-based storage.
- Registration of requests without automatic elevator movement.

The request state currently exists in:

- `elevator.external_calls`
- `elevator.internal_calls`

Both are sets and therefore do not preserve request arrival order.

## Responsibility Separation

### Building

`Building` remains responsible for describing the valid floor range of the building.

It does not decide where the elevator should move.

### Elevator

`Elevator` remains responsible for its own physical state and primitive operations.

This includes:

- Current floor.
- Movement state.
- Door state.
- Moving up.
- Moving down.
- Moving to a valid floor.
- Opening doors.
- Closing doors.
- Storing external calls.
- Storing internal destination requests.

The elevator itself must not become responsible for choosing which pending request should be served next.

### ElevatorController

`ElevatorController` introduces the decision-making layer.

It operates on an existing `Elevator` instance and is responsible for coordinating elevator behavior based on the requests and state already represented by the elevator.

The controller must use the elevator's existing public operations rather than duplicating physical movement logic.

## Initial Scope

Phase 5 will introduce `ElevatorController` incrementally.

The controller must:

1. Be associated with an existing `Elevator`.
2. Be able to inspect the elevator's pending requests.
3. Contain the logic used to decide what request should be handled.
4. Coordinate the elevator through its existing movement operations.
5. Keep decision logic outside the `Elevator` class.

The exact request-selection policy must be defined before implementing scheduling behavior.

Existing Phase 1–4 behavior must remain unchanged unless a modification is strictly necessary for the controller.

## Design Decisions Not Yet Specified

The project plan does not currently define several controller behaviors.

These decisions must be made explicitly during Phase 5 rather than assumed.

### Request selection

When multiple requests exist, it is not yet defined which request should be handled first.

Possible policies could include:

- Nearest requested floor.
- Lowest requested floor.
- Highest requested floor.
- Request arrival order.
- Direction-aware scheduling.

No policy should be implemented until it is explicitly selected.

### External versus internal requests

External and internal requests are currently stored separately.

It is not yet defined whether:

- They have equal priority.
- Internal requests have priority.
- External requests have priority.
- They should be combined when making controller decisions.

### Request completion

It is not yet defined exactly when a request becomes completed and should be removed from pending request state.

### Automatic door operation

It is not yet defined whether arriving at a requested floor should automatically open the doors during this phase.

### Request ordering

The current request collections are sets.

Sets intentionally prevent duplicates but do not preserve arrival order.

Therefore, any scheduling policy requiring FIFO or request age would require an explicit change to request representation. Such a change must not be made implicitly.

## Work Order

Implement and review Phase 5 one part at a time.

1. Introduce the `ElevatorController` class and associate it with an existing elevator.
2. Verify that introducing the controller does not change existing elevator behavior.
3. Define the minimum information the controller needs from the elevator.
4. Explicitly choose the simple request-selection behavior required for this phase.
5. Implement that decision behavior.
6. Implement controller coordination with the elevator using existing elevator operations.
7. Define and implement when handled requests are removed.
8. Verify controller behavior with external requests.
9. Verify controller behavior with internal requests.
10. Verify behavior when both request types exist.
11. Verify that all Phase 1–4 behavior still works.

Each part must be reviewed before moving to the next.

The user writes the implementation.

The assistant provides complete manual test code when testing is required.

## Out of Scope

Do **not** implement in this phase unless explicitly added to the Phase 5 requirements:

- Console user interface.
- Multiple elevators.
- Advanced elevator scheduling algorithms.
- Persistent travel direction scheduling.
- Request prioritization based on complex policies.
- Timing or travel-time simulation.
- Asynchronous execution.
- Threads or concurrency.
- Graphical interface.
- Persistent storage.
- Database integration.
- Networking.
- APIs.
- IoT integration.
- PLC or physical motor control.

The console interface belongs to Phase 6.

Automated test infrastructure belongs to Phase 7 according to the current project plan, although manual tests may continue to be used during development.

## Constraints

Phase 5 must preserve all correct behavior from Phases 1–4.

Registering a request must remain separate from physically moving the elevator.

The `ElevatorController` must not duplicate movement validation already implemented by `Elevator`.

The controller should coordinate existing elevator behavior rather than directly manipulating physical elevator state when an existing elevator operation already represents that behavior.

No advanced scheduling behavior should be introduced without first defining it explicitly.

## Completion Criteria

Phase 5 will be complete when:

- `ElevatorController` exists as a separate class.
- It operates on an existing `Elevator`.
- Decision logic is separated from the elevator's physical operations.
- A clearly documented request-selection policy exists.
- The controller can use pending requests to determine elevator behavior according to that policy.
- Completed requests are handled according to an explicitly defined rule.
- External and internal requests interact according to an explicitly defined rule.
- Existing Phase 1–4 behavior remains correct.
- No Phase 6 console interface has been introduced.
- No unnecessary advanced scheduling behavior has been added.
