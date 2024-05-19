import serial
import csv
import matplotlib.pyplot as plt
from collections import deque

# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)  # Adjust COM1 to the appropriate port and 9600 to baud rate

# Open CSV file for writing
csv_file = open('/home/harvey/github/plotting/LivePlot/data3.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Number', 'Temperature'])

# Initialize plot
plt.ion()
fig, ax = plt.subplots()

# Create deques for x and y data with maxlen 1000
x_data = deque(maxlen=1000)
y_data = deque(maxlen=1000)

# Plot setup
line, = ax.plot(x_data, y_data)
ax.set_xlabel('Number')
ax.set_ylabel('Temperature')
ax.set_title('Live Serial Data')


# Main loop
try:
    while True:
        # Read data from serial port
        data = ser.readline().decode().strip()
        if data:
            time, value = data.split(',')
            x_data.append(float(time))
            y_data.append(float(value))
            csv_writer.writerow([time, value])
            
            # Update the line with the latest data
            line.set_xdata(x_data)
            line.set_ydata(y_data)

            ax.set_xticks(list(x_data)[::100])
            
            # Rescale the axes if necessary
            ax.relim()
            ax.autoscale_view()
            
            # Redraw the plot
            plt.draw()
            plt.pause(0.001)

except KeyboardInterrupt:
    # Close serial port and CSV file
    ser.close()
    csv_file.close()
