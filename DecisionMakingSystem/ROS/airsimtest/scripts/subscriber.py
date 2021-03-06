#!/usr/bin/env python
import rospy
import socket, sys, time, json

from std_msgs.msg import Float32

textport = "5047"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ("", port)
s.bind(server_address)

def talker():
	newTopic = rospy.Publisher('/truevision/steering_cmd', Float32, queue_size=10)
	newTopic1 = rospy.Publisher('/truevision/throttle_cmd', Float32, queue_size=10)
	
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) #10hz
	while True:
		buf, address = s.recvfrom(2048)
		if not len(buf):
			break
		data = json.loads(buf)
		hello_str = data["steering"]
		rospy.loginfo(hello_str)
		newTopic1.publish(0.1)
		newTopic.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
		