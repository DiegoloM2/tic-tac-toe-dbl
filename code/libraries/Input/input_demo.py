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
    
def output_text(text):
    """
    Displays text message on the 16x2 LCD screen.

    Args:
        text (str): The text message to be displayed.

    """
    lcd_16x2.main()
    
    # Display the first 16 characters of the text on the first line of the LCD screen
    lcd_16x2.lcd_string(text[:16], LCD_LINE_1)
    
    # If the text length exceeds 16 characters, display the remaining text on the second line
    if len(text) > 16:
        lcd_16x2.lcd_string(text[16:], LCD_LINE_2)

    
    
def input_number(limit):
    """
    Reads and returns a number input from the user within the specified limit.

    Args:
        limit (int): The upper limit for the input number.

    Returns:
        int: The number input by the user.

    """
    count = 0
    last_press_time = 0
    debounce_delay = 0.4
    lcd_16x2.main()
    lcd_16x2.lcd_string(f"Black ADDS", LCD_LINE_1)
    lcd_16x2.lcd_string(f"Red CONFIRMS", LCD_LINE_2)
    time.sleep(1)
    lcd_16x2.lcd_string(f"Enter number <={limit}", LCD_LINE_1)
    lcd_16x2.lcd_string(f"", LCD_LINE_2)

    while True:
        if counter_button.isPressed():
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Button Pressed!")
                count += 1
                
                # Reset the count if it exceeds the limit
                if count > limit:
                    count = 1

                # Update LCD display with button press information
                lcd_16x2.lcd_string(f"  {count}", LCD_LINE_2)
                
                last_press_time = current_time
                confirmed = False

        # Check if the confirm button is pressed
        elif confirm_button.isPressed():
            current_time = time.time()
            
            # Apply debounce delay to avoid multiple button presses
            if current_time - last_press_time > debounce_delay:
                print("Confirm Button Pressed!")
                last_press_time = current_time
                return count

    