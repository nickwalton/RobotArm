/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */
 
 /*
   To begin publishing run this command:
   rosrun rosserial_python serial_node.py /dev/ttyACM0
   
 
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void servo_cb0( const std_msgs::UInt16& cmd_msg){
  servo0.write(cmd_msg.data); //set servo angle, should be from 0-180  
}
void servo_cb1( const std_msgs::UInt16& cmd_msg){
  servo1.write(cmd_msg.data); //set servo angle, should be from 0-180  
}
void servo_cb2( const std_msgs::UInt16& cmd_msg){
  servo2.write(cmd_msg.data); //set servo angle, should be from 0-180  
}
void servo_cb3( const std_msgs::UInt16& cmd_msg){
  servo3.write(cmd_msg.data); //set servo angle, should be from 0-180  
}
void servo_cb4( const std_msgs::UInt16& cmd_msg){
  servo4.write(cmd_msg.data); //set servo angle, should be from 0-180  
}


ros::Subscriber<std_msgs::UInt16> sub0("servo", servo_cb0);
ros::Subscriber<std_msgs::UInt16> sub1("servo", servo_cb1);
ros::Subscriber<std_msgs::UInt16> sub2("servo", servo_cb2);
ros::Subscriber<std_msgs::UInt16> sub3("servo", servo_cb3);
ros::Subscriber<std_msgs::UInt16> sub4("servo", servo_cb4);

void setup(){
  nh.initNode();
  
  nh.subscribe(sub0);
  nh.subscribe(sub1);
  nh.subscribe(sub2);
  nh.subscribe(sub3);
  nh.subscribe(sub4);
        
  
  servo0.attach(5);
  servo1.attach(9);
  servo2.attach(8);
  servo3.attach(6);
  servo4.attach(7);
  
}

void loop(){
  nh.spinOnce();
  delay(1);
}
