# Technical Context

## Technologies Used
- Python 3.x (core language for both CLI and GUI)
- btcrecover (CLI backend)
- GUI framework: FreeSimpleGUI
- python-dotenv for .env file support

## Development Setup
- Use a Python virtual environment (venv or similar) to isolate dependencies:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
- On macOS, install system dependencies for coincurve (libsecp256k1) before pip install:
  - `brew install automake`
  - `brew install libtool`
- Install dependencies from requirements.txt: `pip install -r requirements.txt`
- requirements.txt includes all necessary dependencies (FreeSimpleGUI, python-dotenv, etc.)
- Run CLI or GUI entrypoint as appropriate

## Technical Constraints
- Security: all sensitive data must remain local and be handled in-memory
- Cross-platform support (Windows, macOS, Linux)
- Usability for non-technical users

## Dependencies
- btcrecover: core wallet recovery logic
- coincurve (libsecp256k1): requires system libraries (`automake`, `libtool`) on macOS
- FreeSimpleGUI: user interface
- python-dotenv: .env file support for GUI field pre-population
- Standard Python libraries for subprocess, file I/O, etc.

## Tool Usage Patterns
- GUI invokes btcrecover CLI as a subprocess
- All user input is validated before processing
- Temporary files (if any) are securely deleted after use
- No network transmission of seeds or passphrases
- .env file can be used to pre-populate GUI fields for convenience
