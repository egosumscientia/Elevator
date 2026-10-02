# Phase 6 --- Console Simulation

## Goal

Introduce a simple console interface that allows a user to operate the
elevator system interactively.

The console layer must use the existing `Building`, `Elevator`, and
`ElevatorController` behavior rather than duplicating their
responsibilities.

Phase 6 adds interaction only. It must preserve all correct behavior
from Phases 1--5.

## Current System State

Before Phase 6, the system already supports:

-   A configurable `Building`.
-   Floor validation.
-   An `Elevator` with physical state and movement operations.
-   Door opening and closing.
-   External floor calls.
-   Internal destination requests.
-   Separate storage of external and internal requests.
-   An `ElevatorController` responsible for request selection and
    coordination.
-   Selection of the nearest requested floor.
-   Higher-floor priority when two requests are equally distant.
-   Equal priority between external and internal requests.
-   Automatic closing of open doors before movement.
-   Automatic opening of doors after arrival.
-   Removal of completed requests after successful service.

## Responsibility Separation

### Building

`Building` continues to define the valid floor range.

### Elevator

`Elevator` continues to represent physical elevator state and primitive
operations.

### ElevatorController

`ElevatorController` continues to make decisions and coordinate elevator
behavior.

### Console Interface

The console interface is responsible only for interaction with the user.

It may:

-   Display the current elevator state.
-   Display pending requests.
-   Accept user commands or menu selections.
-   Register external calls through the existing elevator operation.
-   Register internal destination requests through the existing elevator
    operation.
-   Ask the controller to serve the next pending request.
-   Display validation errors and operation results.

It must not duplicate floor validation, movement logic,
request-selection logic, or controller behavior.

## Initial Scope

The console simulation must provide a simple way to:

1.  View the elevator's current floor.
2.  View whether the doors are open or closed.
3.  View pending external requests.
4.  View pending internal requests.
5.  Register an external floor call.
6.  Register an internal destination request.
7.  Ask the controller to handle the next pending request.
8.  Exit the simulation.

## Input Handling

Console input must be converted and validated before being passed to the
existing model operations when necessary.

Invalid user input must not terminate the program unexpectedly.

Domain validation already implemented by `Building` or `Elevator` must
not be duplicated unnecessarily in the console layer.

Errors raised by existing operations should be presented to the user in
a readable form.

## Controller Interaction

The console must not decide which requested floor should be served next.

When the user asks the system to process the next request, the console
delegates that responsibility to `ElevatorController`.

The request-selection policy defined in Phase 5 remains unchanged.

## Request Registration

Registering an external or internal request through the console must
remain separate from serving that request.

Adding a request must not automatically move the elevator.

Movement occurs only when the controller is explicitly asked to handle a
pending request.

## Console Loop

The simulation should continue accepting user actions until the user
explicitly chooses to exit.

After an operation, the user must be able to continue interacting with
the same `Building`, `Elevator`, and `ElevatorController` instances so
that system state is preserved during the session.

## Design Decisions Not Yet Specified

The exact presentation of the console interface is not yet fixed.

Before implementation, explicitly decide:

-   Whether to use a numbered menu, textual commands, or another simple
    input format.
-   The exact command/menu names shown to the user.
-   How much elevator state is displayed after each action.
-   Whether state is displayed automatically after every operation or
    only when requested.

These presentation decisions must be made before implementing the
corresponding interface behavior.

## Work Order

Implement and review Phase 6 one part at a time.

1.  Define the console interaction format.
2.  Create the console entry point without changing existing domain
    classes.
3.  Display the available user actions.
4.  Implement viewing elevator state.
5.  Implement external request registration through the existing
    elevator operation.
6.  Implement internal request registration through the existing
    elevator operation.
7.  Implement controller execution for the next pending request.
8.  Handle invalid console input without terminating the simulation
    unexpectedly.
9.  Implement explicit exit behavior.
10. Verify that multiple operations preserve state during one console
    session.
11. Verify that all Phase 1--5 behavior remains correct.

Each part must be reviewed before moving to the next.

The user writes the implementation.

The assistant provides complete manual test code when testing is
required.

## Out of Scope

Do **not** implement in this phase unless explicitly added to the
requirements:

-   Graphical interface.
-   Web interface.
-   Multiple elevators.
-   Advanced scheduling algorithms.
-   Persistent storage.
-   Database integration.
-   Networking.
-   APIs.
-   Asynchronous execution.
-   Threads or concurrency.
-   Timing or travel-time simulation.
-   IoT integration.
-   PLC or physical motor control.
-   Automated test infrastructure.

Automated test infrastructure belongs to Phase 7.

## Constraints

-   Preserve all correct behavior from Phases 1--5.
-   Keep console interaction separate from domain and controller logic.
-   Do not move request-selection logic into the console.
-   Do not duplicate existing elevator validation or movement logic.
-   Registering requests must remain separate from serving requests.
-   Do not introduce advanced scheduling behavior.
-   Keep the console implementation simple and focused on operating the
    existing system.

## Completion Criteria

Phase 6 will be complete when:

-   A console interface exists.
-   The user can inspect elevator state.
-   The user can inspect pending requests.
-   External calls can be registered from the console.
-   Internal destination requests can be registered from the console.
-   The controller can be invoked from the console to serve the next
    request.
-   Invalid user input is handled without unexpectedly terminating the
    simulation.
-   The simulation continues until the user explicitly exits.
-   State persists correctly throughout a console session.
-   Existing Phase 1--5 behavior remains correct.
-   No Phase 7 automated test infrastructure has been introduced.
-   No unnecessary advanced functionality has been added.
