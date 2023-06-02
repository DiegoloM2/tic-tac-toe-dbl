import RPi.GPIO as GPIO
import time

# Configuration
photoresistor_pin = 22  # Replace with the actual GPIO pin number you used
delay = 0.1  # Delay between readings in seconds
num_readings = 10  # Number of readings to average

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(photoresistor_pin, GPIO.IN)

def read_photoresistor():
    readings = []
    for _ in range(num_readings):
        readings.append(GPIO.input(photoresistor_pin))
        time.sleep(0.05)
    avg_reading = sum(readings) / len(readings)
    
    if avg_reading > 0.5:
        return "Light detected"
    else:
        return "No light detected"

def main_loop():
    try:
        while True:
            result = read_photoresistor()
            print(result)
    except KeyboardInterrupt:
        GPIO.cleanup()

def main():
    setup_gpio()
    main_loop()

if __name__ == '__main__':
    main()
