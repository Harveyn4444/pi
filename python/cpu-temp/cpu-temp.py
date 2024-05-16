from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

plt.ion()
x = []
y = []
i = 0

with open("/home/pi4/github/pi/python/cpu-temp/cpu-temp.csv", "a") as log:
    while True:
        cputemp = CPUTemperature().temperature
        y.append(cputemp)
        i = i + 1
        #x.append(time())
        x.append(i)
        plt.clf()
        plt.scatter(x,y, c="#FF3E00",edgecolors = "none") #edgecolors="#FF3E00")
        plt.plot(x,y, color="#FF3E00")
        plt.pause(0.1)
        plt.draw()
        log.write ("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(cputemp)))
        # print(i,",",cputemp)
        print(f"{i},{cputemp}")
        sleep(0.1)



