from setuptools import setup

APP = ['passphrase_recover_gui.py']
import os

def package_data_files():
    data_dirs = [
        "btcrecover/opencl",
        "btcrecover/test",
        "btcrecover/wordlists"
    ]
    data_files = []
    for d in data_dirs:
        for root, dirs, files in os.walk(d):
            file_list = [os.path.join(root, f) for f in files]
            if file_list:
                data_files.append((root, file_list))
    return data_files

DATA_FILES = package_data_files()
OPTIONS = {
    'argv_emulation': False,
    'packages': ['dotenv', 'FreeSimpleGUI'],
    'includes': ['tkinter', 'subprocess', 'tempfile', 'os', 'webbrowser'],
    # 'iconfile': 'app.icns',  # Uncomment and provide your .icns icon if available
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
