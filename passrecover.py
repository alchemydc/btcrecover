#!/usr/bin/env python3

# passrecover.py -- Bitcoin BIP39 passphrase (25th word) recovery tool
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.
#

import compatibility_check

from btcrecover import btcrpass
import sys, multiprocessing

if __name__ == "__main__":
    print()
    print("Starting", btcrpass.full_version())

    btcrpass.parse_arguments(sys.argv[1:])
    (passphrase_found, not_found_msg) = btcrpass.main()

    if isinstance(passphrase_found, str):
        print()
        #print("If this tool helped you to recover funds, please consider donating 1% of what you recovered, in your crypto of choice to:")
        #print("BTC: 37N7B7sdHahCXTcMJgEnHz7YmiR4bEqCrS ")
        #print("BCH: qpvjee5vwwsv78xc28kwgd3m9mnn5adargxd94kmrt ")
        #print("LTC: M966MQte7agAzdCZe5ssHo7g9VriwXgyqM ")
        #print("ETH: 0x72343f2806428dbbc2C11a83A1844912184b4243 ")
        #print("DOGE: DMQ6uuLAtNoe5y6DCpxk2Hy83nYSPDwb5T ")
        #print("DASH: Xx2umk6tx25uCWp6XeaD5f7CyARkbemsZG ")
        #print("MONA: mona1q504vpcuyrrgr87l4cjnal74a4qazes2g9qy8mv ")
        #print()
        #print("You may also consider donating to Gurnec, who created and maintained this tool until late 2017 @ 3Au8ZodNHPei7MQiSVAWb7NB2yqsb48GW4")
        #print()
        if hasattr(btcrpass, "safe_print"):
            btcrpass.safe_print("Passphrase found: '" + passphrase_found + "'")
        else:
            print("Passphrase found: '" + passphrase_found + "'")
        if any(ord(c) < 32 or ord(c) > 126 for c in passphrase_found):
            print("HTML Encoded Passphrase:   '" + passphrase_found.encode("ascii", "xmlcharrefreplace").decode() + "'")
        retval = 0

    elif not_found_msg:
        print(not_found_msg)
        retval = 0

    else:
        retval = 1  # An error occurred or Ctrl-C was pressed

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    sys.exit(retval)
