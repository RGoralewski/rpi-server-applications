#!/bin/bash
#**
#******************************************************************************
#* @file       /ex3/bash/variable_blinking_period.sh
#* @author     Radoslaw Goralewski
#* @version    V1.0
#* @date       27-Mar-2020
#* @brief      Raspberry Pi, Serwer IoT Lab : Exercise 3, Bash script GPIO
#******************************************************************************

# Default values
MIN_PERIOD=0.1
MAX_PERIOD=0.5
STEP=0.1

# standard while / case procedure for ' getopt ' function
while [ $# -gt 0 ]; do
    while getopts "m:M:s:" opt ; do
        case $opt in
            m)
                MIN_PERIOD=$OPTARG ;;
            M)
                MAX_PERIOD=$OPTARG;;
            s)
                STEP=$OPTARG ;;
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

if (( $(echo "$MAX_PERIOD < $MIN_PERIOD" |bc -l) ));
then
    echo "Maximum period must be greater than minimum period!"
    exit 1;
fi

echo "Minimum period: $MIN_PERIOD, Maximum period: $MAX_PERIOD, Step: $STEP"

# Initialize GPIO
sh ./gpio_input_init_bash.sh
sh ./gpio_output_init_bash.sh

echo "Press any key to exit."

# Initialize necessary variables
BLINKING_PERIOD=$MAX_PERIOD
BUTTON_STATE="1"
BUTTON_STATE_LAST="1"
LED_STATE="0"

sh ./gpio_output_reset_bash.sh

while [ true ] ;
do
    read -t $BLINKING_PERIOD -n 1
    if [ $? = 0 ] ;
    then
        sh ./gpio_input_deinit_bash.sh
        sh ./gpio_output_deinit_bash.sh
        exit ;
    else
        BUTTON_STATE=$(./gpio_input_read_bash.sh)

        # Change blinking period if button is pressed
        if [[ $BUTTON_STATE -eq 0 ]] && [[ $BUTTON_STATE_LAST -eq 1 ]];
        then
            BLINKING_PERIOD=$(echo "$BLINKING_PERIOD-$STEP" | bc)
            if (( $(echo "$BLINKING_PERIOD < $MIN_PERIOD" |bc -l) ));
            then
                BLINKING_PERIOD=$MAX_PERIOD
            fi
            echo "Button pressed! Current period: $BLINKING_PERIOD"
        fi
        BUTTON_STATE_LAST=$((BUTTON_STATE))

        # Change LED state
        if (( LED_STATE == 0 )) ; then
            LED_STATE=1
            sh ./gpio_output_set_bash.sh
        else
            LED_STATE=0
            sh ./gpio_output_reset_bash.sh
        fi
    fi
done
