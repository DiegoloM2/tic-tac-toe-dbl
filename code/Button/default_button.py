import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button_pin = 26

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def count_button(channel):
    counter = 1
    while True:
        print(counter)
        counter += 1
        if counter > 9:
            counter = 1
        time.sleep(0.1)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=count_button, bouncetime=300)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user")
    GPIO.cleanup()
