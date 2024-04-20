#! /usr/bin/python3

import time

lightStatus = False
holdTime = 0
flashTime = 0

holdTime = float(input('Input sleep timer as seconds: '))
flashTime = int(input('Input flash count: '))

for lightStatus in range(0, flashTime):
    lisghtStatus = False
    time.sleep(holdTime)
    lightStatus = True
    print(str(lightStatus))
