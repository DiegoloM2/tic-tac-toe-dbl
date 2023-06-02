import RPi.GPIO as GPIO
import time

button_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button_state = GPIO.input(button_pin)
    if button_state == GPIO.LOW:
        print("Button pressed!")
        time.sleep(1)
    else:
        print("Button not pressed!")
        time.sleep(1)