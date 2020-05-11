# ROSBOT: Includes 3 ROS Packages for ME 477 class. 

######  Packages are named after my dog fiz :dog:. 

## Breif description of each packages are given below.
######  fiz_topic (src file list).
   - Publisher_subscriber.launch ( run with roslaunch command. The package will generate integer count )
   - topic_publisher.py (publisher node)
   - topic_subcriber.py (subscriber node)
######  fiz_services
   - client_server.launch (returns word count of an input sentence. WordCount.srv can be found in srv folder)
   - service_server.py (server node)
   - service_client.py (client node) 
######  fiz_actions
   - fancy_action.launch (package launch file. Performs feedback action)
   - fancy_action_client.py (client node)
   - fancy_action_server.py (server node)

