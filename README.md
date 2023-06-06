"# tic-tac-toe-dbl" 
"# tic-tac-toe-dbl" 
- So we have the button folder with functionality for 2 button types, mostly just proof of concept and how they work as reference. Created these two myself.
- We have the color sensor folder with the color sensor class, the color functions that are libraries and then color_sensor.py as a test. The color sensor functions and TCS..._class weren't created by me.
- We have the DC motors folder with AMSpi which is the library and two test files being dc_example.py and test.py. AMSpi wasn't created by me.
- We have the demo folder containing all the "drivers" for the components and 2 demo files 1 for the grid and 1 for the sorting, these two are created by me and should be the files that are most important I reckon
- We have the LCD folder with a file which pretty much can be seen as a library as well, we can just use the lcd_string function from there, the LCD file wasn't created by me.
- We have the LDR folder with simple LDR which is just a way of implementing the LDR, I created this one myself.
- We have the servo folder that has some basic servo control, I created that one as well.
- In the root we have tic_tact_toe.py which was the first version of the algo.


# Testing
The project includes tests to ensure the correctness of its functionality. We use [pytest](https://docs.pytest.org/) as our testing framework. To run the tests, follow these steps:

1. Make sure you have pytest installed. If not, install it using: `pip install pytest`
2. Navigate to the project's root directory.
3. Run the following command to execute the tests: `pytest`
The tests will be discovered and executed, and the test results will be displayed in the console.

