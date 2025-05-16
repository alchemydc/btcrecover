# Active Context

## Current Work Focus
- Initial implementation of wildcard passphrase expansion for `--passphrase-list` in `btcrseed.py` is complete and functional for passphrases with up to two wildcards.
- New focus: Investigating and resolving an `AssertionError: outer_iterations > 0` that occurs in `btcrpass.py` when a candidate passphrase contains more than two wildcards.
- Ongoing: Improved macOS packaging and cross-version compatibility for the GUI app, including py2app troubleshooting and documentation.

## Recent Changes
- Successfully enabled wildcard expansion for `--passphrase-list` in `btcrseed.py` for up to two wildcards.
  - Resolved `NameError: name 'tstr' is not defined` in `btcrpass.py` when `init_wildcards()` was called from `btcrseed.py`.
  - The fix involved modifying `btcrseed.py`'s `main()` function to explicitly set `btcrpass.tstr = str`, `btcrpass.tchr = chr`, and `btcrpass.string = string_module` as attributes on the imported `btcrpass` module before calling `btcrpass.init_wildcards()`. This ensures necessary globals are available.
  - `WalletBIP39.config_mnemonic` in `btcrseed.py` now correctly uses `btcrpass.expand_wildcards_generator(passphrase)` for passphrases containing '%' to generate all expanded versions.
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
- **macOS packaging and distribution:** Successfully built the GUI app as a .app using py2app, resolved missing dependency and launch errors, and documented troubleshooting steps for py2app and cross-version macOS compatibility.
- **Documentation:** Added `build_compatibility.md` to the memory bank, summarizing best practices for building on the oldest supported macOS version, using the official Python.org installer, and testing on all target OS versions.

## Next Steps
1. Investigate and fix the `AssertionError: outer_iterations > 0` in `btcrpass.py` that occurs when a candidate passphrase (from `--passphrase-list` in `seedrecover.py`) contains more than two wildcards.
2. Complete the pending git commit and push for the wildcard passphrase expansion feature and previous Memory Bank updates.
3. Update Memory Bank (`activeContext.md`, `progress.md`) after resolving the new `AssertionError`.
4. Continue refining packaging and distribution for non-technical users, referencing the new compatibility documentation.

## Active Decisions and Considerations
- The fix for the `tstr` NameError during wildcard passphrase expansion involved a targeted initialization of `btcrpass` globals from `btcrseed.py`. This avoided a full `btcrpass.parse_arguments()` call, which had its own CLI argument validation that was problematic for this initialization-only purpose.
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
- Inter-module dependencies and initialization order (e.g., `btcrseed.py` calling `btcrpass.py` functions) can lead to subtle errors like `NameError` if not all globals are available as expected when a module is used as a library. Direct initialization or provision of these globals from the calling module can serve as a workaround.
- Early focus on documentation and security requirements will guide both CLI and GUI development.
- The CLI workflow for 25th word recovery is foundational for the GUI feature set.
- Hands-on CLI testing confirmed the documented workflow is robust and effective.
