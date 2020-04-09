# !/bin/bash
# GPIO input init example
# !! run with 'sudo'
# Exports pin to userspace
echo "24" > /sys/class/gpio/export
# Sets pin GPIO24 as an input
echo "in" > /sys/class/gpio/gpio24/direction
