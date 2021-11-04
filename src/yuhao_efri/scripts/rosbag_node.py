#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:51:46 2021

@author: yjian154
"""

import rospy
import subprocess


def rosbagrecord(record_command,record_location):         
    # Start recording.
    command = "source " + record_command
    p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=record_location,
                                  executable='/bin/bash')
    rospy.spin()

if __name__ == '__main__':
    record_command = "/home/yjian154/code/code_idealab_ros/src/yuhao_efri/scripts/rosbag_record.sh"
    record_location = "/home/yjian154/Documents/ros_yuhao_efri/records/"
    rospy.init_node('rosbag_node')
    rospy.loginfo(rospy.get_name() + ' start')
    rosbagrecord(record_command,record_location)
