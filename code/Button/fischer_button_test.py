import pytest
from fischer_button import *
import time


def test_is_pressed():
    button1 = FischerButton(button1_pin)
    print("---- TESTING BUTTON 1, PLEASE PRESS AND MANTAIN IT ----")
    time.sleep(2)
    assert button1.isPressed()
    print("---- UNPRESS BUTTON 1 PLEASE ----")
    time.sleep(2)
    assert !(button1.isPressed())

