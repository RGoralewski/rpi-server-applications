#include <iostream>
#include <future>
#include <thread>
#include <chrono>
#include <wiringPi.h>

int main()
{
    const int button = 5; // < LED: Physical pin 18, BCM GPIO24, and WiringPi pin 5

    bool gpio_state = true, gpio_state_last = true;
    unsigned int cnt = 0;

    std::chrono::milliseconds timeout(100);
    std::future<int> async_getchar = std::async(std::getchar);

    wiringPiSetup();

    pinMode(button, INPUT);

    std::cout << "Press ENTER to exit." << std::endl;

    while(1)
    {
        gpio_state = (digitalRead(button) == HIGH);

        if (!gpio_state && gpio_state_last)
        {
            cnt++;
            std::cout << "Push-button counter: " << cnt <<std::endl;
        }

        gpio_state_last = gpio_state;

        if(async_getchar.wait_for(timeout) == std::future_status::ready)
        {
            async_getchar.get();
            break;
        }
    }

    return 0;
}
