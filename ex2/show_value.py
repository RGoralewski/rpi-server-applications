#!/usr/bin/python3
#**
#******************************************************************************
#* @file       /ex2/show_value.py
#* @author     Radoslaw Goralewski
#* @version    V1.0
#* @date       21-Mar-2020
#* @brief      Raspberry Pi, Serwer IoT Lab : Exercise 2, Python script
#******************************************************************************

import sys
import getopt
from parse import parse

print("***Values displayer***")

temp_unit = None
hum_flag = False
press_flag = False

# Parse input
sysarg = sys.argv[1:]
try:
    opts, args = getopt.getopt(sysarg, "t:hp")
except getopt.GetoptError as e:
    print(e)
    sys.exit(1)

# Check options
for opt, arg in opts:
    if opt in '-t':
        temp_unit = arg
        if temp_unit != 'F' and temp_unit != 'C':
            print("Wrong temperature unit!")
            sys.exit(1)
    elif opt in '-h':
        hum_flag = True
    elif opt in '-p':
        press_flag = True

# Read values from file and display it
if temp_unit:
    with open('temperature.dat') as file:
        temperature = parse('{}C', file.readline())[0] # read only the first line
        if temp_unit == 'C':
            print("Temperature: {}C".format(temperature))
        elif temp_unit == 'F':
            print("Temperature: {:.1f}F".format(float(temperature) * 1.8 + 32.0))
if hum_flag:
    with open('humidity.dat') as file:
        humidity = parse('{}%', file.readline())[0]
        print("Humidity: {}%".format(humidity))
if press_flag:
    with open('pressure.dat') as file:
        pressure = parse('{}hPa', file.readline())[0]
        print("Pressure: {}hPa".format(pressure))
