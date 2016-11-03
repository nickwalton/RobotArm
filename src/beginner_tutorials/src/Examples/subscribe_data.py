#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import numpy as np

a = np.array([])

def callback(data):
	print data
	
	np.append(a,data)
	
	print "a is " 
	print a
		
	np.savetxt("data.csv",a, delimiter = " ", fmt='%10.5f')
	
def listener():

	rospy.init_node('listener', anonymous=True) #anonymous=True means that if two nodes of the same name are launched ros will rename one rather than kicking the old one off. 
	
	rospy.Subscriber("chatter", String, callback)
	
	#spin() simply keeps python from exiting until this node is stopped. 
	rospy.spin() 
	
if __name__ == '__main__':
		listener()
