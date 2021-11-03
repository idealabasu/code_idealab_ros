#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:11:08 2021

@author: yjian154
"""

import math
import numpy
import numpy as np
import sys
import time
import rospy
import subprocess
import os
import signal
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import Int16
import roslaunch

def talker_controller(controller_pub,odrive_cmd,odrive_vel):
#    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Controller Command Sent: {}".format([odrive_cmd,odrive_vel]))
    controller_pub.publish(data=[odrive_cmd,odrive_vel])


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
    controller_pub = rospy.Publisher('controller_talker', Int16MultiArray, queue_size=1)
    time.sleep(1)    
    
    #Initialize Odrive
    freq = 0
    talker_controller(controller_pub,odrive_calib, freq)
    time.sleep(15)
    
    freq_max = 45
    
    t_initial = time.time()
    
    #dir_save_bagfile = '/home/yjian154/Documents/bags/'
    
    #Odrive in close_loop mode
    talker_controller(controller_pub, odrive_ctrl_mode_vel, freq)
    talker_controller(controller_pub, odrive_close_loop_start, freq)
    
    for freq in range(1, freq_max, 1):
        talker_controller(controller_pub, odrive_change_vel, freq)
        time.sleep(2)
        rosbag_launch.start()
        rosbag_process = rosbag_launch.launch(rosbag_node)
#        rosbag_process = rosbag_launch.launch(rosbag_node)
        time.sleep(20)
        print (rosbag_process.is_alive())
        rosbag_process.stop()
    #    while toc - tic <= 20:
    #        en_vel = axis.encoder.vel_estimate 
    #        #print(en_vel)
    #
    #        toc = time.time()          
        
        # Name1 = 'UL_clockwise_forcedata_vel{}'.format(vel)
        # Name1 += '.csv'
        # csv.write(Name1, daq_data)
        # daq_data = np.zeros((chans_in, 1))
        print('Step velocity={} finished'.format(freq))
        
    talker_controller(controller_pub, odrive_change_vel, freq, rosbag_stop)
    t_final = time.time()
    t_total = t_final - t_initial
    print('Test finished, time elipsed: {}'.format(t_total))
    
'''
AXIS_STATE_UNDEFINED = 0,           //<! will fall through to idle
AXIS_STATE_IDLE = 1,                //<! disable PWM and do nothing
AXIS_STATE_STARTUP_SEQUENCE = 2, 	//<! the actual sequence is defined by the config.startup_... flags
AXIS_STATE_FULL_CALIBRATION_SEQUENCE = 3,   //<! run all calibration procedures, then idle
AXIS_STATE_MOTOR_CALIBRATION = 4,   	//<! run motor calibration
AXIS_STATE_SENSORLESS_CONTROL = 5,  	//<! run sensorless control
AXIS_STATE_ENCODER_INDEX_SEARCH = 6, 	//<! run encoder index search
AXIS_STATE_ENCODER_OFFSET_CALIBRATION = 7, //<! run encoder offset calibration
AXIS_STATE_CLOSED_LOOP_CONTROL = 8,  	//<! run closed loop control
AXIS_STATE_LOCKIN_SPIN = 9,       		//<! run lockin spin
AXIS_STATE_ENCODER_DIR_FIND = 10,
'''