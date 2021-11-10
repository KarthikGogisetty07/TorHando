#! /usr/bin/env python
# Created by: Arthur Gomes

import rospy
import csv
import math
from nav_msgs.msg import Odometry, Path
from std_msgs.msg import ColorRGBA
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, PoseStamped

class tracker:

    '''
    This class is written for monitoring robot odometry by publishing rviz markers
    '''
    def __init__(self, position_topic):
        self.prev = [0,0]
        rospy.init_node('tracker')
        rospy.Subscriber(position_topic, Odometry, self.odom_callback)
        self.marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size=10)
        self.path_pub = rospy.Publisher('/robot_path', Path, queue_size=1)
        
        # define marker msg object
        self.define_marker_object(1, 0, 0, 1.0)

        #define path msg
        self.path_msg = Path()
        self.path_msg.header.frame_id = '/odom'

        #print ideal path
        self.publish_line( 1.5, 1.5, 1.5,-1.5, 1)
        self.publish_line( 1.5,-1.5,-1.5,-1.5, 2)
        self.publish_line(-1.5,-1.5,-1.5, 1.5, 3)
        self.publish_line(-1.5, 1.5, 1.5, 1.5, 4)

        rospy.loginfo('listening to odom')
        rospy.spin()

    def define_marker_object(self,r,g,b,a):
        self.marker = Marker()
        self.marker.scale.x = 0.01
        self.marker.scale.y = 0.01
        self.marker.scale.z = 0.01
        self.marker.action = Marker.ADD
        self.marker.header.frame_id = '/odom'
        self.marker.type = Marker.LINE_STRIP


        # self.line_color = ColorRGBA()
        # self.line_color.r = r
        # self.line_color.g = g
        # self.line_color.b = b
        # self.line_color.a = a

        self.marker.color.a = a
        self.marker.color.r = r
        self.marker.color.g = g
        self.marker.color.b = b
        self.start_point = Point()
        self.end_point = Point()

    def publish_line(self, x1,y1, x2,y2, id):
        
        self.marker.pose.orientation.x = 0
        self.marker.pose.orientation.y = 0
        self.marker.pose.orientation.z = 0.0
        self.marker.pose.orientation.w = 1.0
        self.marker.id = id
        self.marker.pose.position.x = 0
        self.marker.pose.position.y = 0
        self.marker.pose.position.z = 0.0

        self.marker.points = []
        #start point
        self.start_point.x = x1
        self.start_point.y = y1
        #end point
        self.end_point.x = x2
        self.end_point.y = y2

        self.marker.points.append(self.start_point)
        self.marker.points.append(self.end_point)

        while self.marker_pub.get_num_connections() == 0:
            pass
        self.marker_pub.publish(self.marker)

    def odom_callback(self, msg):
        temp = [msg.pose.pose.position.x, msg.pose.pose.position.y]
        if abs(math.sqrt( (temp[0]-self.prev[0])**2 + (temp[1]-self.prev[1])**2 )) > 0.1:
           
            pose_msg = PoseStamped()
            pose_msg.header.frame_id = '/odom'
            pose_msg.pose.position.x = temp[0]
            pose_msg.pose.position.y = temp[1]

            self.path_msg.poses.append(pose_msg)
            self.path_pub.publish(self.path_msg)

            self.prev = temp[:]

if __name__ == '__main__':
    obj = tracker('/odom')

