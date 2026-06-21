from motor import MotorController
import time

drive = MotorController()

# modify to -1 if one of your wheels spins backwards
drive.set_motor_direction(front_left=1,rear_left=1,front_right=1,rear_right=1)

# this should spin all wheels forward
drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

time.sleep(1)

drive.set_motors(front_left=0,rear_left=0,front_right=0,rear_right=0)
