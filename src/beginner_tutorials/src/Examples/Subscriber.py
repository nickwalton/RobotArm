#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#Don't forget to make the node executable chmod +x Subscriber.py

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	
def listener():

	rospy.init_node('listener', anonymous=True) #anonymous=True means that if two nodes of the same name are launched ros will rename one rather than kicking the old one off. 
	
	rospy.Subscriber("chatter", String, callback)
	
	#spin() simply keeps python from exiting until this node is stopped. 
	rospy.spin() 
	
if __name__ == '__main__':
		listener()
