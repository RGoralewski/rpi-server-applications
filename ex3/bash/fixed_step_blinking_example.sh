#!/bin/bash
sh ./gpio_output_init_bash.sh
echo "Press any key to exit."
GPIO_STATE=0
while [ true ] ;
do
read -t .1 -n 1
    if [ $? = 0 ] ;
    then
        sh ./gpio_output_deinit_bash.sh
        exit ;
    else
        if (( GPIO_STATE == 0 )) ; then
            GPIO_STATE=1
            sh ./gpio_output_set_bash.sh
        else
            GPIO_STATE=0
            sh ./gpio_output_reset_bash.sh
        fi
    fi
done
