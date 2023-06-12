from libraries.Drivers.dc_driver.AMSpi import *
from grid import *
import time
import pytest

amspi = AMSpi()
amspi.set_74HC595_pins(14, 15, 18)
amspi.set_L293D_pins(PWM0B=17, PWM0A=27, PWM2B=22)

def test_resetBoard():
    print("""
        -------------
        TESTING RESET BOARD FUNCTION | 
        you should visually see the grid moving back to it's initial position 
        ---------------
          """)
    reset_board()

def test_position_functions():
    print("""------- Testing Position FUNCTIONS TO ENSURE CORRECTNESS OF PLACING SYSTEM (physical viewer necessary) ------""")

    positionTwo(amspi)
    print("""
        -------------
        TESTING POSITION 2 FUNCTION | 
        you should visually see the lever moving to position 1 in 0.8 seconds
        ---------------
          """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)
    
    positionFour(amspi)
    print("""
        -------------
        TESTING POSITION 3 FUNCTION | 
        you should visually see the lever moving to position 3 in 1.6 seconds
        ---------------
          """)
    reset_board(amspi)
    print("""
        -------------
        TESTING POSITION 4 FUNCTION | 
        you should visually see the grid moving to position 1 in 0.65 seconds
        ---------------
          """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)
    positionFive(amspi)
    print("""
        -------------
        TESTING POSITION 5 FUNCTION | 
        you should visually see the grid moving up for 0.65 seconds
        a 0.1 second rest and the lever moving for 0.8 seconds into position
        ---------------
          """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)

    positionSix(amspi)
    print("""
        -------------
        TESTING POSITION 6 FUNCTION | 
        you should visually see the grid moving up for 0.65 seconds
        a 0.1 second rest and the lever moving for 1.6 seconds into position
        ---------------
          """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)
    
    positionSeven(amspi)
    print("""
        -------------
        TESTING POSITION 7 FUNCTION | 
        you should visually see the grid moving up for 1.3 seconds
        ---------------
    """)
    reset_board(amspi)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")

    positionEight(amspi)
    print("""
        -------------
        TESTING POSITION 8 FUNCTION | 
        you should visually see the grid moving up for 1.3 seconds, 
        followed by a 0.1 second rest and a 0.8 second movement of the lever.
        ---------------
    """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)
    
    positionNine(amspi)
    print("""
        -------------
        TESTING POSITION 7 FUNCTION | 
        you should visually see the grid moving up for 1.3 seconds, 
        followed by a 0.1 second rest and a 1.6 second movement of the lever.
        ---------------
    """)
    print("--- RESETTING BOARD TO INITIAL POSITION ---\n\n")
    reset_board(amspi)
    


def test_makeMove():
    # Simulate the physical movement of disks for each position
    for pos in range(1, 10):
        makeMove(pos, amspi)
        print(f"Disk should be placed in position {pos}")
        print("Verify if the disk falls in the correct position on the physical setup")
        time.sleep(1)
        print("------ PUT DISK BACK INTO CONVEYOR BELT, YOU HAVE 3 SECONDS --------\n\n")
        # Pause for a few seconds to observe the disk before moving to the next position
        time.sleep(3)

    # Cleanup GPIO