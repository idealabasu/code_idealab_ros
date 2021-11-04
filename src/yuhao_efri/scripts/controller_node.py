#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:11:08 2021

@author: yjian154
"""

import time
import rospy
from std_msgs.msg import Int16MultiArray
import roslaunch

def talker_controller(topic,odrive_cmd,odrive_vel):
    rospy.loginfo("Controller Command Sent: {}".format([odrive_cmd,odrive_vel]))
    topic.publish(data=[odrive_cmd,odrive_vel])


if __name__ == '__main__':
    odrive_calib = 0
    odrive_ctrl_mode_vel = 1
    odrive_ctrl_mode_pos = 2
    odrive_close_loop_start = 3
    odrive_change_vel = 7
    odrive_disable = 8
    rosbag_start = 1
    rosbag_stop = 0
    
    rosbag_node_package = 'yuhao_efri'
    rosbag_node_executable = 'rosbag_node.py'
    rosbag_node = roslaunch.core.Node(rosbag_node_package, rosbag_node_executable)
    rosbag_launch = roslaunch.scriptapi.ROSLaunch()
    
    rospy.init_node('controller_node')
    odrive_topic = rospy.Publisher('controller_odrive', Int16MultiArray, queue_size=1)
    time.sleep(1)    
    
    #Initialize Odrive
    freq = 0
    talker_controller(odrive_topic,odrive_calib, freq)
    time.sleep(15)
    
    freq_max = 45
    
    t_initial = time.time()

    
    #Odrive in velocity control
    talker_controller(odrive_topic, odrive_ctrl_mode_vel, freq)
    #Odrive in close_loop mode    
    talker_controller(odrive_topic, odrive_close_loop_start, freq)
    
    for freq in range(1, freq_max+1, 1):
        #Update odrive velocity
        talker_controller(odrive_topic, odrive_change_vel, freq)
        time.sleep(2)
        rosbag_launch.start()
        rosbag_process = rosbag_launch.launch(rosbag_node)
        while True:  
            if rosbag_process.is_alive() == True:
                time.sleep(20)
                rosbag_process.stop()
                break
            else:
                continue

        print('Step velocity={} finished'.format(freq))
        
    talker_controller(odrive_topic, odrive_disable, freq)
    t_final = time.time()
    t_total = t_final - t_initial
    print('Test finished, time elipsed: {}'.format(t_total))
    rospy.signal_shutdown('Test Finished, controller closed')
    