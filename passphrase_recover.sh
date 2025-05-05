#!/bin/bash

if [ -z "$ADDR" ]; then
  read -p "Enter target address: " ADDR
  export ADDR
fi

if [ -z "$MNEMONIC" ]; then
  read -p "Enter BIP39 mnemonic: " MNEMONIC
  export MNEMONIC
fi

echo "Using Python: $(which python)"

#echo "testing recovery with GPU acceleration"
#time python btcrecover.py --dsw  --enable-opencl --bip39 --addrs $ADDR --addr-limit 1 --tokenlist tokens.txt --mnemonic "$MNEMONIC"

echo "testing recovery without acceleration"
time python btcrecover.py --dsw --bip39 --addrs $ADDR --addr-limit 1 --tokenlist tokenlist.txt --mnemonic "$MNEMONIC"

