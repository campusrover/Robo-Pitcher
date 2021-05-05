#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
import math

def pos(msg):
    global theta
    global theta2
    theta = calc_rads(msg.position[0])
    theta2 = calc_rads(msg.position[1])


rospy.init_node("pitcher")
joint1_pub = rospy.Publisher("/rrbot/joint1_position_controller/command", Float64, queue_size=10)
joint2_pub = rospy.Publisher("/rrbot/joint2_position_controller/command", Float64, queue_size=10)

sub = rospy.Subscriber('/rrbot/joint_states', JointState, pos)

def calc_vel(dist):
    #technically not quite 5
    rad = 2.5
    #note this calculation only works when we launch at 45 degrees, because sin(2*theta) = 1
    #We always launch at 45 degrees because it maximizes the distance travelled by an object at a given speed.
    #Since the speed of the arm is our limiting factor in distance, it makes sense to always launch at 45.
    return (math.sqrt(9.8*dist)/rad)

def calc_rads(pos):
    return pos % (2*(math.pi))

def isclose(a,b,abs_tol = 0.1):
    if abs(a-b) <= abs_tol:
        return True
    else:
        return False


rate = rospy.Rate(10)
theta = 0
theta2 = 0
pi = math.pi
while not rospy.is_shutdown():
    while not isclose(theta,3.1,abs_tol =0.1):
        joint1_pub.publish(1.0)
    joint1_pub.publish(0.0)
    while not isclose(theta2,0,abs_tol =0.1):
        joint2_pub.publish(1.0)
    joint2_pub.publish(0.0)

    print("Please enter the target distance: (to exit, enter anything besides a number)")
    dist = raw_input()
    #checking if input is a float
    try:
        float(dist)
    except ValueError:
        print "exiting!"
        rospy.signal_shutdown("exit")
        rate.sleep()
    print("Thank you! Throwing the ball " + dist + " meters.")
    #5.58505 is 315 degrees in radians, which corresponds to 45 degrees in relation to the ground.
    while not isclose(theta,5.58505,abs_tol =0.1):
        joint1_pub.publish(-calc_vel(float(dist)+0.5))
    joint1_pub.publish(0.0)
    rate.sleep()