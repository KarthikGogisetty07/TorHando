#!/usr/bin/python3

import rospy

from geometry_msgs.msg import Twist

from nav_msgs.msg import Odometry

from tf.transformations import euler_from_quaternion

import math

import time

class move:
    """
    This Class is meant to explain Proportional Control using ROS.
    """

    def set_goal(self, x, y):
        self.goal = [x, y]

    def __init__(self, x, y):
    
        # Initializes the Node.
        rospy.init_node("publisher_node")
        print("Initializing Node")

        # Initializes a publihser within the node
        self.controlPub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        self.odomSub = rospy.Subscriber("/odom", Odometry, self.control)
 
     def set_goal(self, x, y):

        self.goal = [x, y]

     def move2goal(self):
        #Moves the turtle to the goal.         
        
        goal_pose = Pose() 
        vel_msg = Twist()
        
        while (goal_pose.x < self.goal[0] or goal_pose.y < self.goal[1]):
		#Linear:
		
		vel_msg.linear.x = 0.5
		vel_msg.linear.y = 0 
		vel_msg.linear.z = 0
		
		# Angular:
		
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0.5
		
		# Pub:
		self.controlPub(vel_msg)
		self.rate.sleep()
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	self.controlPub(vel_msg)
	
	# controlC to strop
        rospy.spin()
        
if __name__ == "__main__":
	try:
		x = move(1,1)
		x.move2goal()
	except rospy.ROSInterruptExecution:
		pass
       

