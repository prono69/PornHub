#!/bin/bash

mkdir /app/bin/
# downloading bins
wget -q -O /app/bin/megadown https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown
wget -q -O /app/bin/cmrudl https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py
wget -q -O /app/bin/megadirect https://raw.githubusercontent.com/adekmaulana/python-scripts/master/shell/megadirect
# changing bins permissions
chmod 755 bin/megadown
chmod 755 bin/cmrudl
chmod 755 bin/megadirect
echo "Succesfully bins are added"
