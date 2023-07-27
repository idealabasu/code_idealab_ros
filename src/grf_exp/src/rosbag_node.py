#!/usr/bin/env python3
import rospy
import subprocess


def rosbagrecord(record_command,record_location):         
    # Start recording.
    command = "source " + record_command
    p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=record_location,
                                  executable='/bin/bash')
    rospy.spin()

if __name__ == '__main__':
    record_command = "/home/dongting/Documents/catkin_ws/src/code_idealab_ros/src/grf_exp/src/rosbag_record.sh"
    record_location = "/home/dongting/Documents/exp_data"
    rospy.init_node('record_rosbag_node')
    rospy.loginfo("Start recording")
    rosbagrecord(record_command,record_location)