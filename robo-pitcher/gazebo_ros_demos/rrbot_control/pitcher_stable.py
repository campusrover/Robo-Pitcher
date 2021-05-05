#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
import math

def pos(msg):
    global theta
    theta = msg.position[0]

rospy.init_node("pitcher")
joint1_pub = rospy.Publisher("/rrbot/joint1_position_controller/command", Float64, queue_size=10)
joint2_pub = rospy.Publisher("/rrbot/joint2_position_controller/command", Float64, queue_size=10)

sub = rospy.Subscriber('/rrbot/joint_states', JointState, pos)

def calc_vel(dist):
    rad = 2.5
    #note this calculation only works when we launch at 45 degrees, because sin(2*theta) = 1
    #We always launch at 45 degrees because it maximizes the distance travelled by an object at a given speed.
    #Since the speed of the arm is our limiting factor in distance, it makes sense to always launch at 45.
    return (math.sqrt(9.8*dist)/rad)


rate = rospy.Rate(10)
theta = 0
pi = math.pi
while not rospy.is_shutdown():
    while theta % (2*pi) < (pi - 0.2) or theta % (2*pi) > pi:
        joint1_pub.publish(2.0)
        joint2_pub.publish(0.0)
    joint1_pub.publish(0.0)
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
    #0.785398 is the raidan equivalent to 45 degrees
    while theta % (2*pi) > 0.785398:
        joint1_pub.publish(-calc_vel(float(dist)+1.2))
    joint1_pub.publish(5.0)
    rate.sleep()