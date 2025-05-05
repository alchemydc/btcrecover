# Technical Context

## Technologies Used
- Python 3.x (core language for both CLI and GUI)
- btcrecover (CLI backend)
- GUI framework: Gooey, PySimpleGUI, or Tkinter (TBD)

## Development Setup
- Use a Python virtual environment (venv or similar) to isolate dependencies:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
- Install dependencies from requirements.txt: `pip install -r requirements.txt`
- GUI dependencies will be added based on framework selection
- Run CLI or GUI entrypoint as appropriate

## Technical Constraints
- Security: all sensitive data must remain local and be handled in-memory
- Cross-platform support (Windows, macOS, Linux)
- Usability for non-technical users

## Dependencies
- btcrecover: core wallet recovery logic
- GUI library (Gooey, PySimpleGUI, or Tkinter): user interface
- Standard Python libraries for subprocess, file I/O, etc.

## Tool Usage Patterns
- GUI invokes btcrecover CLI as a subprocess or via direct Python API
- All user input is validated before processing
- Temporary files (if any) are securely deleted after use
- No network transmission of seeds or passphrases
