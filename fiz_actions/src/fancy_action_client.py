#! /usr/bin/env python
#-----importing different library
import rospy # rospy module import
import time  # time module import
import actionlib # for action

#-----importing fuctions from specefic library
from fiz_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback

def the_feedback_cb(feedback): # feedback callback function
	print('[Feedback] Time elapsed: %f' %
		(feedback.time_elapsed.to_sec()))
	print('[Feedback] Time remaining: %f' %
		(feedback.time_remaining.to_sec()))

rospy.init_node('timer_action_client') # initialize node
client = actionlib.SimpleActionClient( # register client
	'timer',      # action server name
	TimerAction   # action action message
)
client.wait_for_server()       # wait for action server
goal = TimerGoal()             # create goal object 
goal.time_to_wait =rospy.Duration.from_sec(5.0) # set field


# uncomment this line to test server side abort : 
# goal.time_to_wait = rospy.Duration.from_sec(500.0)

client.send_goal(goal, feedback_cb = the_feedback_cb ) # send goal
# uncomment these lines to test goal preemption:
# time.sleep(3.0)
# client.cancel_goal()

client.wait_for_result() # wait for action server to finish
# print results
print('[Result] State: %d' % (client.get_state()))
print('[Result] Status: %s' % (client.get_goal_status_text()))
if client.get_result():
	print('[Result] Time elapsed: %f' %
		(client.get_result().time_elapsed.to_sec()))
	print('[Result] Updates sent: %d' %
		(client.get_result().updates_sent))




