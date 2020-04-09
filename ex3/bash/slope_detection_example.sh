#!/bin/bash
sh ./gpio_input_init_bash.sh
echo "Press any key to exit."
GPIO_STATE="1"
GPIO_STATE_LAST="1"
CNT=0
while [ true ] ;
do
    read -t .1 -n 1
    if [ $? = 0 ] ;
    then
        sh ./gpio_input_deinit_bash.sh
        exit ;
    else
        GPIO_STATE=$(./gpio_input_read_bash.sh)

        #echo "NOW: $GPIO_STATE"
        #echo "LAST: $GPIO_STATE_LAST"

        if [[ $GPIO_STATE -eq 0 ]] && [[ $GPIO_STATE_LAST -eq 1 ]];
        then
            CNT=$((CNT+1))
            echo "Push-button counter: $CNT"
        fi
        GPIO_STATE_LAST=$((GPIO_STATE))
    fi
done
