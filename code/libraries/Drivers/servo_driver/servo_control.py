<<<<<<< HEAD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 17

GPIO.setup(servo_pin, GPIO.OUT)

def set_angle(angle):
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(2.5)
    duty_cycle = 2.5 + (angle / 180) * 10
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    pwm.stop()
=======
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 17

GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)

def set_angle(angle):
    duty_cycle = 2.5 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)
>>>>>>> 6a24591989d0480487449115dfb73ce7efb604dc
