#!/bin/bash
# GPIO output deinit example
# Exports pin to userspace
echo "23" > /sys/class/gpio/unexport
