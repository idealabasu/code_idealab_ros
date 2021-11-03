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
import rosbag_node

odrive_calib = 0
odrive_ctrl_mode_vel = 1
odrive_ctrl_mode_pos = 2
odrive_close_loop_start = 3
odrive_change_vel = 7
odrive_disable = 8

rosbag_start = 1
rosbag_stop = 0

def talker_odrive(odrive_comd,odrive_vel):
    pub = rospy.Publisher('odrive_control', Int16MultiArray, queue_size=1)
#    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Odrive Command Sent: {}".format([odrive_comd,odrive_vel]))
    pub.publish([odrive_comd,odrive_vel])

def talker_rosbag(rosbag_comd):
    pub = rospy.Publisher('rosbag_control', Int16, queue_size=1)
#    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Odrive Command Sent: {}".format(rosbag_comd))
    pub.publish(rosbag_comd)

#if __name__ == '__main__':
    
rospy.init_node('odrive_talker', anonymous=True)
rospy.init_node('rosbag_talker', anonymous=True)

#Initialize Odrive
freq = 0
talker_odrive(odrive_calib, freq)
time.sleep(15)

freq_max = 45

t_initial = time.time()

#dir_save_bagfile = '/home/yjian154/Documents/bags/'

#Odrive in close_loop mode
talker_odrive(odrive_close_loop_start, freq)

for freq in range(1, freq_max, 1):
    talker_odrive(odrive_change_vel, freq)
    time.sleep(2)
    rosbag_node()
    time.sleep(20)
    rosbag_node.RosbagRecord.terminate_ros_node()
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
    
talker_odrive(odrive_disable)
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