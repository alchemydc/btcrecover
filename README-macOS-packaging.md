# Packaging passphrase_recover_gui.py for macOS with py2app

## 1. Prepare Environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install py2app
```

## 2. Review setup.py

Ensure `setup.py` is present and correctly references `passphrase_recover_gui.py` as the entry point.

## 3. (Optional) Add App Icon

Convert your icon to `.icns` format and place it in the project directory. Uncomment and set the `iconfile` line in `setup.py`.

## 4. Build the App

```sh
python setup.py py2app
```

The `.app` bundle will be created in the `dist/` directory.

## 5. Test the App

- Double-click the `.app` in `dist/` to verify it launches and works.
- Test on a clean Mac (no Python, no Homebrew) if possible.

## 6. Sign and Notarize (Recommended)

- Sign the app with your Apple Developer ID.
- Submit for notarization to avoid Gatekeeper warnings.
- See: [Apple’s notarization guide](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)

## 7. Package for Distribution

- Use Disk Utility or `create-dmg` to package the `.app` as a `.dmg`.
- Alternatively, zip the `.app` for distribution.

## 8. User Instructions

- Drag the app to Applications.
- If Gatekeeper blocks the app, right-click and choose "Open" on first launch.

---

**Troubleshooting:**
- If you see missing library errors, add the relevant package to the `packages` or `includes` in `setup.py`.
- For native dependencies (e.g., coincurve), ensure they are built on the same macOS version you intend to distribute for.
