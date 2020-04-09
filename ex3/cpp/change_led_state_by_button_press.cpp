#include <iostream>
#include <future>
#include <thread>
#include <chrono>
#include <wiringPi.h>

int main()
{
    const int led = 4; // < Red LED: Physical pin 16, BCM GPIO23, and WiringPi pin 4
    const int button = 5; // < LED: Physical pin 18, BCM GPIO24, and WiringPi pin 5

    bool btn_state = true, btn_state_last = true;
    bool led_state = false;

    std::chrono::milliseconds timeout(100);
    std::future<int> async_getchar = std::async(std::getchar);

    wiringPiSetup();

    pinMode(led, OUTPUT);
    pinMode(button, INPUT);

    digitalWrite(led, LOW);

    std::cout << "Press ENTER to exit." << std::endl;

    while(1)
    {
        btn_state = (digitalRead(button) == HIGH);

        if (!btn_state && btn_state_last)
        {
            led_state = !led_state;
            digitalWrite(led, led_state);
            std::cout << "LED state: ";
            if (led_state)
                std::cout << "ON" << std::endl;
            else
                std::cout << "OFF" << std::endl;
        }

        btn_state_last = btn_state;

        if(async_getchar.wait_for(timeout) == std::future_status::ready)
        {
            async_getchar.get();
            break;
        }
    }

    return 0;
}
