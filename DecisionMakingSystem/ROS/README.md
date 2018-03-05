# ROS

## Steps for using Truevision with ROS (This is all to be done on a Linux machine):

1. Create ROS workspace. Follow tutorial given here: http://wiki.ros.org/catkin/Tutorials/create_a_workspace. And save the scripts in the
   workspace (For example: simple_pub.py, simple_sub.py etc.)
2. Run Truevision and choose desired environment. 
3. Run ROS using 
    > roscore
4. Enable ROS connection in Truevision. Choose autonomous mode if controlling car.
5. Compile your script & and then run it.


## Steps for using Truevision with rosbridge: (Step 1 to 3 has to b done on the Linux device while step 4 is independent of the OS of the device)

1. Run Truevision and choose desired environment.
2. Run rosbridge using:
    > roslaunch rosbridge_server rosbridge_websocket.launch
3. Enable ROS connection in Truevision. Choose autonomous mode if controlling car.
4. Run rosbridge_client.html file (or any other html/javascript client for rosbridge, example given here:        http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality ). Depending on the way the script is written you will be able to 
   send or receive ROS messages. 
  
#### Note: rosbridge can be used to connect to ROS from any device as long as the two devices are on the same LAN. It is a way to connect to ROS using a browser. This functionality provided by rosbridge can be used to make non-ROS programs compatible with ROS.
