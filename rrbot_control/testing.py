#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Float64
rospy.init_node("testing")
joint1_pub = rospy.Publisher("/rrbot/joint1_position_controller/command", Float64, queue_size=10)
joint2_pub = rospy.Publisher("/rrbot/joint2_position_controller/command", Float64, queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    t = rospy.Time.now().to_sec()
    joint1_pub.publish(-5.0)
    rate.sleep()