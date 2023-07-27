#!/bin/bash


#rosbag record /ati_node_chatter /vrpn_client_node/rail_position/pose /goal_current_command /dynamixel_workbench/dynamixel_state /ni_daq

rosbag record  /vrpn_client_node /rail_position/pose /brake_location/pose   /ni_daq  /ati_node_chatter /exp_state /ur5_joint_publisher /ur5_pose_publisher /dynamixel_workbench/dynamixel_state
