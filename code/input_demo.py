import RPi.GPIO as GPIO
import time
import libraries.Drivers.LCD_driver.lcd_16x2 as lcd_16x2
from libraries.Drivers.Button_driver.default_button import Button


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

button_pin = 27
confirm_pin = 22

counter_button = Button(button_pin)
confirm_button = Button(confirm_pin)

count = 1
last_press_time = 0
debounce_delay = 0.4
confirm_pressed = False
confirmed = False



def cleanup():
    GPIO.cleanup()
    
    
def enterNumber(limit):
    count = 0
    last_press_time = 0
    debounce_delay = 0.4
    confirm_pressed = False
    confirmed = False
    
    while True:
        # Check if the button is pressed
        if counter_button.isPressed():
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Button Pressed!")
                count += 1
                
                # Reset the count if it exceeds 9
                if count > 9:
                    count = 1
                print("Count: ", count)
                
                # Update LCD display with button press information
                lcd_16x2.lcd_string("Button Pressed!", LCD_LINE_1)
                lcd_16x2.lcd_string("Count: {}".format(count), LCD_LINE_2)
                
                last_press_time = current_time
                confirmed = False

        # Check if the confirm button is pressed
        elif confirm_button.isPressed():
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Confirm Button Pressed!")
                
                # Check if the button press is confirmed
                if not confirmed:
                    confirmed = True
                    print("Confirmed! Count is:", count)
                    
                    # Update LCD display with confirmation message and count
                    lcd_16x2.lcd_string("Confirmed!", LCD_LINE_1)
                    lcd_16x2.lcd_string("Count is: {}".format(count), LCD_LINE_2)
                    
                    # Perform additional actions here
                    
                last_press_time = current_time

    
    

    

def main():
    """
    Entry point of the program.
    """
    global last_press_time, count, confirmed
    lcd_16x2.main()
    
    while True:
        # Check if the button is pressed
        if GPIO.input(button_pin) == GPIO.LOW:
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Button Pressed!")
                count += 1
                
                # Reset the count if it exceeds 9
                if count > 9:
                    count = 1
                print("Count: ", count)
                
                # Update LCD display with button press information
                lcd_16x2.lcd_string("Button Pressed!", LCD_LINE_1)
                lcd_16x2.lcd_string("Count: {}".format(count), LCD_LINE_2)
                
                last_press_time = current_time
                confirmed = False

        # Check if the confirm button is pressed
        elif GPIO.input(confirm_pin) == GPIO.LOW:
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Confirm Button Pressed!")
                
                # Check if the button press is confirmed
                if not confirmed:
                    confirmed = True
                    print("Confirmed! Count is:", count)
                    
                    # Update LCD display with confirmation message and count
                    lcd_16x2.lcd_string("Confirmed!", LCD_LINE_1)
                    lcd_16x2.lcd_string("Count is: {}".format(count), LCD_LINE_2)
                    
                    # Perform additional actions here
                    
                last_press_time = current_time


try:												
    main()
except KeyboardInterrupt:
    cleanup()
