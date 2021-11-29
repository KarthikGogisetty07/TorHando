#!/usr/bin/python3

import rospy

from geometry_msgs.msg import Twist

from nav_msgs.msg import Odometry

from tf.transformations import euler_from_quaternion

import math

import time

class PID:
    """
    This Class is meant to explain Proportional Control using ROS.
    """

    def set_goal(self, x, y):
        self.goal = [x, y]

    def __init__(self, ka, kp, ki, kd, x, y):

        """
        Proportional Controller:

            if error = current_position - goal_position
            Then, you would want your velocity to be:
            k*error. Where k is some real constant called gain.

            Why?

            Because, you would want to approach the goal position
            in accordance to your current position (Slope).

            Slope = d(position)/d(time)

            d(time) is the time you want to take to reach that position,
            it describes how aggresive your controller has to behave. Omiting
            d(time) and having a constant K gain, will help tune the aggresion
            of the controller.

            For example:

                If your gain is too high, then, your controller will over react
                to even small errors. If your gain is too small, then it will 
                not react in time to your errors.


        """
        # Initializes the Node.
        rospy.init_node("publisher_node")
        print("Initializing Node")

        # Initializes a publihser within the node
        self.controlPub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        self.odomSub = rospy.Subscriber("/odom", Odometry, self.control)

        # P gain for angle
        self.ka = ka

        # P gain for velocity
        self.kp = kp
        
        # I gain for velocity
        self.ki = ki
        
        # I gain for velocity
        self.kd = kd
        
        #goal:
        self.set_goal(x, y)
        
    def set_goal(self, x, y):

        self.goal = [x, y]


    def control(self, msg):
        
        #now = time.time()
        
        previous_error_x = 0
        previous_error_y = 0
        
        d_error_x = 0
        d_error_y = 0
        
        # P-controller Logic:
        error_x = msg.pose.pose.position.x - self.goal[0]
        error_y = msg.pose.pose.position.y - self.goal[1]
        
        quat = msg.pose.pose.orientation
        (roll, pitch, yaw) = euler_from_quaternion([quat.x, quat.y, quat.z, quat.w])
        error_theta = math.atan2(self.goal[1], self.goal[0]) - yaw
        
        error_linear = math.sqrt(error_x**2 + error_y**2)
                       
        #I-Controller Logic:
        if(-1<error_linear<1):   
            previous_error_x = previous_error_x + self.ki*error_x
            previous_error_y = previous_error_y + self.ki*error_y
        else:
            previous_error_x = 0
            previous_error_y = 0
            
        error_linear_previous = math.sqrt(previous_error_x**2 + previous_error_y**2)
        
      
        #D-Controller Logic:
        #if(-1<error_linear<1):    
            #d_error_x = error_x - d_error_x
            #d_error_y = error_x - d_error_y
            
            #d_error = math.sqrt(d_error_x**2 + d_error_y**2)
            
            #future_error = self.kd(error_linear - d_error)/(time.time()) - now)
        #else:
            #future_error = 0
        
  
        
        new_msg = Twist()
        if(abs(error_theta) > 0.1):
            new_msg.angular.z = self.ka*error_theta
            new_msg.linear.x = 0

        else:
            if(abs(error_linear) > 0.1):
                new_msg.linear.x = self.kp*error_linear + error_linear_previous
                new_msg.angular.z = 0
            
            else:
                new_msg.linear.x = 0
                new_msg.angular.z = 0

        self.controlPub.publish(new_msg)



if __name__ == '__main__':
        p = PID(1, 0.3, 0.4, 0.2, 2, 1)
        rospy.spin()


