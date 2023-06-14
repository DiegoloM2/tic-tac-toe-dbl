from libraries.Sorting.sorting import Sorting
from libraries.Drivers.color_driver.TCS34725_class import TCS34725
import time

sorter = Sorting()

def test_detect_white_disk():
    # Set up the necessary objects or sensors for testing
    print("--- TESTING THE DETECT_DISK FUNCTION ---")
    print("PLACE A WHITE DISK IN THE BELT FOR THE SENSOR TO DETECT, YOU HAVE 10 SECONDS")
    time.sleep(10)
    result = sorter.detect_disk()

    # Compare the result with the expected outcome
    assert result == "White"

def test_detect_black_disk():
    # Set up the necessary objects or sensors for testing
    colourSensor = TCS34725()
    print("--- TESTING THE DETECT_DISK FUNCTION ---")
    print("PLACE A BLACK DISK IN THE BELT FOR THE SENSOR TO DETECT, YOU HAVE 10 SECONDS")
    time.sleep(10)
    result = sorter.detect_disk()

    # Compare the result with the expected outcome
    assert result == "Black"

def test_sort_disk():
    print("--- TESTING THE SORT DISK FUNCTION ---")
    print("PUT A DISK ON THE SERVOMOTOR FOR IT TO BE PUSHED, YOU HAVE 10 SECONDS")
    time.sleep(10)
    print("YOU SHOULD SEE THE SERVOMOTOR TURN TO AN ANGLE OF ~30 DEGREES TO PUSH THE DISK FOLLOWED BY 5 SECONDS OF INACTIVITY")
    sorter.sort_disk()
    
test_detect_white_disk()
test_detect_black_disk()
test_sort_disk()