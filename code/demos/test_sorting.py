import pytest
from sorting_demo import detect_disk, sort_disk, run_colour_sensor, TCS34725
import time

def test_detect_white_disk():
    # Set up the necessary objects or sensors for testing
    colourSensor = TCS34725()
    print("--- TESTING THE DETECT_DISK FUNCTION ---")
    print("PLACE A WHITE DISK IN THE BELT FOR THE SENSOR TO DETECT, YOU HAVE 2 SECONDS")
    time.sleep(2)
    result = detect_disk(colourSensor)

    # Compare the result with the expected outcome
    assert result == "White"

def test_detect_black_disk():
    # Set up the necessary objects or sensors for testing
    colourSensor = TCS34725()
    print("--- TESTING THE DETECT_DISK FUNCTION ---")
    print("PLACE A BLACK DISK IN THE BELT FOR THE SENSOR TO DETECT, YOU HAVE 2 SECONDS")
    time.sleep(2)
    result = detect_disk(colourSensor)

    # Compare the result with the expected outcome
    assert result == "Black"

def test_sort_disk():
    print("--- TESTING THE SORT DISK FUNCTION ---")
    print("PUT A DISK ON THE SERVOMOTOR FOR IT TO BE PUSHED, YOU HAVE 2 SECONDS")
    time.sleep(2)
    print("YOU SHOULD SEE THE SERVOMOTOR TURN TO AN ANGLE OF ~30 DEGREES TO PUSH THE DISK FOLLOWED BY 5 SECONDS OF INACTIVITY")
    sort_disk(0)
