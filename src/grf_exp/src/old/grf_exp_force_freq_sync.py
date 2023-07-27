#!/usr/bin/env python3
import rospy
import sys
import roslaunch
import time
import numpy
import math
from math import pi
import rosnode
from src.grf_exp.src.old.ur5_controller import ur5_command_publisher

# from dynamixel_controller import Dynamixel_controller


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
	try:
		front_feet.control_dynamixel("Torque_Enable",0)
		front_feet.control_dynamixel("Operating_Mode",mode)
		front_feet.control_dynamixel("Torque_Enable",1)
	except:
		pass
	try:
		back_feet.control_dynamixel("Torque_Enable",0)
		back_feet.control_dynamixel("Operating_Mode",mode) 
		back_feet.control_dynamixel("Torque_Enable",1)
	except:
		pass

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
	slip_dist = 0.015
	clean_to_exp_height = 0.1

	insert_vel = 1/1000

	# 2023-02-02
	# clean_pose  = [-1.4038532415973108, -1.3078416029559534, 1.34041166305542, -1.56696063676943, -1.5534375349627894, 5.745469570159912]
	# prepare_pose = [-1.4036372343646448, -1.2501691023456019, 1.5993051528930664, -1.883542839680807, -1.5535810629474085, 5.7462968826293945]
	# exp_pose    = [-1.4344037214862269, -1.3153298536883753, 1.7571134567260742, -1.9884713331805628, -1.5625665823565882, 5.714755058288574]

	#2023-02-27
	# prepare_pose = [0.21156051754951477, -1.6583412329303187, 2.066023826599121, -1.9778426329242151, -1.5712526480304163, 0.9973201155662537]

	# exp_pose = [0.21154853701591492, -1.6272342840777796, 2.112865924835205, -2.055852715169088, -1.5713966528521937, 0.9974279403686523]

	# clean_pose = [0.08152905851602554, -1.662487808858053, 1.7876863479614258, -1.6957810560809534, -1.5710609594928187, 0.866793155670166]
	
	#2023-03-19-passive_gripping
	# prepare_pose = [0.0815650150179863, -1.5978644529925745, 1.9941048622131348, -1.9665778318988245, -1.571324650441305, 0.8671167492866516]
	# exp_pose = [0.081541046500206, -1.5899680296527308, 2.0079269409179688, -1.9884231726275843, -1.5713723341571253, 0.8671886324882507]
	# clean_pose = [0.08128900080919266, -1.6698091665851038, 1.6587028503417969, -1.5593016783343714, -1.5711091200457972, 0.866301417350769]

	# 2023-06-02-single_claw
	prepare_pose = [0.07304871827363968, -1.5784171263324183, 1.9971623420715332, -1.9821565786944788, -1.5836175123797815, 0.8728137612342834]
	exp_pose = [0.07313298434019089, -1.5455978552447718, 2.050570011138916, -2.072040859852926, -1.5837252775775355, 0.8732691407203674]
	clean_pose = [0.07308504730463028, -1.651834789906637, 1.7938828468322754, -1.70927602449526, -1.5834015051471155, 0.8724178671836853]


	ur5.movej_ur5_ros(prepare_pose,0.01,1,True)
	# ur5.movej_ur5_ros(exp_pose,0.05,1,True)


	# try:
	# 	x_deg = float(sys.argv[1])
	# 	y_deg = float(sys.argv[2])
	# 	z_deg = float(sys.argv[3])
	# except:
	x_deg,y_deg,z_deg = -5,0,0
	try:
		recon_distance = int(sys.argv[1])
	except:
		recon_distance = 0

	# post_recon = int(sys.argv[5])

	# if post_recon==1:
	# 	rospy.loginfo("post reconfig")
	# else:
	# 	rospy.loginfo("pre reconfig")

	# try:
	# 	fore_thre = float(sys.argv[6])
	# except:
	# 	rospy.loginfo("No force limit specificied, using 1 N")
	# 	fore_thre = 1

	# END ur5 init
	# START servo init
	front_feet_num = 0
	back_feet_num = 1
	current_control = 0
	position_control = 3

	# front_feet = Dynamixel_controller(front_feet_num)
	# back_feet = Dynamixel_controller(back_feet_num)

	# _commu_res = front_feet.control_dynamixel("LED",1)
	# dxl_switch_mode(position_control)
	# _commu_res = front_feet.control_dynamixel("Goal_Current",-8)
	# _commu_res = back_feet.control_dynamixel("Goal_Current",-8)

	# if not post_recon:
	# 	dxl_switch_mode(position_control)
	# 	front_feet.move_relative(-1*recon_distance)
	# 	back_feet.move_relative(-1*recon_distance)
	# time.sleep(10)

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
	# ur5.movel_ur5_ros(moving_vector_down*clean_to_exp_height,0.02,0.1,True)
	rospy.loginfo("State: {}, move to the exp prepare position".format(state_indicator))	
	time.sleep(3)
	# ur5.force_control_intrusion(fore_thre)		
	exp_x_angle  = numpy.array([pi/180*x_deg,0,0])
	exp_y_angle  = numpy.array([0,pi/180*y_deg,0])
	exp_z_angle  = numpy.array([0,0,pi/180*z_deg])

	state_indicator = 2
	rospy.loginfo("State: {}, In position, adjusting RPY angle".format(state_indicator))
	# rotate_around_h(ur5,exp_x_angle,0.03,1,True)
	# rotate_around_h(ur5,exp_y_angle,0.03,1,True)
	# rotate_around_h(ur5,exp_z_angle,0.03,1,True)
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
	ur5.force_control_intrusion(5)
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

	# dxl_switch_mode(position_control)
	# back_feet.move_relative(-1*recon_distance)

	ur5.movel_ur5_ros(moving_vector_backward*slip_dist,0.001,0.1,True)
	time.sleep(10)
	rospy.loginfo("sliding finished")
	state_indicator = 4

	# ur5.movel_ur5_ros(moving_vector_backward*-slip_dist,0.001,0.1,True) 

	# if z_deg!=0: 
	# 	ur5.rotate_ur5_ros(exp_z_angle*-1,0.03,acc=1,wait=True)
	# if y_deg!=0:
	# 	ur5.rotate_ur5_ros(exp_y_angle*-1,0.03,acc=1,wait=True)
	# if x_deg!=0:
	# 	ur5.rotate_ur5_ros(exp_x_angle*-1,0.03,acc=1,wait=True)	
	
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
	# prefix = '/ur5'
	# list_to_kill = list(filter(lambda x: x.startswith(prefix), all_node_list))
		
	ur5.movej_ur5_ros(clean_pose,0.05,1,True)
	# back_feet.move_relative(recon_distance)
	# front_feet.move_relative(int(1.1*recon_distance))
	# back_feet.move_relative( int(1.1*recon_distance))
	ur5.shake_a_clean()
	# ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)
	rospy.signal_shutdown("finished by timer")
	rosnode.kill_nodes(list_to_kill)
	# rospy.on_shutdown(rosnode.kill_nodes(list_to_kill))