# ROSBOT: Includes 3 ROS Packages for ME 477 class. 

######  Packages are named after my dog fiz :dog:. 



## fiz_topic
###### Overview 
This is a basic package consists of two nodes (publsiher and sibscriber). use command  <roslaunch fiz_topic Publisher_subscriber.launch> to fire up this package.      

###### list of source files
   - Publisher_subscriber.launch ( run with roslaunch command. The package will generate integer count )
   - topic_publisher.py (publisher node)
   - topic_subcriber.py (subscriber node)
## fiz_services
   - client_server.launch (returns word count of an input sentence. WordCount.srv can be found in srv folder)
   - service_server.py (server node)
   - service_client.py (client node) 
## fiz_actions
   - fancy_action.launch (package launch file. Performs feedback action)
   - fancy_action_client.py (client node)
   - fancy_action_server.py (server node)

