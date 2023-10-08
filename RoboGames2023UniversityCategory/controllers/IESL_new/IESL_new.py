"""IESL_new controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard
import time

if __name__ == "__main__":
    
    
    # create the Robot instance.
    robot = Robot()
    kb = Keyboard()

    # get the time step of the current world.
    timestep = 64
    MAX_SPEED = -10.0

    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    f_l = robot.getDevice('front_left')
    f_r = robot.getDevice('front_right')
    b_l = robot.getDevice('left_back')
    b_r = robot.getDevice('right_back')

    a_h = robot.getDevice('virtical_arm')
    a_h.setPosition(0.0)
    l_p = 0.0

    h_r = robot.getDevice('horizontal_right')
    h_r.setPosition(0.0)
    h_r_p = 0.0
    h_l = robot.getDevice('horizontal_left')
    h_l.setPosition(0.0)
    h_l_p = 0.0

    f_l.setPosition(float('inf'))
    f_l.setVelocity(0.0)

    f_r.setPosition(float('inf'))
    f_r.setVelocity(0.0)

    b_l.setPosition(float('inf'))
    b_l.setVelocity(0.0)

    b_r.setPosition(float('inf'))
    b_r.setVelocity(0.0)
    
    def grab():
        while True:
            global h_r_p
            global h_l_p
            h_r_p -= 0.005
            h_l_p += 0.005
            if h_r_p <= -0.115 or h_l_p >= 0.115:
                break
            h_r.setPosition(h_r_p)
            h_l.setPosition(h_l_p)
            #time.sleep(0.1)
    
        while True:
            global l_p 
            l_p += 0.001
            if l_p >= 0.55:
                break
            a_h.setPosition(l_p)
            #time.sleep(0.1)
        
    def drop():
        while True:
            global h_r_p
            global h_l_p
            h_r_p += 0.005
            h_l_p -= 0.005
            if h_r_p >= 0.0 or h_l_p <= 0.0:
                break
            h_r.setPosition(h_r_p)
            h_l.setPosition(h_l_p)
        while True:
            global l_p
            l_p -= 0.01
            if l_p < 0.03:
                break
            a_h.setPosition(l_p)
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()

        # Process sensor data here.

        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)

        l_s = 0.0
        r_s = 0.0
        key = kb.getKey()
        if (key == 315):
            r_s = MAX_SPEED
            l_s = MAX_SPEED
        elif key == 317:
            r_s = -MAX_SPEED
            l_s = -MAX_SPEED
        elif key == 316:
            r_s = -MAX_SPEED
            l_s = MAX_SPEED
        elif key == 314:
            r_s = MAX_SPEED
            l_s = -MAX_SPEED
        else:
            r_s = 0.0
            l_s = 0.0

        if (key == 87):
            grab()
        elif key == 83:
            drop()
        elif key == 65:
            h_r_p -= 0.005
            h_l_p += 0.005
            if h_r_p <= -0.115 or h_l_p >= 0.115:
                h_r_p = -0.115
                h_l_p = 0.115

        elif key == 68:
            h_r_p += 0.005
            h_l_p -= 0.005
            if h_r_p >= 0.0 or h_l_p <= 0.0:
                h_r_p = 0.0
                h_l_p = 0.0
        else:
            l_p += 0
            h_r_p += 0
            h_l_p += 0
            
        

        
        #h_r.setPosition(h_r_p)
        #h_l.setPosition(h_l_p)

        f_l.setVelocity(l_s)
        f_r.setVelocity(r_s)
        b_l.setVelocity(l_s)
        b_r.setVelocity(r_s)

        pass

    # Enter here exit cleanup code.
