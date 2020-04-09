/**
 ******************************************************************************
 * @file       /ex3/cpp/variable_blinking_period.cpp
 * @author     Radoslaw Goralewski
 * @version    V1.0
 * @date       28-Mar-2020
 * @brief      Raspberry Pi, Serwer IoT Lab : Exercise 3, C++ program GPIO
 ******************************************************************************
 */

#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <wiringPi.h>
#include <future>
#include <thread>
#include <chrono>

int main(int argc, char *argv[])
{
    //Default values
    int min_period = 100;
    int max_period = 500;
    int step = 100;


    int arg;

    /* Standard while / switch procedure for ' getopt ' function */
    while ((arg = getopt(argc, argv, "m:M:s:")) != -1)
    {
        switch(arg)
        {
            case 'm':
                min_period = atof(optarg) * 1000;
                break;
            case 'M':
                max_period = atof(optarg) * 1000;
                break;
            case 's':
                step = atof(optarg) * 1000;
                break;
            case '?':
                if((optopt == 'm') || (optopt == 'M') || (optopt == 's'))
                    std::cerr << "option -" << static_cast<char>(optopt) << " requires argument" << std::endl;
                else if(isprint(optopt))
                    std::cerr << "option -" << static_cast<char>(optopt) << " not recognized" << std::endl;
                else
                    std::cerr << "option character \\x" << optopt << " not recognized" << std::endl;
                return 1;
            default:
                abort();
        }
    }

    std::cout << "Minimum period: " << float(min_period / 1000.0) << ", Maximum period: " << float(max_period / 1000.0) << ", Step: " << float(step / 1000.0) << std::endl;

    //Initialize necessary variables
    bool button_state = true;
    bool button_state_last = true;
    bool led_state = false;

    const int led = 4; // < LED: Physical pin 16, BCM GPIO23, and WiringPi pin 4
    const int button = 5; // < LED: Physical pin 18, BCM GPIO24, and WiringPi pin 5

    std::chrono::milliseconds blinking_period(max_period);
    std::future<int> async_getchar = std::async(std::getchar);

    wiringPiSetup();

    pinMode(led, OUTPUT);
    pinMode(button, INPUT);

    digitalWrite(led, LOW);

    std::cout << "Press ENTER to exit." << std::endl;

    while(1)
    {
        //Read button state
        button_state = (digitalRead(button) == HIGH);

        //If was pressed, change the blinking period
        if (!button_state && button_state_last)
        {
            blinking_period -= std::chrono::milliseconds(step);
            if (blinking_period < std::chrono::milliseconds(min_period)) {
                blinking_period = std::chrono::milliseconds(max_period);
            }
            std::cout << "Button pressed! Current period: " << float(blinking_period.count() / 1000.0) << std::endl;
        }

        //Save state
        button_state_last = button_state;

        //Toggle LED
        led_state = !led_state;
        digitalWrite(led, led_state);

        //Wait for the blinking_period time, if enter was pressed exit program
        if(async_getchar.wait_for(blinking_period) == std::future_status::ready)
        {
            async_getchar.get();
            break;
        }
    }

    return 0;
}
