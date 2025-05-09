# Active Context

## Current Work Focus
- Creating a copy of seedrecover.py called passrecover.py that uses the btcrpass.py to brute force the 25th word, given a known 12 or 24 word mnemonic.


## Recent Changes
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
1. Creating a copy of seedrecover.py called passrecover.py that uses the btcrpass.py to brute force the 25th word, given a known 12 or 24 word mnemonic.

## Active Decisions and Considerations
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
