import RPi.GPIO as GPIO
import time

from libraries.Drivers.color_driver.TCS34725_class import TCS34725
from libraries.Drivers.color_driver.color_functions import *

from libraries.Drivers.LDR_driver.LDR_control import *

from libraries.Drivers.servo_driver.servo_control import *

colourSensor = TCS34725()
set_angle(90)

whiteblack = 0

while True:
    print(str(read_photoresistor()) + " " +run_colour_sensor(colourSensor))
    if run_colour_sensor(colourSensor) == "White" and read_photoresistor() == 0 and whiteblack == 0:
        print("White Disk Detected -> Time To Sort!")
        whiteblack = 1
        set_angle(30)
        time.sleep(5)
    elif run_colour_sensor(colourSensor) == "White" and read_photoresistor() == 0 and whiteblack == 1:
        print("White Disk Detected -> Not Sorting, Looking For Black!")
    elif run_colour_sensor(colourSensor) == "Black" and read_photoresistor() == 0 and whiteblack == 1:
        print("Black Disk Detected -> Time To Sort!")
        whiteblack = 0
        set_angle(30)
        time.sleep(5)
    elif run_colour_sensor(colourSensor) == "Black" and read_photoresistor() == 0 and whiteblack == 0:
        print("Black Disk Detected -> Not Sorting, Looking For White!")
    else:
        set_angle(90)
