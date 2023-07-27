#!/usr/bin/env python3
import rospy
import sys
import roslaunch
import time
import numpy
import math
from math import pi
import rosnode
import sys
from ur_robot_lite_controller import UR5Controller
from ati_sensor.srv import Calibrate_ati


def start_ati_node():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ['/home/dongting/Documents/catkin_ws/src/code_idealab_ros/src/ati_sensor/launch/ati_sensor.launch'])
    launch.start()
def calibrate_ati():
    try:
        rospy.wait_for_service('/calibrate_ati', 20.0)
        calibrate_service = rospy.ServiceProxy('/calibrate_ati', Calibrate_ati)
        response = calibrate_service()
        return response.success  # or whatever field your service response has
    except (rospy.ServiceException, rospy.ROSException) as e:
        rospy.logerr("Service call failed: %s" % e)
        return False


if __name__ == '__main__':
	ur5 = UR5Controller()
	# Check if ATI node exists
	if '/ati_node' not in rosnode.get_node_names():
		rospy.loginfo("ATI node not found, starting ATI node...")
		start_ati_node()

	# Calibrate ATI sensor
	if calibrate_ati():
		rospy.loginfo("ATI sensor successfully calibrated.")
	else:
		rospy.logerr("ATI sensor calibration failed.")


	# rospy.init_node('exp_node', anonymous=False)
	moving_vector_left = numpy.array((1,1,0))*math.sqrt(2)/2
	moving_vector_right = -numpy.array((1,1,0))*math.sqrt(2)/2
	moving_vector_forward = numpy.array((1,-1,0))*math.sqrt(2)/2
	moving_vector_backward = numpy.array((-1,1,0))*math.sqrt(2)/2
	moving_vector_up = numpy.array((0,0,1))
	moving_vector_down = numpy.array((0,0,-1))

	timeout = 60
	depth = 30/1000
	slip_dist = 50/1000
	clean_to_exp_height = 0.1

	insert_vel = 1/1000
	# 2023-06-02-single_claw
	prepare_pose = [0.07304871827363968, -1.5784171263324183, 1.9971623420715332, -1.9821565786944788, -1.5836175123797815, 0.8728137612342834]
	exp_pose = [0.07313298434019089, -1.5455978552447718, 2.050570011138916, -2.072040859852926, -1.5837252775775355, 0.8732691407203674]
	clean_pose = [0.07308504730463028, -1.651834789906637, 1.7938828468322754, -1.70927602449526, -1.5834015051471155, 0.8724178671836853]


	ur5.urx_method.movej(prepare_pose,0.01,1,wait=True)

	# adjust RPY angle for your experiments
	x_deg,y_deg,z_deg = 10,10,0
	try:
		recon_distance = int(sys.argv[1])
	except:
		recon_distance = 0

	# Start the date collection node
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

	# End data collection node

	state_indicator = 1
	# ur5.movel_ur5(moving_vector_down*clean_to_exp_height,0.02,0.1,True)
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
		ur5.rotate_around_h(exp_x_angle,0.1,a=1,w=True)
		rospy.loginfo("rotated x")
	if y_deg!=0:
		ur5.rotate_around_h(exp_y_angle,0.1,a=1,w=True)
		rospy.loginfo("rotated y")
	if z_deg!=0:
		ur5.rotate_around_h(exp_z_angle,0.1,a=1,w=True)
		rospy.loginfo("rotated z")
	# ur5.force_control_intrusion(5)
	time.sleep(5)
	state_indicator = 3
	rospy.loginfo("State: {}, prepare to slide".format(state_indicator))


	ur5.move_ur5(moving_vector_backward*slip_dist,0.01,0.1,True)
	time.sleep(10)
	rospy.loginfo("sliding finished")
	state_indicator = 4

	# ur5.movel_ur5(moving_vector_backward*-slip_dist,0.001,0.1,True) 

	# if z_deg!=0: 
	# 	ur5.rotate_ur5_ros(exp_z_angle*-1,0.03,acc=1,wait=True)
	# if y_deg!=0:
	# 	ur5.rotate_ur5_ros(exp_y_angle*-1,0.03,acc=1,wait=True)
	# if x_deg!=0:
	# 	ur5.rotate_ur5_ros(exp_x_angle*-1,0.03,acc=1,wait=True)	
	
	ur5.move_ur5(moving_vector_up*0.05,0.01,1,True)

	state_indicator = 5
	rospy.loginfo("State: {}, experiments finished, prepare to retract".format(state_indicator))
	# state_pub.publish(state_indicator)

	rospy.loginfo("put things back")

	rospy.loginfo("finished, current angle (XYZ) is: {}, {}, {}".format(x_deg,y_deg,z_deg))
	all_node_list  = rosnode.get_node_names()
	prefix = '/record'
	list_to_kill = list(filter(lambda x: x.startswith(prefix), all_node_list))
	rosnode.kill_nodes(list_to_kill)

	ur5.urx_method.movej(clean_pose,0.05,1,True)

	ur5.shake_a_clean()
	# ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)
	rospy.signal_shutdown("finished by timer")
	rosnode.kill_nodes(list_to_kill)
	# rospy.on_shutdown(rosnode.kill_nodes(list_to_kill))