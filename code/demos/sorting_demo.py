import RPi.GPIO as GPIO
import time

from libraries.Drivers.color_driver.TCS34725_class import TCS34725
from libraries.Drivers.color_driver.color_functions import *

from libraries.Drivers.LDR_driver.LDR_control import *

from libraries.Drivers.servo_driver.servo_control import *

colourSensor = TCS34725()
set_angle(90)

def detect_disk(colourSensor):
    return run_colour_sensor(colourSensor)

def detect_light():
    return read_photoresistor() == 0


def sort_disk(whiteblack):
    set_angle(30)
    time.sleep(5)

def detect_and_sort(colourSensor):
    whiteblack = 0
    while True:
        print(str(detect_light()) + " " + detect_disk(colourSensor))
        if detect_disk(colourSensor) == "White" and detect_light() and whiteblack == 0:
            print("White Disk Detected -> Time To Sort!")

            sort_disk(whiteblack)
            whiteblack = 1
        elif detect_disk(colourSensor) == "White" and detect_light() and whiteblack == 1:
            print("White Disk Detected -> Not Sorting, Looking For Black!")
        elif detect_disk(colourSensor) == "Black" and detect_light() and whiteblack == 1:
            print("Black Disk Detected -> Time To Sort!")
            sort_disk(whiteblack)
            whiteblack = 0
        elif detect_disk(colourSensor) == "Black" and detect_light() and whiteblack == 0:
            print("Black Disk Detected -> Not Sorting, Looking For White!")
        else:
            set_angle(90)
