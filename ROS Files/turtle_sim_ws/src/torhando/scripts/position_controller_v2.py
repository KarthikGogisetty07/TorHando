#! /usr/bin/env python
# created by: Arthur Gomes

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class position_controller:

    '''
    A position controller for kobuki mobile base. 
    Takes desired position in world frame as in input
    outputs velocity commands
    assume world frame always situated at robot starting position
    '''

    def __init__(self, node_name, velocity_topic, position_topic):

        # load gains from param server
        self.linear_pid = rospy.get_param('~linear_pid', [0.35, 0.001, 0.0])
        self.angular_pid = rospy.get_param('~angular_pid', [1.5, 0.0, 0.0])

        # load max speed for base from server
        self.linear_max = rospy.get_param('~linear_max',0.9)
        self.angular_max = rospy.get_param('~angular_max', 3.0)

        # load goal tolerances for base from server
        self.linear_tolerance = rospy.get_param('~linear_tolerance', 0.01)
        self.angular_tolerance = rospy.get_param('~angular_tolerance', 0.01)

        # set initial configuration of bot
        self.current_config = [0,0,0]

        # create twist msg
        self.vel_msg = Twist()

        # initialize some node stuff
        rospy.init_node(node_name)
        self.vel_pub = rospy.Publisher(velocity_topic, Twist, queue_size=1)
        rospy.Subscriber(position_topic, Odometry, self.odom_callback)
        self.rate = rospy.Rate(20)

    def odom_callback(self,msg):
        self.current_config[0] = msg.pose.pose.position.x
        self.current_config[1] = msg.pose.pose.position.y
        quat= msg.pose.pose.orientation
        _,_,self.current_config[2] = euler_from_quaternion([quat.x, quat.y, quat.z, quat.w])
        # print(math.degrees(self.current_config[2]))

    def goto(self,x,y):

        print('moving to ',x,y)
        linear_EA = 0
        angular_EA = 0
        prev_linear_E = 0
        prev_angular_E = 0

        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        
        Ea = self.angular_error(x,y)

        while abs(Ea) > self.angular_tolerance and not rospy.is_shutdown():

            Ea = self.angular_error(x,y)
            self.vel_msg.linear.x = 0
            w = self.angular_pid[0]*Ea + self.angular_pid[1]*angular_EA + self.angular_pid[2]*(Ea - prev_angular_E)
            prev_angular_E = Ea
            angular_EA += Ea

            # cap angular velocity and publish
            self.vel_msg.angular.z = self.cap_angular_velocity(w)
            self.vel_pub.publish(self.vel_msg)
            self.rate.sleep()
            # print(self.vel_msg)

        El = self.linear_error(x,y)
        while abs(El) > self.linear_tolerance and not rospy.is_shutdown():

            Ea = self.angular_error(x,y)
            El = self.linear_error(x,y)
            w = self.angular_pid[0]*Ea + self.angular_pid[1]*angular_EA + self.angular_pid[2]*(Ea - prev_angular_E)
            prev_angular_E = Ea
            angular_EA += Ea
            v = self.linear_pid[0]*El + self.linear_pid[1]*linear_EA + self.linear_pid[2]*(El - prev_linear_E)
            prev_linear_E = El
            linear_EA += El

            # cap velocities and publish
            self.vel_msg.angular.z = self.cap_angular_velocity(w)
            self.vel_msg.linear.x = self.cap_linear_velocity(v)
            self.vel_pub.publish(self.vel_msg)
            self.rate.sleep()
            # print(self.vel_msg)

        rospy.loginfo('reached')

    # def execute_trajectory(self, trajs):
    #     rospy.loginfo('starting trajectory')
    #     for traj in trajs:
    #         pass

    def angular_error(self,x,y):
        cx = self.current_config[0]
        cy = self.current_config[1]
        yaw = self.current_config[2]

        a = x*math.cos(yaw) + y*math.sin(yaw) - cx*math.cos(yaw) - cy*math.sin(yaw)
        b = -x*math.sin(yaw) + y*math.cos(yaw) + cx*math.sin(yaw) - cy*math.cos(yaw)
        return math.atan2(b,a)

    def linear_error(self,x,y):
        return math.sqrt((x - self.current_config[0])**2 + (y - self.current_config[1])**2)

    def cap_linear_velocity(self, v):
        if v > self.linear_max:
            return self.linear_max
        else:
            return v

    def cap_angular_velocity(self, w):
        if w > self.angular_max:
            return self.angular_max
        else:
            return w
            
o = position_controller('kobuki_velocity_controller', '/cmd_vel', '/odom')

# add trajectory here 
o.goto(1.5,1.5)

for i in range(10):
    o.goto(1.5,-1.5)
    o.goto(-1.5,-1.5)
    o.goto(-1.5, 1.5)
    o.goto(1.5,1.5)

o.goto(0,0)

rospy.spin()