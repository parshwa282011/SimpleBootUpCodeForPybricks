from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
# You will have to inizitilize your drive base before any of your code like shown bellow
# but first inizitilize your motors
leftMotor  = Motor(Port.A, positive_direction = Direction.CLOCKWISE)
rightMotor = Motor(Port.E, positive_direction = Direction.COUNTERCLOCKWISE)

driveBase  = DriveBase(leftMotor, rightMotor, wheel_diameter = 56, axle_track = 127.5) 
# for drivebase to be more accurate turn on use gyro like bellow
# driveBase.use_gyro(True)

# In your code you will define a main function like below
def main():
    # All of the input of the pybricks drive base
    # for moving straight are going to be in milimeters
    # Just to remember 1 cm = 10 mm
    # Your code for what this program is supposed to do is in here 
    # excluding the functions and a few variables you may define
    driveBase.straight(100)
    print("went straight")
    driveBase.turn(90)
    print("Turned")
    driveBase.straight(100)
    print("went straight")
    driveBase.turn(-90)
    print("Turned")
    driveBase.curve(100,-90)
    print("curved")
    driveBase.turn(-90)
    print("Turned")
    driveBase.straight(200)
    print("went straight")
    # The print functions are just for debugging incase your program doesn't work
    # it is a good way to find out where it breaks
