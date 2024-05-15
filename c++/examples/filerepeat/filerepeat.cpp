#include <iostream>

using namespace std;

#include <fstream>
#include <string>
#include <stdlib.h>

double temp;

#include <iomanip>
#include <thread>
#include <chrono>
//#include <boost/date_time.hpp>
//namespace bpt = boost::posix_time;
// void f()
// {
//     std::cout << "Called at " << bpt::microsec_clock::local_time().time_of_day() << '\n';
// }

// void caller()
// {
//     for(int n=0; n < 5; ++n) {
//         f();
//         std::this_thread::sleep_for(std::chrono::seconds(1));
//     }
// }

void read(){
    
        std::ifstream myfile; myfile.open("/sys/class/thermal/thermal_zone0/temp");
        std::string mystring;

        if (myfile.is_open() ) {
            myfile >> mystring;
            temp = stod(mystring);

            //std::cout << mystring << endl;
            std::cout << temp/1000 << endl;
            
        }
}

int main()
{
    while(true){

    std::thread thr(read);
    thr.join();


    }
}





