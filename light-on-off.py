#! /usr/bin/python3

light-status == False
hold-time == 0
flash-time == 0

hold-time = int(input('Input sleep timer as seconds: ')
flash-time = int(input('Input flash count: ')

for light-status in range(0, flash-time):
	lisght-status = False
	time.sleep(hold-time)
	light-status = True
	print(str(light-status))


