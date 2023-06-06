import RPi.GPIO as GPIO
import time

# Initialize GPIO settings (not necessary since pwm will be passed as parameter on call)
# GPIO.setmode(GPIO.BCM)
# servo_pin = 27
# GPIO.setup(servo_pin, GPIO.OUT)
# pwm = GPIO.PWM(servo_pin, 50)
# pwm.start(2.5)

def set_angle(angle, pwm):
    """
    Set the angle of the servo motor.

    Args:
        angle (float): The desired angle of the servo motor (0-180).
    """
    duty_cycle = 2.5 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)




