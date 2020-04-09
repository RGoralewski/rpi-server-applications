#!/usr/bin/python3

import time
import sys
import select

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")

timeout = 0.1
buttonState = True
buttonStateLast = True
cnt = 0
i = ''

# Pin Definitions:
buttonPin = 18 # < Push-button: Physical pin 18, BCM GPIO24

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin, GPIO.IN) # Button pin set as input

print("Press ENTER to exit.")

while not i:
    # Waiting for I/O completion
    i, o, e = select.select([sys.stdin], [], [], timeout)

    if i:
        sys.stdin.readline()
        GPIO.cleanup() # cleanup all GPIO
        exit()

    buttonState = (GPIO.input(buttonPin) == GPIO.HIGH)

    if (buttonState is False) and (buttonStateLast is True):
        cnt += 1
        print("Push-button counter: ", cnt)

    buttonStateLast = buttonState
