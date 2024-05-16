from gpiozero import CPUTemperature
from time import sleep, strftime, TimeoutError

with open("") as log:


cputemp = CPUTemperature().temperature
print(cputemp)