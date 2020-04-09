#!/usr/bin/python3

import time
import sys
import select
import getopt

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script.")


# Default
duty = 50 # [%]
freq = 50 # [Hz]

# Parse input
sysarg = sys.argv[1:]
try:
    opts, args = getopt.getopt(sysarg, "d:f:")
except getopt.GetoptError as e:
    print(e)
    sys.exit(1)

# Check options
for opt, arg in opts:
    if opt in '-d':
        duty = int(arg)
        if (duty < 0 or duty > 100):
            print("Duty must be 0-100%!")
            sys.exit()
    elif opt in '-f':
        freq = int(arg)
        if (freq < 1):
            print("Frequency must be greater than 0!")
            sys.exit()

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
