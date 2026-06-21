import time
from pca9685 import PCA9685

class MotorController:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.set_pwm_freq(50)
    def duty_range(self, duty1, duty2, duty3, duty4):
        if duty1 > 4095:
            duty1 = 4095
        elif duty1 < -4095:
            duty1 = -4095        
        if duty2 > 4095:
            duty2 = 4095
        elif duty2 < -4095:
            duty2 = -4095  
        if duty3 > 4095:
            duty3 = 4095
        elif duty3 < -4095:
            duty3 = -4095
        if duty4 > 4095:
            duty4 = 4095
        elif duty4 < -4095:
            duty4 = -4095
        return duty1,duty2,duty3,duty4
    def left_upper_wheel(self,duty):
        if duty>0:
            self.pwm.set_motor_pwm(0,0)
            self.pwm.set_motor_pwm(1,duty)
        elif duty<0:
            self.pwm.set_motor_pwm(1,0)
            self.pwm.set_motor_pwm(0,abs(duty))
        else:
            self.pwm.set_motor_pwm(0,4095)
            self.pwm.set_motor_pwm(1,4095)
    def left_lower_wheel(self,duty):
        if duty>0:
            self.pwm.set_motor_pwm(3,0)
            self.pwm.set_motor_pwm(2,duty)
        elif duty<0:
            self.pwm.set_motor_pwm(2,0)
            self.pwm.set_motor_pwm(3,abs(duty))
        else:
            self.pwm.set_motor_pwm(2,4095)
            self.pwm.set_motor_pwm(3,4095)
    def right_upper_wheel(self,duty):
        if duty>0:
            self.pwm.set_motor_pwm(6,0)
            self.pwm.set_motor_pwm(7,duty)
        elif duty<0:
            self.pwm.set_motor_pwm(7,0)
            self.pwm.set_motor_pwm(6,abs(duty))
        else:
            self.pwm.set_motor_pwm(6,4095)
            self.pwm.set_motor_pwm(7,4095)
    def right_lower_wheel(self,duty):
        if duty>0:
            self.pwm.set_motor_pwm(4,0)
            self.pwm.set_motor_pwm(5,duty)
        elif duty<0:
            self.pwm.set_motor_pwm(5,0)
            self.pwm.set_motor_pwm(4,abs(duty))
        else:
            self.pwm.set_motor_pwm(4,4095)
            self.pwm.set_motor_pwm(5,4095)

    def set_motor_model(self, duty1, duty2, duty3, duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.left_upper_wheel(duty1*self.dir1)
        self.left_lower_wheel(duty2*self.dir2)
        self.right_upper_wheel(duty3*self.dir3)
        self.right_lower_wheel(duty4*self.dir4)

    def set_motors(self, front_left=0, rear_left=0, front_right=0, rear_right=0):
        self.set_motor_model(front_left, rear_left, front_right, rear_right)

    def set_motor_direction(self, front_left=1,rear_left=1,front_right=1,rear_right=1):
        self.dir1 = front_left
        self.dir2 = rear_left
        self.dir3 = front_right
        self.dir4 = rear_right

    def close(self):
        self.set_motor_model(0,0,0,0)
        self.pwm.close()

if __name__=='__main__':
    PWM = MotorController()          
    try:
        PWM.set_motors(front_left=2000,rear_left=2000,front_right=2000,rear_right=2000)       #Forward
        time.sleep(1)
        PWM.set_motors(front_left=-2000,rear_left=-2000,front_right=-2000,rear_right=-2000)   #Back
        time.sleep(1)
        PWM.set_motors(front_left=-2000,rear_left=-2000,front_right=2000,rear_right=2000)     #Left 
        time.sleep(1)
        PWM.set_motors(front_left=2000,rear_left=2000,front_right=-2000,rear_right=-2000)     #Right    
        time.sleep(1)
        PWM.set_motor_model(0,0,0,0)                   #Stop
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        PWM.close()

