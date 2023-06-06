from servo_control import set_angle
import RPi.GPIO as GPIO
import pytest

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
servo_pin = 27
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)

def test_set_angle():
    """
    Test the set_angle function by setting the servo angle to 30 and 90 degrees.
    """
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(2.5)
    
    # Check that set_angle rotates servomotor through pwm.get_duty_cycle()
    set_angle(30, pwm)
    assert abs(pwm.get_duty_cycle() - 7.5) < 0.01

    # Tester needs to confirm he has seen the servo motor move.
    visible_proof = input("Did the servo motor move an angle of ~30 degrees? (y/n)")
    assert visible_proof == "y"

    set_angle(90, pwm)
    assert abs(pwm.get_duty_cycle() - 12.5) < 0.01

    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        test_set_angle()
    except KeyboardInterrupt:
        GPIO.cleanup()