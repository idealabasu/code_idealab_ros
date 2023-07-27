#!/usr/bin/env python3
import rospy
import sys
import time
from ni_daq.msg import ni_1_force


def callback(data):
	# global daq_reading
	# daq_reading = ni_1_force
	rospy.loginfo(data)

def daq_listener():
    rospy.init_node('daq_listener_node', anonymous=True)
    rospy.Subscriber("/ni_daq", ni_1_force, callback)
    rospy.spin()

if __name__ == '__main__':
	# global daq_reading
	daq_listener()
	# while True:
	# 	print(daq_reading)
