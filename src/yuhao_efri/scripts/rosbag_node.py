#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:51:46 2021

@author: yjian154
"""

import rospy
import subprocess

#def terminate_ros_node(s):
#        # Adapted from http://answers.ros.org/question/10714/start-and-stop-rosbag-within-a-python-script/
#        list_cmd = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
#        list_output = list_cmd.stdout.read()
#        retcode = list_cmd.wait()
#        assert retcode == 0, "List command returned %d" % retcode
#        for str in list_output.split("\n"):
#            if (str.startswith(s)):
#                os.system("rosnode kill " + str)
#
#def stop_recording_handler():
#        rospy.loginfo(rospy.get_name() + ' stop recording.')
#        terminate_ros_node("/rosbag_node")
        
def rosbagrecord(record_command,record_location):         
    # Start recording.
    command = "source " + record_command
    p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=record_location,
                                  executable='/bin/bash')
#        rospy.on_shutdown(stop_recording_handler)
    rospy.spin()

if __name__ == '__main__':
    record_command = "/home/yjian154/code/code_idealab_ros/src/yuhao_efri/scripts/rosbag_record.sh"
    record_location = "/home/yjian154/Documents/ros_yuhao_efri/records/"
    rospy.init_node('rosbag_node')
    rospy.loginfo(rospy.get_name() + ' start')
    rosbagrecord(record_command,record_location)

    
#    # Go to class functions that do all the heavy lifting. Do error checking.
#    try:
#        rosbag_record = RosbagRecord()
#    except rospy.ROSInterruptException:
#        pass