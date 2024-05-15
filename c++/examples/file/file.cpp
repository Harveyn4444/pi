#include <iostream>
using namespace std;

#include <fstream>
#include <string>

#include <stdlib.h>

double temp;

int main() {

        std::ifstream myfile; myfile.open("/sys/class/thermal/thermal_zone0/temp");
        std::string mystring;

        if (myfile.is_open() ) {
            myfile >> mystring;
            temp = stod(mystring);

            //std::cout << mystring << endl;
            std::cout << temp/1000 << endl;
            
        }

    
}




