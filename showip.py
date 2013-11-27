#!/usr/bin/env python
#
# !!! Needs psutil installing:
#
#    $ sudo pip install psutil
#

import os
import sys
if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import pcd8544.lcd as lcd
import subprocess

# TODO: custom font bitmaps for up/down arrows
# TODO: Load histogram

    
def stats():
    lcd.text("adresses:")
    lcd.locate(0,0)
        
def main():
    lcd.init()
    lcd.set_contrast(190)
    lcd.backlight(1)
    lcd.text("adresses:")
    ip = subprocess.check_output("hostname -I", shell=True)
    lcd.locate(0,1)
    lcd.text(str(ip.strip()) )
    
if __name__ == "__main__":
    main()
