import color_functions
import TCS34725_class

colourSensor = TCS34725()

while True:
    print(run_color_sensor(colourSensor))