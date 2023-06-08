import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 27

GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)

def set_angle(angle):
    duty_cycle = 2.5 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)