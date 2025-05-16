# macOS Build Compatibility Instructions

To maximize compatibility of your packaged .app across multiple macOS versions:

---

## 1. Build on the Oldest Supported macOS Version

- Always build your app on the oldest version of macOS you want to support (e.g., Monterey, Big Sur).
- Binaries built on newer macOS versions may use system libraries or symbols not present on older systems, causing runtime errors.

## 2. Use the Official Python.org Installer

- Download and install Python from https://www.python.org for the target macOS version.
- Avoid using Homebrew or system Python, as they may link against newer or incompatible system libraries.

## 3. Set Deployment Target (Advanced)

- You can try setting the deployment target environment variable before building:
  ```sh
  export MACOSX_DEPLOYMENT_TARGET=11.0  # For Big Sur, for example
  ```
- Note: This does not always guarantee compatibility if the build host is newer than the target OS.

## 4. Test on All Target macOS Versions

- After building, test the .app on the oldest and newest macOS versions you intend to support.
- This helps catch compatibility issues before distribution.

---

**Summary:**  
- The most reliable way to ensure compatibility is to build on the oldest macOS version you want to support, using the official Python.org Python for that OS.
- Cross-version compatibility is a common challenge for all macOS app packaging tools.
