import RPi.GPIO as GPIO
import time

button1_pin = 9
button2_pin = 11

class FischerButton():
    def __init__(self, button_pin):
        self.button_pin = button_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def isPressed(self):
        button_state = GPIO.input(self.button_pin)
        if button_state == GPIO.LOW:
            return True
        else:
            return False