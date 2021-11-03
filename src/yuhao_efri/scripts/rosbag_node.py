#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:55:32 2021

@author: yjian154
"""

#!/usr/bin/env python

import rospy
import subprocess
import os
import signal
from std_msgs.msg import Int16MultiArray


record_command = '/home/code/code_idealab_ros/src/yuhao_efri/scripts/rosbag_record.sh'
record_folder = '/home/yjian154/Documents/ros_yuhao_efri/records/'

class RosbagRecord:
    
    def __init__(self):    
        
        if rospy.has_param(record_command) and rospy.has_param(record_folder):
            self.record_script = rospy.get_param(record_command)
            self.record_folder = rospy.get_param(record_folder)
            rospy.on_shutdown(self.stop_recording_handler)

            # Start recording.
            command = "source " + self.record_script
            self.p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=self.record_folder,
                                      executable='/bin/bash')
            # Wait for shutdown signal to close rosbag record
            rospy.spin()
        else:
            rospy.signal_shutdown(rospy.get_name() + ' no record script or folder specified.')
            

    def terminate_ros_node(self, s):
        # Adapted from http://answers.ros.org/question/10714/start-and-stop-rosbag-within-a-python-script/
        list_cmd = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
        list_output = list_cmd.stdout.read()
        retcode = list_cmd.wait()
        assert retcode == 0, "List command returned %d" % retcode
        for str in list_output.split("\n"):
            if (str.startswith(s)):
                os.system("rosnode kill " + str)

    def stop_recording_handler(self):
        rospy.loginfo(rospy.get_name() + ' stop recording.')
        self.terminate_ros_node("/record")


#def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + 'Odrive Command Received: %s', data.data)
#    rosbag_cmd = data.data[2]
#    if rosbag_cmd == 1:
#        RosbagRecord()
#    else:
#        RosbagRecord.stop_recording_handler()
#
#def listener_rosbag():
#    rospy.Subscriber('controller_talker', Int16MultiArray, callback)
    
if __name__ == '__main__':
    rospy.init_node('rosbag_node')
    rospy.loginfo(rospy.get_name() + ' start')

    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
#        listener_rosbag()
        rosbag_record = RosbagRecord()
    except rospy.ROSInterruptException:
        pass