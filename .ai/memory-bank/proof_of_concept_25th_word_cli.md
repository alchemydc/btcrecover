# Proof of Concept: 25th Word (BIP39 Passphrase) Recovery via CLI

## Objective
Demonstrate the process of recovering a BIP39 passphrase ("25th word") using the btcrecover CLI before implementing GUI features.

## Steps

1. **Prepare Your BIP39 Seed Phrase**
   - Collect your 12 or 24 known seed words.

2. **Create a Tokenlist File**
   - Make a text file (e.g., `tokens.txt`) with possible passphrase candidates, one per line.

3. **Run btcrecover with the `--bip39` Option**
   - Use the following command format:
     ```
     python btcrecover.py --bip39 --tokenlist tokens.txt [other-options...]
     ```
   - Common additional options:
     - `--addrs <target_address>`: If you know an address to check for.
     - `--wallet-type <type>`: Specify wallet type if not Bitcoin.
     - `--bip32-path <path>`: For custom derivation paths.

4. **Review Results**
   - btcrecover will try each passphrase candidate as the 25th word and report any successful recovery.

## Example Command
```
python btcrecover.py --bip39 --tokenlist tokens.txt --addrs <target_address>
```

## References
- [docs/TUTORIAL.md](../docs/TUTORIAL.md#bip-39-passphrases)
- [docs/Seedrecover_Quick_Start_Guide.md](../docs/Seedrecover_Quick_Start_Guide.md)

## Notes
- All sensitive data must remain local and be handled securely.
- This workflow is foundational for the GUI implementation.
