#!/usr/bin/python3

import time
import sys
import select

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")

timeout = 0.1
ledState = False
i = ''

# Pin Definitions:
ledPin = 16 # < LED: Physical pin 16, BCM GPIO23

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

print("Press ENTER to exit.")

GPIO.output(ledPin, GPIO.LOW)
while not i:
    # Waiting for I/O completion
    i, o, e = select.select([sys.stdin], [], [], timeout)

    if i:
        sys.stdin.readline()
        GPIO.cleanup() # cleanup all GPIO
        exit()

    ledState = not ledState

    if ledState:
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)
