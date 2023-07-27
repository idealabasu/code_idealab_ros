roslaunch dynamixel_workbench_controllers dynamixel_controllers.launch
roslaunch vrpn_client_ros grf_exp.launch
rosrun ati_nano ati_node.py "192.168.1.122" 1 1000
