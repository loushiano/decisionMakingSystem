# ROS
## Step for using Truevision with ROS (This is all to be done on a Linux machine):

1. Create ROS workspace. Follow tutorial given here: http://wiki.ros.org/catkin/Tutorials/create_a_workspace. And save the scripts in the
   workspace (For example: simple_pub.py, simple_sub.py etc.)
2. Run Truevision and choose desired environment. 
3. Run ROS using 
    > roscore
4. Enable ROS connection in Truevision. Choose autonomous mode if controlling car.
5. Compile your script & and then run it.


## Step for using Truevision with rosbridge:

1. Run Truevision and choose desired environment.
2. Run rosbridge using:
    > roslaunch rosbridge_server rosbridge_websocket.launch
3. Enable ROS connection in Truevision. Choose autonomous mode if controlling car.
4. Run the 
  
