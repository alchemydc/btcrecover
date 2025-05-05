# Progress

## What Works
- Project brief and Memory Bank structure established.
- Security requirements and technical context documented.
- Proof-of-concept for 25th word (BIP39 passphrase) recovery using the CLI completed and tested.

## What's Left to Build
- Design and build the GUI frontend using FreeSimpleGUI (or Tkinter) as a wrapper that calls btcrecover.py via subprocess.
- Integrate the GUI with the btcrecover backend using subprocess calls.
- Add slider to allow user to control number of cores allocated to cracking.
- Add tooltips to GUI
- Add explainers for how the token list is used by btcrecover
- Add progress bar
- Add advanced settings / view to allow user to stop cracking and continue where they left off, potentially on multiple machines

## Current Status
- CLI 25th word recovery workflow is functional and documented.
- Architectural decision made: Gooey is not suitable due to lack of argparse in btcrecover.py. 
- GUI development will proceed using PySimpleGUI (or Tkinter) with subprocess integration.

## Known Issues
- btcrecover uses all cores, which leaves nothing left for UI while running
- cancel button in UI doesn't work

## Evolution of Project Decisions
- Security elevated to a top-level requirement (handle seeds/passphrases with care).
- Use of Python virtual environments (venv) mandated for dependency isolation.
- Documentation-first workflow adopted to ensure clarity and continuity.
- Gooey was evaluated but rejected due to incompatibility with the current CLI structure; PySimpleGUI (or Tkinter) with subprocess is now the preferred GUI approach.
