# Product Context

## Security Considerations
Partial seeds and passphrase fragments must be handled with care using industry best practices. Sensitive data should never leave the user's machine, and all temporary storage or in-memory handling must minimize exposure and risk.

## Purpose
Enable non-technical users to recover access to their cryptocurrency wallets by providing a user-friendly GUI for btcrecover.

## Problems Solved
- Users who have lost access to funds due to incorrectly recorded seed phrases or forgotten BIP39 passphrases ("25th word").
- Reduces the technical barrier for wallet recovery, making advanced recovery tools accessible to a broader audience.

## How It Should Work
- Users launch the GUI and are guided through the process of entering their known seed words and possible passphrase candidates.
- The tool generates and tests combinations using the btcrpass.py library
- Results (success/failure, recovered passphrase, or next steps) are clearly presented in the GUI.

## User Experience Goals
- Simple, step-by-step workflow for non-technical users.
- Clear instructions and helpful error messages.
- Minimal required input; advanced options hidden by default.
- Safe handling of sensitive data (seeds/passphrases never leave the user's machine).
- Fields can be pre-populated from a .env file for convenience.
- Tooltips provided for all input fields to guide users.
