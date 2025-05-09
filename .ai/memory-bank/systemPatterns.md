# System Patterns

## System Architecture
- Modular structure: Python library backend (btcrpass.py library) and a GUI frontend (tk).
- .env file support for pre-populating GUI fields (via python-dotenv).
- "Advanced Options" toggle in the GUI controls visibility of address limit, thread selection, and GPU acceleration controls.
- Wildcard cheatsheet hyperlink is shown next to the token list label when Token List is selected.
- Direct use of btcrecover internals (e.g., btcrpass) in isolation is not robust: many globals must be manually set, and the modules are not designed for modular reuse without full CLI context.

## Key Technical Decisions
- Use Python for both backend and GUI for compatibility and ease of integration.
- Security-first: all sensitive data handled in-memory, never sent externally.
- GUI framework selection prioritizes simplicity, cross-platform support, and permissive licensing
- GUI supports user-selectable input type (Token List or Password List) and passes correct flag to backend.
- Tooltips provided for all input fields to improve usability.
- Advanced options visibility logic: attempted explicit boolean handling for hiding, reverted to original logic after issue persisted.

## Design Patterns in Use
- Separation of concerns: GUI and recovery logic are decoupled.
- Input validation and error handling at all user input points.
- Documentation-driven development (Memory Bank as source of truth).

## Component Relationships
- GUI frontend collects user input and displays results.
- Backend (btcrpass.py library) performs seed/passphrase recovery.
- Communication via direct Python API if feasible.  Initial attempts using subprocess calls yielded bad UX that didn't show progress to user

## Critical Implementation Paths
- User launches GUI → enters seed/passphrase candidates → GUI invokes backend recovery → results displayed.
- CLI proof-of-concept for 25th word recovery is foundational for GUI workflow.
