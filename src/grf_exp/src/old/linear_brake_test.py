#!/usr/bin/env python3
import rospy
import sys
from grf_exp.msg import dynamixel_goal_current
from ati_nano.msg import force_torque
import std_msgs.msg
import roslaunch
import time
from dynamixel_workbench_msgs.srv import DynamixelCommand
from geometry_msgs.msg import PoseStamped
import serial
from dynamixel_controller import Dynamixel_controller


if __name__ == '__main__':
	
	rospy.loginfo("prepare to launch files")
	uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
	roslaunch.configure_logging(uuid)
	rospy.init_node('exp_node')
	rospy.loginfo("Init Exp")

	dxl_id = 1
	current_control = 0
	velocity_control = 1
	position_control = 3
	pull_motor = Dynamixel_controller(dxl_id)

	_commu_res = pull_motor.control_dynamixel("LED",1)
	rospy.loginfo("prepare to collect")
	rosbag_node_package = 'grf_exp'
	rosbag_node_executable = 'rosbag_node.py'
	rosbag_node = roslaunch.core.Node(rosbag_node_package, rosbag_node_executable)
	rosbag_launch = roslaunch.scriptapi.ROSLaunch()
	rosbag_launch.start()
	rosbag_process = rosbag_launch.launch(rosbag_node)
	rospy.loginfo("Start collecting")

	pull_motor.switch_mode(1)
	brake_arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
	brake_arduino.write(b'1')
	time.sleep(1)
	brake_arduino.write(b'2')
	rospy.loginfo("brake init")

	time_a = time.time()

	pull_motor.control_dynamixel("Goal_Current",-5)
	while True:
		# print(time.time()-time_a)
		if time.time()-time_a > 5 :
			brake_arduino.write(b'1')
		if time.time()-time_a > 10 :
			brake_arduino.write(b'2')
		if time.time()-time_a > 15 :
			brake_arduino.write(b'1')
			pull_motor.control_dynamixel("Torque_Enable",0)
			rosbag_process.stop()
			break

	all_node_list  = rosnode.get_node_names()
	prefix = '/record'
	list_to_kill = list(filter(lambda x: x.startswith(prefix), all_node_list))
	rospy.signal_shutdown("finished by timer")
	rosnode.kill_nodes(list_to_kill)