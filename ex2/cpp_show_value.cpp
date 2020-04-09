/**
 ******************************************************************************
 * @file       /ex2/cpp_show_value.cpp
 * @author     Radoslaw Goralewski
 * @version    V1.0
 * @date       24-Mar-2020
 * @brief      Raspberry Pi, Serwer IoT Lab : Exercise 2, C++ program
 ******************************************************************************
 */

#include <iostream>
#include <unistd.h>
#include <fstream>
#include <string>
#include <cstdio>
#include <iomanip>

int main(int argc, char *argv[])
{
    std::cout << "***Values displayer***" << std::endl;

    char temp_unit = '\0';
    bool hum_flag = false;
    bool press_flag = false;

    int arg;

    std::string read_value;

    /* Standard while / switch procedure for ' getopt ' function */
    while ((arg = getopt(argc, argv, "t:hp")) != -1)
    {
        switch(arg)
        {
            case 't':
                temp_unit = *optarg;
                break;
            case 'h':
                hum_flag = true;
                break;
            case 'p':
                press_flag = true;
                break;
            case '?':
                if(optopt == 't')
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

    if (temp_unit != '\0') {
        if (temp_unit != 'C' && temp_unit != 'F') {
            std::cerr << "Wrong temperature unit!" << std::endl;
            return 1;
        }
        else {
            //Read value from file
            std::string line;
            std::ifstream myfile("temperature.dat");
            if (myfile.is_open())
            {
                //Read first line
                getline(myfile, line);
                read_value = line;
                myfile.close();
            }

            //Dispay according to selected unit
            if (temp_unit == 'C') {
                std::cout << "Temperature: " << read_value << std::endl;
            }
            else if (temp_unit == 'F') {
                int pos = read_value.find("C");
                std::string sub = read_value.substr(0, pos);
                float temp_celsius = std::stof(sub);
                float temp_fahrenheit = temp_celsius * 1.8 + 32.0;
                std::cout << "Temperature: " << std::fixed << std::setprecision(1) << temp_fahrenheit << "F" << std::endl;
            }
        }
    }

    if (hum_flag) {
        //Read value from file
        std::string line;
        std::ifstream myfile("humidity.dat");
        if (myfile.is_open())
        {
            //Read first line
            getline(myfile, line);
            read_value = line;
            std::cout << "Humidity: " << line << std::endl;
            myfile.close();
        }
    }

    if (press_flag) {
        //Read value from file
        std::string line;
        std::ifstream myfile("pressure.dat");
        if (myfile.is_open())
        {
            //Read first line
            getline(myfile, line);
            read_value = line;
            std::cout << "Pressure: " << line << std::endl;
            myfile.close();
        }
    }

    return 0;
}
