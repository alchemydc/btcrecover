#!/bin/bash

if [ -z "$ADDRESS" ]; then
  read -p "Enter target address: " ADDRESS
  export ADDRESS
fi

if [ -z "$MNEMONIC" ]; then
  read -p "Enter BIP39 mnemonic: " MNEMONIC
  export MNEMONIC
fi

echo "Using Python: $(which python)"

#echo "testing recovery with GPU acceleration"
#time python btcrecover.py --dsw  --enable-opencl --bip39 --addrs $ADDRESS --addr-limit 1 --tokenlist tokens.txt --mnemonic "$MNEMONIC"

#echo "testing recovery without acceleration"
#time python btcrecover.py --dsw --bip39 --addrs $ADDRESS --addr-limit 1 --tokenlist tokenlist.txt --mnemonic "$MNEMONIC"

#python seedrecover.py --dsw --wallet-type bip39 --addrs $ADDRESS --addr-limit 1 --tokenlist tokenlist.txt --mnemonic "$MNEMONIC" --mnemonic-length 24 --language en
python seedrecover.py --threads 1 --dsw --wallet-type bip39 --addrs $ADDRESS --addr-limit 1 --passphrase-list passwordlist.txt --mnemonic "$MNEMONIC" --mnemonic-length 24 --language en

#python seedrecover_tokenpass.py --threads 1 --dsw --wallet-type bip39 --addrs $ADDRESS --addr-limit 1 --tokenlist tokenlist.txt --mnemonic "$MNEMONIC" --mnemonic-length 24 --language en
