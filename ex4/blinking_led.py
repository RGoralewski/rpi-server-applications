#!/usr/bin/python3
#**
#******************************************************************************
#* @file        /ex4/blinking_led.py
#* @author      Radoslaw Goralewski
#* @version     V1.0
#* @date        30-Mar-2020
#* @brief       Raspberry Pi, Serwer IoT Lab : Exercise 4, Python script
#******************************************************************************

import sys
import time
import select
import json
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")

# Default blinking period
blinking_period = 0.1

print("Default blinking step: {}".format(blinking_period))

# Initialize necessary variables
ledState = False
i = ''
last_read_time = time.time()

# Pin Definitions:
ledPin = 16 # < LED: Physical pin 16, BCM GPIO23

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

GPIO.output(ledPin, ledState)

print("Press ENTER to exit.")

while not i:
    # Waiting for I/O completion
    i, o, e = select.select([sys.stdin], [], [], blinking_period)

    if i:
        sys.stdin.readline()
        GPIO.cleanup() # cleanup all GPIO
        exit()

    # Read a new period from file every one second
    current_time = time.time()
    if (current_time - last_read_time) > 1.0:
        with open('period.dat') as file:
            line = file.readline()
            data = json.loads(line)
            blinking_period = data['period']
        last_read_time = time.time()

    # Change LED state
    ledState = not ledState
    GPIO.output(ledPin, ledState)
