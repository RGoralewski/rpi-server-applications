#!/bin/bash
# GPIO output reset example
# Sets pin GPIO23 to low
echo "0" > /sys/class/gpio/gpio23/value
