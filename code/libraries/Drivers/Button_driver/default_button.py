import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Button():
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pin = pin
    def isPressed(self):
        return GPIO.input(button_pin) == GPIO.LOW
