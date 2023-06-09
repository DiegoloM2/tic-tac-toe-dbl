<<<<<<< HEAD:code/libraries/Sorting/sorting.py
import RPi.GPIO as GPIO
import time

from libraries.Drivers.color_driver.TCS34725_class import TCS34725
from libraries.Drivers.color_driver.color_functions import *
from libraries.Drivers.servo_driver.servo_control import *


class Sorting():
    def __init__(self):
        # Last disk represents the last disk's color (0 if black, 1 if white)
        self.lastDisk = 0
        self.colorSensor = TCS34725()
        set_angle(0)

    def detect_disk(self,):
        return run_colour_sensor(self.colorSensor)
    def sort_disk(self):
        print("---- SORTING DISK ----")
        time.sleep(1.5)
        set_angle(30)
        time.sleep(1)
        set_angle(0)
        print("---- DISK SORTED ----\n")


    def timeToSort(self, ):
        if self.detect_disk() == "White" and self.lastDisk == 0:
            print("White Disk Detected -> Time To Sort!")
            self.lastDisk = 1
            return True
        elif self.detect_disk() == "Black" and self.lastDisk == 1:
            print("Black Disk Detected -> Time To Sort!")
            self.lastDisk = 0
            return True
        elif self.detect_disk() == "Black" and self.lastDisk == 0:
            print("Black Disk Detected -> Not Sorting, Looking For White!")
            return False
        elif self.detect_disk() == "White" and self.lastDisk == 1:
            print("White Disk Detected -> Not Sorting, Looking for Black!")
            return False
        return False




=======
import RPi.GPIO as GPIO
import time

from libraries.Drivers.color_driver.TCS34725_class import TCS34725
from libraries.Drivers.color_driver.color_functions import *
from libraries.Drivers.servo_driver.servo_control import *


class Sorting():
    def __init__(self):
        # Last disk represents the last disk's color (0 if black, 1 if white)
        self.lastDisk = 0
        self.colorSensor = TCS34725()
        set_angle(90)

    def detect_disk(self,):
        return run_colour_sensor(self.colorSensor)
    def sort_disk(self):
        set_angle(30)
        time.sleep(5)
        set_angle(90)

    def timeToSort(self, ):
        if self.detect_disk() == "White" and self.lastDisk == 0:
            print("White Disk Detected -> Time To Sort!")
            lastDisk = 1
            return True
        elif self.detect_disk() == "Black" and self.lastDisk == 1:
            print("Black Disk Detected -> Time To Sort!")
            lastDisk = 0
            return True
        elif self.detect_disk() == "Black" and self.lastDisk == 0:
            print("Black Disk Detected -> Not Sorting, Looking For White!")
            return False
        elif self.detect_disk() == "White" and self.lastDisk == 1:
            print("White Disk Detected -> Not Sorting, Looking for Black!")
            return False
        return False




>>>>>>> 6a24591989d0480487449115dfb73ce7efb604dc:code/implementation/sorting.py
