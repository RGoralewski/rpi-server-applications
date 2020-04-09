#!/bin/bash
#**
#******************************************************************************
#* @file       /ex2/show_value.sh
#* @author     Radoslaw Goralewski
#* @version    V1.0
#* @date       22-Mar-2020
#* @brief      Raspberry Pi, Serwer IoT Lab : Exercise 2, Bash script
#******************************************************************************

temp_unit=""
hum_flag=0
press_flag=0

echo "***Values displayer***"

# standard while / case procedure for ' getopt ' function
while [ $# -gt 0 ]; do
    while getopts "t:hp" opt ; do
        case $opt in
            t)
                temp_unit=$OPTARG ;;
            h)
                hum_flag=1 ;;
            p)
                press_flag=1 ;;
            \?)
                echo "option '-$OPTARG not recognized'"
                exit 1 ;;
            : )
                echo "option '-$OPTARG requires argument'"
                exit 1 ;;
        esac
    done
    shift $((OPTIND-1))
done

# Display values from files
if [[ -n $temp_unit ]]; then
    first_line=$(head -n 1 "temperature.dat")
    if [[ $temp_unit == "C" ]]; then
        echo "Temperature: $first_line"
    elif [[ $temp_unit == "F" ]]; then
        temp_celsius=${first_line::-1}
        temp_fahrenheit=$(echo "temp=$temp_celsius;temp*=1.8;temp+=32.0;temp" | bc)
        echo "Temperature: ${temp_fahrenheit}F"
    else
        echo "Wrong temperature unit!"
        exit 1
    fi
fi
if [[ $hum_flag -gt 0 ]]; then
    first_line=$(head -n 1 "humidity.dat")
    echo "Humidity: $first_line"
fi
if [[ $press_flag -gt 0 ]]; then
    first_line=$(head -n 1 "pressure.dat")
    echo "Pressure: $first_line"
fi
