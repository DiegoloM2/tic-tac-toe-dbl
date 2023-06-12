from libraries.Drivers.LDR_driver.LDR_control import read_photoresistor

def detect_x_axis_state(button1: FischerButton, button2: FischerButton, button3: FischerButton) -> int:
    """
    Detects the position of the x-axis system based on the state of three buttons.
    
    Parameters:
        button1 (FischerButton): The first button object representing a position on the x-axis system.
        button2 (FischerButton): The second button object representing a position on the x-axis system.
        button3 (FischerButton): The third button object representing a position on the x-axis system.
    
    Returns:
        int: The position of the x-axis system:
            - 1: If button1 is pressed.
            - 2: If button2 is pressed.
            - 3: If button3 is pressed.
            - -1: If none of the buttons are pressed.
    """
    if button1.isPressed():
        return 1
    elif button2.isPressed():
        return 2
    elif button3.isPressed():
        return 3
    else: 
        return -1

def disk_detected():
    return read_photoresistor()

def check_valid_move(move, board):
    if board[pos - 1] != 0:
        print("Space occupied, try again.")
        return -1
    elif move > 9
