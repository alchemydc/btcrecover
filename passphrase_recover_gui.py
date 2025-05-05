#import freesimplegui as sg
import FreeSimpleGUI as sg
import tempfile
import subprocess
import os

layout = [
    [sg.Text('Enter target BTC address:'), sg.InputText(key='ADDRESS')],
    [sg.Text('Enter BIP39 mnemonic (seed phrase):')],
    [sg.Multiline(size=(60, 3), key='MNEMONIC')],
    [sg.Text('Enter passphrase/token list (one per line):')],
    [sg.Multiline(size=(60, 5), key='TOKENLIST')],
    [sg.Checkbox('Enable GPU acceleration (--enable-opencl)', key='OPENCL')],
    [sg.Button('Recover'), sg.Button('Cancel')],
    [sg.Output(size=(90, 15))]
]

window = sg.Window('btcrecover Passphrase Recovery', layout)

def validate_inputs(address, mnemonic, tokenlist):
    if not address.strip():
        print("Error: BTC address is required.")
        return False
    if not mnemonic.strip():
        print("Error: BIP39 mnemonic is required.")
        return False
    if not tokenlist.strip():
        print("Error: Passphrase/token list is required.")
        return False
    return True

while True:
    event, values = window.read()
    if event == 'Recover':
        address = values['ADDRESS']
        mnemonic = values['MNEMONIC']
        tokenlist = values['TOKENLIST']
        opencl = values['OPENCL']

        if not validate_inputs(address, mnemonic, tokenlist):
            continue

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tf:
            tf.write(tokenlist)
            tf.flush()
            tokenlist_path = tf.name

        cmd = [
            'python', 'btcrecover.py',
            '--dsw',
            '--bip39',
            '--addrs', address,
            '--addr-limit', '1',
            '--tokenlist', tokenlist_path,
            '--mnemonic', mnemonic.strip()
        ]
        if opencl:
            cmd.append('--enable-opencl')

        print(f"Running: {' '.join(cmd)}\n")
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in proc.stdout:
                print(line, end='')
            proc.wait()
        except Exception as e:
            print(f"Error running btcrecover: {e}")
        finally:
            os.remove(tokenlist_path)

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()
