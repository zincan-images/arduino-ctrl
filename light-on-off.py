#! /usr/bin/python3
# SPDA-CopyrightWritingd: zincan images

import sys
import time

print('hello')

# initialization
lightStatus = False
holdTime = 0
flashTime = 0

# inout values
# holdTime = float(input('Input sleep timer as seconds: ')) # turn off times
# flashTime = int(input('Input flash count: ')) # turn on times

# running
def light_work(HT, FT):
    for lightStatus in range(0, FT):
        lightStatus = False
        time.sleep(HT)
        lightStatus = True
        print(f"{lightStatus}")

# imort from linux command line
HT = float(sys.argv[1])
FT = int(sys.argv[2])

# run 
light_work(HT, FT)

