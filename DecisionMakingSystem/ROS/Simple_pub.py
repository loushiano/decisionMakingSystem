'''
 Author - Utkarsh Anand 
This is an example of a simple publisher for ROS for the truevision 
simulator. We are publishing on the topics throttle_cmd and     steering_cmd.
'''
#!/usr/bin/env python    
import rospy
import random
from std_msgs.msg import Float32

def talker():
    newTopic = rospy.Publisher('/truevision/throttle_cmd', Float32, queue_size=10)
    newTopic1 = rospy.Publisher('/truevision/steering_cmd', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 5hz
    a = 0
    while not rospy.is_shutdown():
        a = a+1
        hello_str = 0.1
	
        rospy.loginfo(hello_str)
        newTopic.publish(hello_str)
	if(a ==4):
		rospy.loginfo(0.1)
		newTopic1.publish(0.1)
		
	
	if(a==8):
		rospy.loginfo(-0.1)
		newTopic1.publish(-0.1)
		a = 0
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
