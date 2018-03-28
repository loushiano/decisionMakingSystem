#!/usr/bin/env python

import rospy
import socket, sys, time, json
from std_msgs.msg import Float32

textport = "5048"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ("", port)
s.bind(server_address)

def talker():
    pub = rospy.Publisher('/Airsim/steering', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        buf, address = s.recvfrom(2048)
        if not len(buf):
            break
        data = json.loads(buf)
        hello_str = data["steering"]
        
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass