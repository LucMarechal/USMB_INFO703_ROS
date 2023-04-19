#!/usr/bin/env python3

XXXXX  # import rospy
XXXXX  # import Pose message 
XXXXX  # import Twist message
from XXXXX import XXXXX, XXXXX  # import the mathematical functions atan2 and sqrt from the python module called math
import sys

target_x = 0   # initialize the x coordinate of the target
target_y = 0   # initialize the y coordinate of the target
x = 0          # initialize the x coordinate of the turtle
y = 0          # initialize the y coordinate of the turtle
yaw = 0        # initialize the orientation of the turtle


def pose_callback(pose):
    global x, y, yaw

    x = XXXXX
    y = XXXXX
    yaw = XXXXX

    # printout the x and y position of the turtle1 in the consol (just for debugg)
    XXXXXXXXXXXXXXXXX  


def pose_target_callback(pose):
    global target_x
    global target_y

    target_x = XXXXX
    target_y = XXXXX

    # printout the x and y position of the turtle2 in the consol (just for debugg)
    XXXXXXXXXXXXXXXXXX



def turtle_to_target():
    # Initialise the node
    XXXXX

    # Create a subscriber to the turtle1 pose topic
    sub = XXXXX

    # Create a publisher to the turtle1 velocity command
    pub = XXXXX

    rate = rospy.Rate(10) # 10hz
 
    vel = XXXXX # creates a Twist object named vel
    
    while (True):
        K_linear = 0.5

        distance = XXXXX     # Computes the Euclidean distance between current pose and the target
	    
	# printout the distance in the consol (just for debugg)	
	rospy.loginfo("distance = %f\n",distance)

        linear_speed = XXXXX  # computes the velocity of the proportional controller

        K_angular = 4.0
	    steering_angle = XXXXX
	    angular_speed = (steering_angle - yaw) * K_angular

	    vel.linear.x = linear_speed
	    vel.angular.z = angular_speed

	    # publish the value of the velocity for the turtle1
	    XXXXX	

	    if (distance <0.01):  # Explain why we do this
	        break

        rate.sleep()



if __name__ == '__main__':
    try:
        # Create a subscriber to the turtle2 pose topic (our target) in order to find its position
        sub_target = XXXXX

        turtle_to_target()

    except rospy.ROSInterruptException:
        pass
