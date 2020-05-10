#!/usr/bin/env/ python
import rospy
from fiz_services.srv import WordCount
import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_count') # wait for registration

word_counter = rospy.ServiceProxy( # setup proxy

	'word_count', # service name
	 WordCount    # service type

)

words = ''.join(sys.argv[1:]) # parse args

word_count = word_counter(words) # use service

print (words+'--> has '+str(word_count.count)+'words') 