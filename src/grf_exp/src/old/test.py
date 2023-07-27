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

def dynamixel_goal_current_talker(goal_current):
	pub_goal_current = rospy.Publisher('goal_current_command', dynamixel_goal_current, queue_size=10)
	rate = rospy.Rate(1000)
	while not rospy.is_shutdown():
		goal_current_value = dynamixel_goal_current()
		goal_current_value.header.stamp = rospy.Time.now()
		goal_current_value.goal_current_command = 1
		pub_goal_current.publish(goal_current_value)
		rate.sleep()

def control_dynamixel(command,dxl_id,addr_name,value):
    #command,dxl_id,addr_name,value
    rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
    dynamixelCommand = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command',DynamixelCommand)
    try:
        # resp1 = dynamixelCommand('',1,'Goal_Current',0)
        resp1 = dynamixelCommand(command,dxl_id,addr_name,value)
        rospy.loginfo("moving dynamixel: current"+str(value))
        print(resp1)
    except rospy.ServiceException as exc:
        print("Service did not process request: " + str(exc))

# add a position subscriber

def callback(PoseStamped_value):
	rospy.loginfo(PoseStamped_value.pose.position.y)


def vrpn_listener():
    rospy.init_node('vrpn_listener', anonymous=True)
    rospy.Subscriber("/vrpn_client_node/rail_position/pose", PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':

	mode = sys.argv[1]
	dxl_id = int(sys.argv[2])
	value =  int(sys.argv[3])
	command = ''
	if mode=="velocity":
		addr_name = 'Goal_Velocity'
	elif mode == "current":
		addr_name = 'Goal_Current'

	rospy.init_node('exp_node')
	rospy.loginfo("Start Exp")

	rospy.loginfo("prepare to launch files")
	uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
	roslaunch.configure_logging(uuid)

	rospy.loginfo("prepare to collect")
	rosbag_node_package = 'grf_exp'
	rosbag_node_executable = 'rosbag_node.py'
	rosbag_node = roslaunch.core.Node(rosbag_node_package, rosbag_node_executable)
	rosbag_launch = roslaunch.scriptapi.ROSLaunch()
	
	rosbag_launch.start()
	rosbag_process = rosbag_launch.launch(rosbag_node)
	rospy.loginfo("Start collecting")


	# dynamixel_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/dongting/Documents/catkin_ws/src/dynamixel-workbench/dynamixel_workbench_controllers/launch/dynamixel_controllers_current.launch"])
	
	dynamixel_launch.start()
	time.sleep(2)
	rospy.loginfo("Dynamixel Started")

	# ati_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/dongting/Documents/catkin_ws/src/code_idealab_ros/src/ati_sensor/launch/ati_sensor.launch"])
	# ati_launch.start()
	# time.sleep(15)


	# vrpn_launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/dongting/Documents/catkin_ws/src/vrpn_client_ros/launch/grf_exp.launch"])
	# vrpn_launch.start(
	# rospy.loginfo("VRPN Started")

	rospy.loginfo("Start collecting")
	time_a = time.time()

	try:
		control_dynamixel(command,dxl_id,addr_name,value)
		while True:
			# print(time.time()-time_a)
			if time.time()-time_a >10:
				value = 0
				control_dynamixel(command,dxl_id,addr_name,value)
				rosbag_process.stop()
				break
	# except rospy.ROSInterruptException:
	# 	value = 0
	# 	control_dynamixel(command,dxl_id,addr_name,value)
	# 	rospy.signal_shutdown('Test Finished, controller closed')	
	except :
		rospy.loginfo('Test Finished by KeyboardInterrupt')
		# print('P Test Finished by KeyboardInterrupt')
		value = 0
		control_dynamixel(command,dxl_id,addr_name,value)
		# rospy.loginfo('Test Finished by KeyboardInterrupt')
		# dynamixel_launch.shutdown()
		# vrpn_launch.shutdown()
		rospy.signal_shutdown('Test Finished, controller closed')	