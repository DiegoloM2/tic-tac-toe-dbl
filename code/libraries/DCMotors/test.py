import RPi.GPIO as GPIO
from AMSpi import AMSpi
import time

with AMSpi() as amspi:
    amspi.set_74HC595_pins(14, 15, 18)
    amspi.set_L293D_pins(16, 17, 27, 22)
    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
    time.sleep(3)
    amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])