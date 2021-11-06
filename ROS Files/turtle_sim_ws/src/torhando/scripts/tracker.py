#! /usr/bin/env python
# Created by: Arthur Gomes

import rospy
import csv
import math
from nav_msgs.msg import Odometry

class tracker:

    '''
    This class is written for monitoring robot odometry and saving it to a csv file upon node termination
    '''
    def __init__(self, position_topic):
        self.position_array = []
        self.prev = [0,0]
        rospy.init_node('tracker')
        rospy.Subscriber(position_topic, Odometry, self.odom_callback)
        rospy.loginfo('listening to odom')
        rospy.spin()

        # write to the csv file
        with open('path.csv','w',newline='') as fh:
            writer_obj = csv.writer(fh)
            writer_obj.writerows(self.position_array)
        
        rospy.loginfo('wriiten to file')

    def odom_callback(self, msg):
        temp = [msg.pose.pose.position.x, msg.pose.pose.position.y]
        if abs(math.sqrt( (temp[0]-self.prev[0])**2 + (temp[1]-self.prev[1])**2 )) > 0.01:
            self.prev = temp[:]
            self.position_array.append(temp)



