# ROSBOT: Includes 3 ROS Packages for ME 477 class. 

######  Packages are named after my dog fiz :dog:. 



## fiz_topic
###### Overview 
This is a basic package consists of two nodes (publsiher and sibscriber). 
This package will perform basic integer count.

###### How to run
   - clone to the ros workspace to source directory.
   - use $catkin_make command to build the catkin.
   - source the directory with $ source devel/setup.bash.
   - use $ roslaunch fiz_topic Publisher_subscriber.launch\ from ubuntu terminal.

###### list of src files
   - Publisher_subscriber.launch ( run with roslaunch command. The package will generate integer count )
   - topic_publisher.py (publisher node)
   - topic_subcriber.py (subscriber node)
   
   both nodes are written in python environment. 
   use command $ roscd name_package file_name\ to explore file directory directly from ubuntu terminal. 

## fiz_services
###### Overview 
This is a basic package consists of two nodes (server and client).
Counts words from a input sentence.

###### How to run
   - clone to the ros workspace to source directory.
   - use $catkin_make command to build the catkin.
   - source the directory with $ source devel/setup.bash.
   - use $ roslaunch fiz_topic Publisher_subscriber.launch _inputSentence_\ from ubuntu terminal.

###### list of src files
   - client_server.launch (returns word count of an input sentence. WordCount.srv can be found in srv folder)
   - service_server.py (server node)
   - service_client.py (client node) 
## fiz_actions
###### Overview 
This is a basic package consists of two nodes (server and client).
Performs basic feedback control. 

###### How to run
   - clone to the ros workspace to source directory.
   - use $catkin_make command to build the catkin.
   - source the directory with $ source devel/setup.bash.
   - use $ roslaunch fiz_topic fancy_action.launch\ from ubuntu terminal.
   
###### actions
   - Timer.action
     
     contains timer action input output and feedback message.  
  
###### list of src files
   - fancy_action.launch (package launch file. Performs feedback action)
   - fancy_action_client.py (client node)
   - fancy_action_server.py (server node)

