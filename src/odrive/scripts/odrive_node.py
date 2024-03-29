#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:24:06 2021

@author: yjian154
"""

from __future__ import print_function

import odrive
import rospy
from std_msgs.msg import Int16MultiArray


def odrive_move(usr_cmd, odrive_val):
        
    if usr_cmd == 0:
        print('Odrive Calibration Started')
        axis.requested_state = 3
        
    elif usr_cmd == 1:
        print('Setting control mode = Velocity')
        ctrl.config.control_mode = 2
        
    elif usr_cmd == 2:
        print('Setting control mode = Position')
        ctrl.config.control_mode = 3
        
    elif usr_cmd == 3:
        axis.requested_state = 8
        print('Setting working mode = Closed Loop')
        
    elif usr_cmd ==7:
        ctrl.input_vel = int(odrive_val)
        print('Odrive Started, velocity = {}'.format(odrive_val))
        
    elif usr_cmd == 8:
        axis.requested_state = 1
        print("Odrive Disabled")
        
    else:
        print('Error: Odrive command not recognized')
        pass

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Odrive Command Received: {}'.format(data.data))
    odrive_state = data.data[0]
    odrive_val = data.data[1]
    odrive_move(odrive_state, odrive_val)
    
def stop_odrive_handler():
    axis.requested_state = 1

def listener_odrive():
    rospy.Subscriber('controller_odrive', Int16MultiArray, callback)
    rospy.on_shutdown(stop_odrive_handler)
    rospy.spin()
    
if __name__ == '__main__':
    rospy.init_node('odrive_node')
    rospy.loginfo(rospy.get_name() + ' start')
    print("finding an odrive...")
    my_drive = odrive.find_any()
    axis = my_drive.axis1
    mo = axis.motor
    enc = axis.encoder
    ctrl = axis.controller
    mo.config.current_lim = 30
    mo.config.requested_current_range = 90
    mo.config.calibration_current = 20
    ctrl.config.vel_limit = 8000
    mo.config.pole_pairs = 7
    mo.config.motor_type = 0
    enc.config.cpr = 8192
    my_drive.config.dc_max_negative_current = -30
    print('Motor found{}'.format(mo))
    listener_odrive()




'''
MOTOR_TYPE_HIGH_CURRENT = 0,
MOTOR_TYPE_GIMBAL = 2
'''
'''
CTRL_MODE_VOLTAGE_CONTROL = 0,
CTRL_MODE_CURRENT_CONTROL = 1,
CTRL_MODE_VELOCITY_CONTROL = 2,
CTRL_MODE_POSITION_CONTROL = 3,
CTRL_MODE_TRAJECTORY_CONTROL = 4
'''
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