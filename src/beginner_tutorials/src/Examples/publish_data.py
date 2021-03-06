#!/usr/bin/env python

#from sensor_msgs.msg import Imu
#from geometry_msgs.msg import Vector3Stamped

import time
import rospy
from std_msgs.msg import String


def talker(): #Defines the function
	
	#Declares that node is publishing to chatter topic
	pub = rospy.Publisher('chatter', String, queue_size=10) 
		
	#Tells the name of your node, essential to communicate with master
	rospy.init_node('talker') 
		
	#Allows a convenient way to loop at the desired rate. 
	rate = rospy.Rate(10) #10 hz

	# Shuts down if ROS fails
	while not rospy.is_shutdown():

		for i in range(1,9):
			pub.publish(str(i))
		
		#Sleeps the necessary amount to have 10hz 
		rate.sleep()

		

if __name__=='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
			
