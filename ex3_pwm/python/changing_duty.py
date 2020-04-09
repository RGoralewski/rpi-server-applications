#!/usr/bin/python3

import time
import sys
import select
import getopt
import numpy as np

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")


# Default
duty = 50 # [%]
freq = 50 # [Hz]

timeout = 0.1
i = ''

# Pin Definitions:
pwmPin = 12 # < LED: Physical pin 12, BCM GPIO18

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmPin, GPIO.OUT)

p = GPIO.PWM(pwmPin, freq)
p.start(duty)

print("Press ENTER to exit.")

while not i:
    # Waiting for I/O completion
    i, o, e = select.select([sys.stdin], [], [], timeout)

    if i:
        sys.stdin.readline().strip()
        p.stop()
        GPIO.cleanup() # cleanup all GPIO
        exit()

    for d in np.arange(0, 100, 0.5):
        p.ChangeDutyCycle(d)
        time.sleep(0.01)
    for d in np.arange(100, 0, 0.5):
        p.ChangeDutyCycle(d)
        time.sleep(0.01)
