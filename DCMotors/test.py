from AMSpi import AMSpi

with AMSpi() as amspi:
    amspi.set_74HC595_pins(21, 20, 16)
    amspi.set_L293D_pins(5, 6, 13, 19)
    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])