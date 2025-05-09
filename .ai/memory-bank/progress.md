# Progress

## What Works
- Project brief and Memory Bank structure established.
- Security requirements and technical context documented.
- Proof-of-concept for 25th word (BIP39 passphrase) recovery using the CLI completed and tested.
- Initial POC GUI frontend built using FreeSimpleGUI as a wrapper that calls btcrecover.py via subprocess. Works but UX is bad because no progress is shown until subprocess completes.
- GUI features:
  - .env file support for pre-populating fields (python-dotenv).
  - Dark mode enabled by default.
  - User-selectable Token List or Password List input type; correct flag passed to btcrecover.
  - Dynamic label updates for input type.
  - Tooltips added to all input fields.
  - requirements.txt restored and python-dotenv added as a dependency.
  - "Advanced Options" toggle controls visibility of address limit, thread selection, and GPU acceleration controls.
  - Wildcard cheatsheet hyperlink next to "Enter token list" label, visible only for Token List input type.
  - Thread slider and GPU acceleration moved to advanced options.
  - Attempted fix for advanced options visibility (explicit boolean), reverted to original logic after issue persisted.

## What's Left to Build
- Create passrecover.py modeled on seedrecover.py but using btcrpass.py under the hood instead of btcrseed.py.  This should result in a much more responsive UI that shows progress, etc.
- Add explainers/help for how token lists and wildcards work with btcrecover (wildcard cheatsheet hyperlink now present in UI).
- Add progress bar to GUI.
- Add advanced settings/view to allow user to stop cracking and continue where they left off, potentially on multiple machines.
- Improve cancel button reliability and UI responsiveness during cracking.
- Perform cross-platform testing and gather user feedback.
- If modularization is needed, consider refactoring btcrecover internals to reduce reliance on global state.

## Current Status
- CLI 25th word recovery workflow is functional and documented.
- GUI frontend is functional with major usability features implemented.
- Architectural decision made: Gooey is not suitable due to lack of argparse in btcrecover.py.
- GUI development is proceeding using FreeSimpleGUI with subprocess integration.

## Known Issues
- no progress is shown in the UI (passphrase_recover_gui.py) after the subprocess is created until it completes. this is bad UX
- cancel button in UI doesn't work
- Advanced options column does not hide as expected when toggled off (FreeSimpleGUI limitation or bug).

## Evolution of Project Decisions
- Wrapping btcrecover.py with passphrase_recover_gui.py does not seem to provide the UX experience that we want. suggest looking at seedrecover.py (which leverages btcrseed.py) and creating passrecover.py which will leverage btcrpass.py.
- btcrpass.py is too large to fit into LLM context, so will need to do some work by hand to create a GUI wrapper for it. we can learn a lot from looking at seedrecover.py.
- Security elevated to a top-level requirement (handle seeds/passphrases with care).
- Use of Python virtual environments (venv) mandated for dependency isolation.
- Documentation-first workflow adopted to ensure clarity and continuity.
- Gooey was evaluated but rejected due to incompatibility with the current CLI structure; PySimpleGUI (now FreeSimpleGUI) with subprocess is now the preferred GUI approach.


