#!/usr/bin/env python3
"""
Created on Fri May 14 14:44:06 2021
Tested on ROS Melodic Ubuntu 18.04
@author: dongting
"""

import rospy
import sys
import numpy
from read_ati_class import atiSensor
from ati_sensor.msg import force_torque
from ati_sensor.srv import calibrate_ati
import std_msgs.msg

def talker(ati_sensor, rec_queue_size, pub_rate):
    pub = rospy.Publisher('ati_node_chatter', force_torque, queue_size=rec_queue_size)
    rate = rospy.Rate(pub_rate)
    while not rospy.is_shutdown():
        force = ati_sensor.get_data()
        data = force_torque()
        data.header.stamp = rospy.Time.now()
        data.fx, data.fy, data.fz, data.tx, data.ty, data.tz = force
        pub.publish(data)
        rate.sleep()

def calibrate_service_handler(req):
    try:
        ati_sensor._calibrate()  # Call the _calibrate() method
        return True  # Return True if calibration was successful
    except Exception as e:
        print(f"Failed to calibrate: {e}")
        return False  # Return False if there was an exception

if __name__ == '__main__':

    # If a command-line argument is provided, use it as TCP_IP.
    # Otherwise, use '192.168.1.122' as a default value.
    # python3 ati_sensor_node.py
    # rosrun ati_sensor ati_sensor_node.py
    rospy.init_node('~ati_node', anonymous=False)
    TCP_IP = rospy.get_param('~ati_ip', '192.168.1.122')  # Replace '192.168.1.122' with a default IP, if you want
    rec_queue_size = 1
    pub_rate = 1000
    ati_sensor = atiSensor(tcp_ip=TCP_IP)  # Create an atiSensor object
    rospy.Service('calibrate_ati', calibrate_ati, calibrate_service_handler)
    # To calibrate in the middle of a trial, use: "rosservice call /calibrate_ati"

    rospy.loginfo("ATI started")
    try:
        talker(ati_sensor, rec_queue_size, pub_rate)
    except rospy.ROSInterruptException:
        pass