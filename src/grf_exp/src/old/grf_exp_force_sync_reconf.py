#!/usr/bin/env python3
import rospy
import sys
import math3d as m3d
from grf_exp.msg import dynamixel_goal_current
from ati_nano.msg import force_torque
import std_msgs.msg
from std_msgs.msg import Int32
import roslaunch
import time
import urx
from universal_robots.msg import position
from universal_robots.msg import joint
from universal_robots.msg import position_command
from universal_robots.msg import joint_command
import numpy
import math
from math import pi
import rosnode
from ur5_controller import ur5_command_publisher
from dynamixel_controller import Dynamixel_controller


# def gen_ur5_vectors(ur5_port):
# 	if ur5_port == "192.168.1.104":
# 		moving_vector_left = numpy.array((1,1,0))*math.sqrt(2)/2
# 		moving_vector_right = -numpy.array((1,1,0))*math.sqrt(2)/2
# 		moving_vector_forward = numpy.array((1,-1,0))*math.sqrt(2)/2
# 		moving_vector_backward = numpy.array((-1,1,0))*math.sqrt(2)/2
# 		moving_vector_up = numpy.array((0,0,1))
# 		moving_vector_down = numpy.array((0,0,-1))
# 	if ur5_port == "192.168.1.103":
# 		moving_vector_left = numpy.array((1,0,0))
# 		moving_vector_right = numpy.array((-1,0,0))
# 		moving_vector_forward = numpy.array((0,-1,0))
# 		moving_vector_backward = numpy.array((0,1,0))
# 		moving_vector_up = numpy.array((0,0,1))
# 		moving_vector_down = numpy.array((0,0,-1))

	# moving_vectors = [moving_vector_left,moving_vector_right,moving_vector_forward,moving_vector_backward,moving_vector_up,moving_vector_down]
	
	# return moving_vectors

def dxl_switch_mode(mode):
	front_feet.control_dynamixel("Torque_Enable",0)
	back_feet.control_dynamixel("Torque_Enable",0)
	front_feet.control_dynamixel("Operating_Mode",mode)
	back_feet.control_dynamixel("Operating_Mode",mode)
	front_feet.control_dynamixel("Torque_Enable",1)
	back_feet.control_dynamixel("Torque_Enable",1)

if __name__ == '__main__':
	rospy.init_node('exp_node', anonymous=False)
	
	#UR5 part
	ur5_port = "192.168.1.104"
	ur5 = ur5_command_publisher()
	
	moving_vector_left = numpy.array((1,1,0))*math.sqrt(2)/2
	moving_vector_right = -numpy.array((1,1,0))*math.sqrt(2)/2
	moving_vector_forward = numpy.array((1,-1,0))*math.sqrt(2)/2
	moving_vector_backward = numpy.array((-1,1,0))*math.sqrt(2)/2
	moving_vector_up = numpy.array((0,0,1))
	moving_vector_down = numpy.array((0,0,-1))

	timeout = 60
	depth = 30/1000
	slip_dist = 0.05
	clean_to_exp_height = 0.1

	insert_vel = 1/1000

	prepare_pos_0 = [-1.438723389302389, -1.3827808539019983, 1.4246602058410645, -1.5966017881976526, -1.5612128416644495, 5.747987747192383]
	clean_pos = [-1.4386633078204554, -1.3676732222186487, 1.5521812438964844, -1.7392385641681116, -1.5612848440753382, 5.748300075531006]
	ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)    
	ur5.movej_ur5_ros(clean_pos,0.05,1,True)
	
	try:
		x_deg = float(sys.argv[1])
		y_deg = float(sys.argv[2])
		z_deg = float(sys.argv[3])
	except:
		x_deg,y_deg,z_deg = 0,0,0
	
	# try:
	# 	recon_distance = int(sys.argv[4])
	# except:
	# 	recon_distance = 0

	# post_recon = int(sys.argv[5])

	# if post_recon==1:
	# 	rospy.loginfo("post reconfig")
	# else:
	# 	rospy.loginfo("pre reconfig")

	try:
		fore_thre = float(sys.argv[4])
	except:
		rospy.loginfo("No force limit specificied, using 1 N")
		fore_thre = 1

	# END ur5 init
	# START servo init
	front_feet_num = 0
	back_feet_num = 1
	current_control = 0
	position_control = 3

	# front_feet = Dynamixel_controller(front_feet_num)
	# back_feet = Dynamixel_controller(back_feet_num)

	# _commu_res = front_feet.control_dynamixel("LED",1)
	# dxl_switch_mode(current_control)
	# _commu_res = front_feet.control_dynamixel("Goal_Current",-8)
	# _commu_res = back_feet.control_dynamixel("Goal_Current",-8)

	# if not post_recon:
	# 	dxl_switch_mode(position_control)
	# 	front_feet.move_relative(-1*recon_distance)
	# 	back_feet.move_relative(-1*recon_distance)
	time.sleep(10)

	# END servo init

	rospy.loginfo("RPY-angle, in XYZ order: {}".format([item for item in sys.argv[1::]]))
	rospy.loginfo("prepare to launch files")

	rospy.loginfo("prepare to collect")
	rosbag_node_package = 'grf_exp'
	rosbag_node_executable = 'rosbag_node.py'
	rosbag_node = roslaunch.core.Node(rosbag_node_package, rosbag_node_executable)
	rosbag_launch = roslaunch.scriptapi.ROSLaunch()
	
	rosbag_launch.start()
	rosbag_process = rosbag_launch.launch(rosbag_node)
	rospy.loginfo("Start collecting")
	time.sleep(3)

	state_indicator = 0
	rospy.loginfo("State: {}, start node and prepare for experiments".format(state_indicator))

	state_indicator = 1
	ur5.movel_ur5_ros(moving_vector_down*clean_to_exp_height,0.02,0.1,True)
	rospy.loginfo("State: {}, move to the exp prepare position".format(state_indicator))	
	time.sleep(3)
	ur5.force_control_intrusion(fore_thre)		
	exp_x_angle  = numpy.array([pi/180*x_deg,0,0])
	exp_y_angle  = numpy.array([0,pi/180*y_deg,0])
	exp_z_angle  = numpy.array([0,0,pi/180*z_deg])

	state_indicator = 2
	rospy.loginfo("State: {}, In position, adjusting RPY angle".format(state_indicator))


	
	rospy.loginfo([x_deg,y_deg,z_deg])
	if x_deg!=0:
		ur5.rotate_ur5_ros(exp_x_angle,0.03,acc=1,wait=True)
		rospy.loginfo("rotated x")
	if y_deg!=0:
		ur5.rotate_ur5_ros(exp_y_angle,0.03,acc=1,wait=True)
		rospy.loginfo("rotated y")
	if z_deg!=0:
		ur5.rotate_ur5_ros(exp_z_angle,0.03,acc=1,wait=True)
		rospy.loginfo("rotated z")
	time.sleep(5)
	state_indicator = 3
	rospy.loginfo("State: {}, prepare to slide".format(state_indicator))

	# START reconfig feet
	# if post_recon:
	# 	dxl_switch_mode(position_control)
	# 	front_feet.move_relative(-1*recon_distance)
	# 	back_feet.move_relative( -1*recon_distance)
	# time.sleep(10)
	# END reconfig feet

	ur5.movel_ur5_ros(moving_vector_backward*slip_dist,0.001,0.1,True)
	time.sleep(10)
	rospy.loginfo("sliding finished")
	state_indicator = 4

	ur5.movel_ur5_ros(moving_vector_backward*-slip_dist,0.001,0.1,True) 

	if z_deg!=0: 
		ur5.rotate_ur5_ros(exp_z_angle*-1,0.03,acc=1,wait=True)
	if y_deg!=0:
		ur5.rotate_ur5_ros(exp_y_angle*-1,0.03,acc=1,wait=True)
	if x_deg!=0:
		ur5.rotate_ur5_ros(exp_x_angle*-1,0.03,acc=1,wait=True)	
	
	ur5.movel_ur5_ros(moving_vector_up*0.03,0.01,1,True)

	state_indicator = 5
	rospy.loginfo("State: {}, experiments finished, prepare to retract".format(state_indicator))
	# state_pub.publish(state_indicator)

	rospy.loginfo("put things back")

	rospy.loginfo("finished, current angle (XYZ) is: {}, {}, {}".format(x_deg,y_deg,z_deg))
	all_node_list  = rosnode.get_node_names()
	prefix = '/record'
	list_to_kill = list(filter(lambda x: x.startswith(prefix), all_node_list))
	rosnode.kill_nodes(list_to_kill)
	prefix = '/ur5'
	list_to_kill = list(filter(lambda x: x.startswith(prefix), all_node_list))
		
	ur5.movej_ur5_ros(clean_pos,0.05,1,True)
	front_feet.move_relative(int(1.1*recon_distance))
	back_feet.move_relative( int(1.1*recon_distance))
	ur5.shake_a_clean()
	ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)
	rospy.signal_shutdown("finished by timer")
	rosnode.kill_nodes(list_to_kill)
	# rospy.on_shutdown(rosnode.kill_nodes(list_to_kill))