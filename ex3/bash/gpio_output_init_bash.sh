# !/bin/bash
# GPIO output init example
# !! run with ' sudo '
# Exports pin to userspace
echo "23" > /sys/class/gpio/export
# Sets pin GPIO23 as an output
echo "out" > /sys/class/gpio/gpio23/direction
# Sets pin GPIO23 to low
echo "0" > /sys/class/gpio/gpio23/value
