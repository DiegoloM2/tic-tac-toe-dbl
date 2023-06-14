import RPi.GPIO as GPIO
import time
import libraries.Drivers.LCD_driver.lcd_16x2 as lcd_16x2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

button_pin = 17
confirm_pin = 27

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(confirm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1
last_press_time = 0
debounce_delay = 0.4
confirm_pressed = False
confirmed = False

def cleanup():
    GPIO.cleanup()

def main():
    global last_press_time, count
    lcd_16x2.main()
    
    
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            current_time = time.time()
            if current_time - last_press_time > debounce_delay:
                print("Button Pressed!")
                count += 1
                if count > 9:
                    count = 1
                print("Count: ", count)
                lcd_16x2.lcd_string("Button Pressed!", LCD_LINE_1)
                lcd_16x2.lcd_string("Count: {}".format(count), LCD_LINE_2)
                last_press_time = current_time
                confirmed = False

        elif GPIO.input(confirm_pin) == GPIO.LOW:
            current_time = time.time()
            if current_time - last_press_time > debounce_delay:
                print("Confirm Button Pressed!")
                if not confirmed:
                    confirmed = True
                    print("Confirmed! Count is:", count)
                    lcd_16x2.lcd_string("Confirmed!", LCD_LINE_1)
                    lcd_16x2.lcd_string("Count is: {}".format(count), LCD_LINE_2)
                    # Perform additional actions here
                last_press_time = current_time

try:
    main()
except KeyboardInterrupt:
    cleanup()
