from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
# You must import your programs here as whon below as an example
import EXAMPLECODE
import EXAMPLECODE2
# You would use this but instead of the name EXAMPLECODE you would put the name of your program
hub = PrimeHub()
# this makes it possible to stop your robot
hub.system.set_stop_button((Button.CENTER,Button.BLUETOOTH))
# The variables
# this is you max number of programs you will have on you spike prime
maxProgramNumber = 2
isProgramChosen = False
buttonsPressed = hub.buttons.pressed()
programNumberSelected = 1
# this part is to decide which program to run
while not isProgramChosen:
    
    buttonsPressed = hub.buttons.pressed()
    hub.display.number(programNumberSelected)
    print(programNumberSelected)
    if Button.CENTER in buttonsPressed:
        isProgramChosen = True
    if Button.RIGHT in buttonsPressed:
        programNumberSelected += 1
        wait(1)
        # The wait is to make sure that it doesn't go on infinitly
    if Button.LEFT in buttonsPressed:
        programNumberSelected -= 1
        wait(1)
    if programNumberSelected > maxProgramNumber:
            programNumberSelected = 1
    if programNumberSelected < 1:
            programNumberSelected = maxProgramNumber
# Here is where you will use functions in your program and call them here
# This is to make it easier to turn off
if programNumberSelected == 1:
    EXAMPLECODE.main()
elif programNumberSelected == 2:
    EXAMPLECODE2.main()
    running = True
    while running:
        # exit the program by holding down the center button
        pass