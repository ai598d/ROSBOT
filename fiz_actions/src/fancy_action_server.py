#! /usr/bin/env python
#-----importing different library
import rospy # rospy module import
import time  # time module import
import actionlib # for action

#-----importing fuctions from specefic library
from fiz_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback

#----creating do timer function
def do_timer(goal): # action function definition
	start_time = time.time()  # assign a starting time
	update_count =0
	if goal.time_to_wait.to_sec() > 60.0: #check req duration
		result = TimerResult()
		result.time_elapsed= rospy.Duration.from_sec(
			time.time() - start_time)
		result.updates_sent = update_count
		server.set_aborted(result, "Aborted: t00 long to wait")
		return #too long of  requested wait  
	while(time.time()-start_time)< goal.time_to_wait.to_sec():
		# waiting to meet wait duration
		if server.is_preempt_requested(): # check preemption
			result = TimerResult()
			result.time_elapsed = rospy.Duration.from_sec(
				time.time() - start_time)
			result.updates_sent = update_count
			server.set_preempted(result, "Timer preempted")
			return
		feedback = TimerFeedback()
		feedback.time_elapsed = rospy.Duration.from_sec(
			time.time() - start_time )
		feedback.time_remaining= \
			goal.time_to_wait - feedback.time_elapsed
		server.publish_feedback(feedback)
		update_count +=1
		time.sleep(1.0)
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(
		time.time() - start_time)
	result.updates_sent = update_count
	server.set_succeeded(result,"Timer completed successfully")

rospy.init_node('timer_action_server') #initialzie node
server = actionlib.SimpleActionServer(
	'timer', TimerAction, do_timer, False
	)
server.start()
rospy.spin()




