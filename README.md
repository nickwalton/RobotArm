# **Robot Arm**

[//]: # (Image References)

[image1]: ./ModeledRobotArm.JPG "Modeled Robot Arm"
[image2]: ./AssembledRobotArm.jpg "Assembled Arm"


## Design
I've always loved doing little robotics projects. When I was younger I would go to thrift stores and find old electric toys, take them apart and frankenstein them into some new robotics contraption.

Summer of 2016 I decided I wanted to make a robot arm that could flip grilled cheese sandwiches, because delicious.

At the time I was a Mechanical Engineering Major and Computer Science Minor so I started at the basic physics level to figure out the necessary dimensions of my robot arm.

I made a cardboard prototype to figure out the range of motions that would be needed, and from there developed a simple 4 DOF robot arm model. After developing the model I analyzed the stresses and torques that would be present at each joint and on each arm to figure out the necessary thickness of each arm. The basic calculation can be seen [here](./RobotArmCalculations.pdf).

### From there I modeled the arm with the calculated dimensions in solidworks.

![alt text][image1]

### I 3D printed my model, assembled and wired it with servos I had purchased. 

![alt text][image2]

## Conclusion:
Finally at a hackathon I took my assembled arm and used ROS and an arduino to be able to control each of my joints in real time with my laptop keys. It was able to pick up and move bagels around successfully! Unfortunately I realized that the end effector didn't have a good enough range of motion to flip something over successfuly. But my main goal was mostly to just have fun and learn cool things and in that it was extremely successful.
