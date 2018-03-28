#!/usr/bin/env python
import rospy
import socket
import json
from std_msgs.msg import Float32
 
host = "172.17.54.224" # replace with static IP of pi, this IP was for a lab machine
textport = "5047" # replace with port number to be used

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	x = data.data
	a = {"throttle" : x}
	string = json.dumps(a)
	
	s.sendto(string.encode('utf-8'), server_address)
	    





def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("/Airsim/throttle", Float32, callback)
	
	rospy.spin()

if __name__ == '__main__':
	listener()
