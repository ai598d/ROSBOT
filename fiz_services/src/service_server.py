#!/usr/bin/env python
import rospy
from fiz_services.srv import WordCount, WordCountResponse

def count_words(request):
	return len(request.words.split()) # return number of words

rospy.init_node('service_server') # a server node

service = rospy.Service( # register service 
	'word_count',  # service name
	WordCount,     # service type
	count_words    # fucntion servicve provide
	)

rospy.spin()
