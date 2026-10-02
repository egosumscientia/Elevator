# Phase 5 — Controller

## Goal

Introduce an `ElevatorController` responsible for separating control and decision logic from the physical elevator model.

The existing `Elevator` class represents the elevator state and provides the operations that can physically change that state.

The controller is responsible for deciding how those existing operations should be used in response to pending requests.

This phase introduces the controller layer, but it does **not** introduce the console interface or advanced elevator scheduling algorithms.

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

The request state exists in:

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

The elevator itself does not choose which pending request should be served next.

### ElevatorController

`ElevatorController` provides the decision-making layer.

It operates on an existing `Elevator` instance and coordinates elevator behavior based on the requests and state already represented by the elevator.

The controller uses the elevator's existing public operations rather than duplicating physical movement logic.

## Request Inspection

The controller can inspect:

- `elevator.external_calls`
- `elevator.internal_calls`

External and internal requests are combined temporarily when determining the next destination.

The original request sets remain separate and are not modified merely to perform request selection.

## Request Selection Policy

External and internal requests have equal priority when selecting the next destination.

The next request is selected according to the following policy:

1. Calculate the absolute distance between the elevator's current floor and every pending requested floor.
2. Select the requested floor with the shortest distance.
3. If two requested floors are equally distant from the current floor, select the higher floor.
4. Request arrival order is not considered.

Because arrival order is not required, the existing set-based request representation remains unchanged.

If there are no pending requests, no destination is selected.

## Controller Movement

When a pending destination exists, the controller coordinates movement by calling the elevator's existing `move_to_floor()` operation.

The controller does not directly manipulate `current_floor` or reproduce the movement logic already implemented by `Elevator`.

If there are no pending requests, requesting controller movement produces no movement.

## Request Completion

A request is considered completed when the elevator reaches the requested floor.

After successful arrival:

- The destination is removed from `external_calls` if present.
- The destination is removed from `internal_calls` if present.
- If the same floor was requested both externally and internally, both requests are considered completed.

Requests are removed only after successful arrival.

## Automatic Door Operation

Door operation is coordinated automatically by the controller.

Before moving toward a pending destination:

- If the doors are already closed, no door action is required.
- If the doors are open, the controller closes them before movement.

After reaching the requested floor:

- The controller automatically opens the doors.

Therefore, consecutive controller operations follow this behavior:

1. Select the next destination.
2. Close the doors if necessary.
3. Move to the selected floor.
4. Open the doors.
5. Remove the completed request from pending request state.

A request for the elevator's current floor is also considered valid. In that case, no physical floor movement is required, the doors are opened, and the request is completed.

## Verified Behavior

Manual verification during Phase 5 confirmed:

- The controller can inspect external and internal requests.
- The nearest requested floor is selected.
- Equal-distance requests select the higher floor.
- External and internal requests participate equally in destination selection.
- A destination requested by both request types is removed from both sets after service.
- External-only requests are handled correctly.
- Internal-only requests are handled correctly.
- Multiple requests can be handled consecutively.
- No pending requests result in no movement.
- Requests are not removed when movement fails.
- Doors open automatically after arrival.
- Open doors are automatically closed before serving the next destination.
- Requests for the current floor are handled correctly.
- Existing Phase 1–4 behavior remains unchanged.

## Out of Scope

Do **not** implement in this phase:

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

Automated test infrastructure belongs to Phase 7. Manual tests are used during the current development phases.

## Constraints

Phase 5 preserves all correct behavior from Phases 1–4.

Registering a request remains separate from physically moving the elevator.

`ElevatorController` does not duplicate movement validation already implemented by `Elevator`.

The controller coordinates existing elevator behavior rather than directly manipulating physical elevator state when an existing elevator operation represents that behavior.

No advanced scheduling behavior is introduced.

## Completion Criteria

Phase 5 is complete when:

- `ElevatorController` exists as a separate class.
- It operates on an existing `Elevator`.
- Decision logic is separated from the elevator's physical operations.
- The nearest-request selection policy is implemented.
- Equal-distance requests prioritize the higher floor.
- External and internal requests have equal selection priority.
- The controller coordinates movement through existing elevator operations.
- Completed requests are removed after arrival.
- Requests present in both request sets are removed from both.
- Doors close automatically before subsequent movement when necessary.
- Doors open automatically after arrival.
- Existing Phase 1–4 behavior remains correct.
- No Phase 6 console interface has been introduced.
- No unnecessary advanced scheduling behavior has been added.