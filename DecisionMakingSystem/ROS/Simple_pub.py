#!/usr/bin/env python    
import rospy
from std_msgs.msg import Float32

def talker():
    newTopic = rospy.Publisher('/truevision/throttle_cmd', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = 1
        rospy.loginfo(hello_str)
        newTopic.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
