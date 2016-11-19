#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from keyboard.msg import Key
import time

#Don't forget to make the node executable chmod +x Subscriber.py


class RobotArm():
	def __init__(self):
		self.servo0 = rospy.Publisher("/servo0", UInt16, queue_size=1)
		self.servo1 = rospy.Publisher("/servo1", UInt16, queue_size=1)
		self.servo2 = rospy.Publisher("/servo2", UInt16, queue_size=1)
		self.servo3 = rospy.Publisher("/servo3", UInt16, queue_size=1)
		self.servo4 = rospy.Publisher("/servo4", UInt16, queue_size=1)
		
		self.pos_servo_0 = 90
		self.pos_servo_1 = 90
		self.pos_servo_2 = 90
		self.pos_servo_3 = 90
		self.pos_servo_4 = 90
		
		
		rospy.init_node('arm_command', anonymous=True)
		
	def update_servo(self, servo, pos):
	
		rate = rospy.Rate(2000)
		if servo == 0:
			self.servo0.publish(pos)
			self.pos_servo_0 = pos
		
		if servo == 1:
			self.servo1.publish(pos)
			self.pos_servo_1 = pos
			
		if servo == 2:
			self.servo2.publish(pos)
			self.pos_servo_2 = pos
			
		if servo == 3:
			self.servo3.publish(pos)
			self.pos_servo_3 = pos
			
		if servo == 4:
			self.servo4.publish(pos)
			self.pos_servo_4 = pos
		
	# Changes position of arm based on keyboard presses 
	def callback(self,data):
	
		#Servo 0
		if data.code == 97: #If a is pressed
			self.pos_servo_0 = self.pos_servo_0+2
			my_arm.update_servo(0, self.pos_servo_0)
			
		if data.code == 100: #If d is pressed
			self.pos_servo_0 = self.pos_servo_0-2
			my_arm.update_servo(0, self.pos_servo_0)
			
		#Servo 1
		if data.code == 119: #If w is pressed
			self.pos_servo_1 = self.pos_servo_1-2
			my_arm.update_servo(1, self.pos_servo_1)
			
		if data.code == 115: #If s is pressed
			self.pos_servo_1 = self.pos_servo_1+2
			my_arm.update_servo(1, self.pos_servo_1)
			
		#Servo 2
		if data.code == 117: #If u is pressed
			self.pos_servo_2 = self.pos_servo_2-2
			my_arm.update_servo(2, self.pos_servo_2)
			
		if data.code == 106: #If j is pressed
			self.pos_servo_2 = self.pos_servo_2+2
			my_arm.update_servo(2, self.pos_servo_2)
			
		#Servo 3+4
		if data.code == 32: #If space is pressed
			self.pos_servo_3 = self.pos_servo_3+2
			my_arm.update_servo(3, self.pos_servo_3)
			self.pos_servo_4 = self.pos_servo_4+2
			my_arm.update_servo(4, self.pos_servo_4)
			
		if data.code == 304: #If shift is pressed
			self.pos_servo_3 = self.pos_servo_3-2
			my_arm.update_servo(3, self.pos_servo_3)
			self.pos_servo_4 = self.pos_servo_4-2
			my_arm.update_servo(4, self.pos_servo_4)
			
		#Servo 4
		if data.code == 104: #If h is pressed
			self.pos_servo_4 = self.pos_servo_4-2
			my_arm.update_servo(4, self.pos_servo_4)
			
		if data.code == 107: #If k is pressed
			self.pos_servo_4 = self.pos_servo_4+2
			my_arm.update_servo(4, self.pos_servo_4)
			
				
			
		#Code to keep values betwen 0 and 180
		
		#Servo 0
		if self.pos_servo_0 <= 2:
			self.pos_servo_0 == 4;
		if self.pos_servo_0 == 180:
			self.pos_servo_0 == 178;
			
		#Servo 1
		if self.pos_servo_1 <= 2:
			self.pos_servo_1 == 4;
		if self.pos_servo_1 >= 178:
			self.pos_servo_1 == 176;
			
		#Servo 2
		if self.pos_servo_2 == 0:
			self.pos_servo_2 == 2;
		if self.pos_servo_2 == 180:
			self.pos_servo_2 == 178;
			
		#Servo 3
		if self.pos_servo_3 == 0:
			self.pos_servo_3 == 2;
		if self.pos_servo_3 == 180:
			self.pos_servo_3 == 178;
			
		#Servo 4
		if self.pos_servo_4 == 0:
			self.pos_servo_4 == 2;
		if self.pos_servo_4 == 180:
			self.pos_servo_4 == 178;
	
	
	
		
		
	
	def listener(self):
	
		print "Got to subscriber"
		rospy.Subscriber("/keyboard/keydown", Key, self.callback)
	
		#spin() simply keeps python from exiting until this node is stopped. 
		rospy.spin() 
	
if __name__ == '__main__':
	my_arm = RobotArm()
	
	my_arm.update_servo(0, 90)
	my_arm.update_servo(1,70)
	my_arm.update_servo(2,90)
	my_arm.update_servo(3, 90)
	my_arm.update_servo(4, 90)
	
	my_arm.listener()
	
	
	
