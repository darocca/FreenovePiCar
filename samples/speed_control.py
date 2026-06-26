from motor import MotorController
import time

drive = MotorController()

try:
    cmd = input("enter a speed (-4096 to + 4096) or 'quit' to exit: ")
    while cmd != "quit":
        speed = int(cmd)
        drive.set_motors(speed, speed, speed, speed)
        
except ValueError:
    print("Input is invalid")

finally:
    # stop the motors
    drive.set_motors(0, 0, 0, 0)