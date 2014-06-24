# Keyboard Interruption in python
"""

	Author	:	ANOOP P T
	Date	:	24/06/2014
 
	Problem	:	Simple Clock
	
	
"""

import msvcrt
import os
from datetime import datetime
import time

while True:
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break
    os.system('cls')
    print(datetime.now().strftime('%H:%M:%S'))
    time.sleep(1)
    
##while 1:
##    print('Testing..')
##    # body of the loop ...
##    if msvcrt.kbhit():
##        os.system('cls')
##        print(ord(msvcrt.getch()))
##        if ord(msvcrt.getch()) == 13:
##            break
