#!/usr/bin/env python
import rospy # importing from rsopy package
from std_msgs.msg import Int32 # standrd int type

def callback(msg):  # call back for receiving mssges
	print(msg.data) # printto terminal

rospy.init_node('topic_subscriber') # initialize node

sub = rospy.Subscriber('counter', Int32, callback) # subscribe

rospy.spin() # wait for node to be shutdown



