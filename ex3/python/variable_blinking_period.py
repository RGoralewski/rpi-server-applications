#!/usr/bin/python3
#**
#******************************************************************************
#* @file        /ex3/python/variable_blinking_period.py
#* @author      Radoslaw Goralewski
#* @version     V1.0
#* @date        26-Mar-2020
#* @brief       Raspberry Pi, Serwer IoT Lab : Exercise 3, Python script GPIO
#******************************************************************************

import sys
import getopt
from parse import parse
import time
import select
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")

# Default values
min_period = 0.1
max_period = 0.5
step = 0.1

# Parse input
sysarg = sys.argv[1:]
try:
    opts, args = getopt.getopt(sysarg, "m:M:s:")
except getopt.GetoptError as e:
    print(e)
    sys.exit(1)

# Check options
for opt, arg in opts:
    if opt in '-m':
        min_period = float(arg)
    elif opt in '-M':
        max_period = float(arg)
        if (max_period <= min_period):
            print("Maximum period must be greater than minimum period!")
    elif opt in '-s':
        step = float(arg)

# Print set values
print("Minimum period: {}, Maximum period: {}, Step: {}".format(min_period, max_period, step))

# Initialize necessary variables
blinking_period = max_period
buttonState = True
buttonStateLast = True
ledState = False
i = ''

# Pin Definitions:
ledPin = 16 # < LED: Physical pin 16, BCM GPIO23
buttonPin = 18 # < Push-button: Physical pin 18, BCM GPIO24

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(buttonPin, GPIO.IN) # Button pin set as input

GPIO.output(ledPin, ledState)

print("Press ENTER to exit.")

while not i:
    # Waiting for I/O completion
    i, o, e = select.select([sys.stdin], [], [], blinking_period)

    if i:
        sys.stdin.readline()
        GPIO.cleanup() # cleanup all GPIO
        exit()

    # If button is pressed, change blinking period
    buttonState = (GPIO.input(buttonPin) == GPIO.HIGH)
    if (buttonState is False) and (buttonStateLast is True):
        blinking_period -= step
        if blinking_period < min_period:
            blinking_period = max_period
        print("Button pressed! Current period: {:.1f}".format(blinking_period))
    # Save last button state
    buttonStateLast = buttonState

    # Change LED state
    ledState = not ledState
    GPIO.output(ledPin, ledState)
