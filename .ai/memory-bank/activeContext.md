# Active Context

## Current Work Focus
- Pivoting strategy: Pausing `passrecover.py` GUI development. New focus is on investigating and planning enhancements to `btcrseed.py` to support wildcard expansion for passphrase lists (similar to its tokenlist functionality).


## Recent Changes
- Created `passrecover.py`, a CLI tool modeled on `seedrecover.py` and `btcrecover.py`. It correctly uses `btcrpass.parse_arguments()` and `btcrpass.main()` for BIP39 passphrase (25th word) recovery. Currently, it's CLI-only; GUI development for it is now paused.
- Added a top-level Security Considerations section to productContext.md, requiring careful handling of partial seeds and passphrase fragments.
- Documented that on macOS, installing coincurve (libsecp256k1) requires `brew install automake` and `brew install libtool` before running pip install.
- Successfully completed and validated the CLI 25th word (BIP39 passphrase) recovery workflow.
- Switched GUI implementation from PySimpleGUI to FreeSimpleGUI due to PySimpleGUI's license change; FreeSimpleGUI is now used for the proof-of-concept GUI.
- Major GUI improvements:
  - .env file support for pre-populating UI fields using python-dotenv.
  - Dark mode enabled by default.
  - User can select between Token List and Password List input types; correct flag is passed to btcrecover.
  - Dynamic label updates for input type.
  - Tooltips added to all input fields for user guidance.
  - requirements.txt restored and python-dotenv added as a dependency.
  - "Advanced Options" toggle added: address limit, thread selection, and GPU acceleration controls are now only visible when enabled.
  - Wildcard cheatsheet hyperlink added next to "Enter token list" label, visible only for Token List input type.
  - Attempted fix for advanced options visibility (ensuring column hides when deselected); reverted to original logic after issue persisted.

## Next Steps
1. Complete the pending git commit and push for the initial creation of `passrecover.py` and the previous Memory Bank updates.
2. Investigate how `btcrpass.py` (used by `btcrseed.py` for password generation logic) handles wildcard expansion for tokenlists.
3. Plan modifications to `btcrseed.py` (and potentially `btcrpass.py` if common logic can be shared/extended) to enable similar wildcard expansion for the `--passphrase-list` argument when used with `seedrecover.py`.
4. Update Memory Bank (`activeContext.md`, `progress.md`) to reflect detailed findings and the plan for implementing passphrase wildcard expansion in `btcrseed.py`.

## Active Decisions and Considerations
- Decision to pause direct GUI development for `passrecover.py`. Given that `btcrpass.py` (its core) lacks native UI hooks, integrating a responsive GUI is complex.
- Redirecting efforts to enhance `btcrseed.py` for wildcard support in passphrase lists. This leverages `btcrseed.py`'s existing GUI integration (via `seedrecover.py`) and aims to provide a more powerful and user-friendly passphrase recovery experience within the established seed recovery workflow.
- Security is a top-level requirement: all sensitive data must be handled with care and never leave the user's machine.
- The GUI must be accessible to non-technical users, with advanced options hidden by default (address limit, thread selection, and GPU acceleration are only shown when "Show Advanced Options" is enabled).
- System dependencies for cryptographic libraries (e.g., coincurve) must be documented for each platform; on macOS, Homebrew packages `automake` and `libtool` are required.
- Gooey is not suitable for this project because btcrecover.py does not use argparse; refactoring for Gooey would be disruptive.
- PySimpleGUI was rejected due to its new license; FreeSimpleGUI (or Tkinter) with subprocess is now the preferred approach for building the GUI, as it allows the core logic to remain unchanged and is easy to maintain.

## Important Patterns and Preferences
- Documentation-first workflow: Memory Bank is the single source of truth for project context and progress.
- Stepwise, user-friendly recovery process.

## Learnings and Project Insights
- Early focus on documentation and security requirements will guide both CLI and GUI development.
- The CLI workflow for 25th word recovery is foundational for the GUI feature set.
- Hands-on CLI testing confirmed the documented workflow is robust and effective.
