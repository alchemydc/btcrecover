#import freesimplegui as sg
import FreeSimpleGUI as sg
sg.theme('DarkBlue')
import tempfile
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

max_cores = os.cpu_count()
default_threads = max(1, max_cores - 1)

address_default = os.getenv('ADDRESS', '')
mnemonic_default = os.getenv('MNEMONIC', '')
tokenlist_default = os.getenv('TOKENLIST', '')
try:
    threads_default = int(os.getenv('THREADS', default_threads))
    if threads_default < 1 or threads_default > max_cores:
        threads_default = default_threads
except Exception:
    threads_default = default_threads
opencl_env = os.getenv('OPENCL', '0').lower()
opencl_default = opencl_env in ('1', 'true', 'yes')

layout = [
    [sg.Text('Enter target BTC address:', tooltip='The Bitcoin address you want to recover funds for.'), 
     sg.InputText(default_text=address_default, key='ADDRESS', tooltip='The Bitcoin address you want to recover funds for.')],
    [sg.Text('Enter BIP39 mnemonic (seed phrase):', tooltip='Your 12/24-word recovery phrase. Words separated by spaces.')],
    [sg.Multiline(default_text=mnemonic_default, size=(60, 3), key='MNEMONIC', tooltip='Your 12/24-word recovery phrase. Words separated by spaces.')],
    [sg.Text('Input type:', tooltip='Provide a list of possible passphrases (passphrase list) or password fragments (token list).'), 
     sg.Combo(['Token List', 'Password List'], default_value='Token List', key='INPUT_TYPE', readonly=True, enable_events=True, tooltip='Provide a list of possible passphrases (passphrase list) or password fragments (token list).')],
    [sg.Text('Enter token list (one per line):', key='INPUT_LABEL', tooltip='Enter one candidate per line. Wildcards are supported in token lists.')],
    [sg.Multiline(default_text=tokenlist_default, size=(60, 5), key='INPUT_BOX', tooltip='Enter one candidate per line. Wildcards are supported in token lists.')],
    [sg.Text('Threads to use:', tooltip='Number of CPU cores to use for recovery. Leave at default for best UI responsiveness.'), 
     sg.Slider(range=(1, max_cores), orientation='h', size=(34, 20), default_value=threads_default, key='THREADS', tooltip='Number of CPU cores to use for recovery. Leave at default for best UI responsiveness.')],
    [sg.Checkbox('Enable GPU acceleration (--enable-opencl)', key='OPENCL', default=opencl_default, tooltip='Enable GPU acceleration if your system supports OpenCL.')],
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
    if event == 'INPUT_TYPE':
        # Update label based on selection
        if values['INPUT_TYPE'] == 'Token List':
            window['INPUT_LABEL'].update('Enter token list (one per line):')
        else:
            window['INPUT_LABEL'].update('Enter password list (one per line):')

    if event == 'Recover':
        address = values['ADDRESS']
        mnemonic = values['MNEMONIC']
        input_type = values['INPUT_TYPE']
        input_box = values['INPUT_BOX']
        opencl = values['OPENCL']
        threads = int(values['THREADS'])

        if not validate_inputs(address, mnemonic, input_box):
            continue

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tf:
            tf.write(input_box)
            tf.flush()
            inputlist_path = tf.name

        cmd = [
            'python', 'btcrecover.py',
            '--dsw',
            '--bip39',
            '--addrs', address,
            '--addr-limit', '1',
            '--mnemonic', mnemonic.strip(),
            '--threads', str(threads)
        ]
        if input_type == 'Token List':
            cmd += ['--tokenlist', inputlist_path]
        else:
            cmd += ['--passwordlist', inputlist_path]
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
            os.remove(inputlist_path)

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()
