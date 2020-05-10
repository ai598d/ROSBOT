#!/usr/bin/env python

import rospy # importing functions from rospy
from std_msgs.msg import Int32 # standard msg and int type

# setup: initialize node, register tpic, set rate

rospy.init_node( # initialize node
	'topic_publisher' # node default name 
)
pub = rospy.Publisher(# register topic with roscore
	'counter', # topic name
	 Int32,
	 queue_size =5 #que_size

)

rate = rospy.Rate(2)  # adaptive rate

# loop: publish, count, sleep

count=0

while not rospy.is_shutdown(): # untill ctrl c
	pub.publish(count) # publish count
	count +=1 # increment 
	rate.sleep() # set by rospy.Rate