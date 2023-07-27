# Use NI-DAQ with ros

## Installl rosbridge suite
```
sudo apt-get install ros-melodic-rosbridge-server
```

## Build your customize package for data types

download the source file at
https://github.com/idealabasu/code_idealab_ros

cd to the folder and make the package

```
cd ~/Documents/code_idealab_ros-master
catkin_make
source devel/setup.bash
```
For example, we will use the data_type for force_torque.msg in ati_nano and ni_4_channel.msg in ni_daq


## Start ROS bridge
```
source devel/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch
```
The reason to ```source devel/setup.bash``` is to use the customize msgs in the package so that ros bridge can find it


## Windows start the publisher node


## Start echoing the data
Same reason, you need to do rouce the setup.bash
```
source devel/setup.bash
rosmsg show force_torque
```
For example, if we start a topic called ni_daq, then:
```
rostopic list
rostopic echo ni_daq
rqt_plot ni_daq
```

# ATI

## Start ATI code -- idealab_ros

install code_equipmemt
git clone https://github.com/idealabasu/code_equipment.git


<!-- from idealab_equipment import read_ati_gamma -->
```
catkin_make
source devel/setup.bash
rosrun ati_nano gamma.py

source devel/setup.bash
rostopic list
rostopic echo /ati_gamma_chatter

source devel/setup.bash

rosrun ati_nano ati_node.py "192.168.1.122" 2 2000
rostopic hz //ati_gamma_chatter 
```

## EPFL-PACKAGE
git clone https://github.com/epfl-lasa/net-ft-ros.git
cd net-ft-ros
rosdep install --from-paths src/net-ft-ros --ignore-src -r -y
source devel/setup.bash

rospack find netft_rdt_driver

roscd netft_rdt_driver/launch/
chmod +x ft_sensor.launch 
chmod +x ft_sensor.perspective 


chmod +x ft_listener.cpp
chmod +x netft_node.cpp
chmod +x netft_rdt_bias.cpp
chmod +x netft_rdt_driver.cpp

roslaunch netft_rdt_driver ft_sensor.launch 

## Netft_utils

rosrun netft_utils netft_node 192.168.1.122


### Rosdep install

### manual install

```
sudo apt-get install ros_kinetic_dev_cob_common

git clone https://github.com/dreuter/ros_libvlc.git
rosdep install --from-paths src
cd ..
catkin_make

# Install libmodbus at https://libmodbus.org/download/
autoreconf -i
./autogen.sh
./configure
make

sudo make install
export LD_RUN_PATH=/usr/local/lib
export LD_LIBRARY_PATH=/usr/local/lib/


git clone https://github.com/cbandera/rosparam_handler.git

git clone https://github.com/ros-teleop/teleop_twist_joy.git -b melodic-devel

git clone https://github.com/KITrobotics/force_torque_sensor.git

git clone https://github.com/KITrobotics/iirob_filters.git

git clone https://github.com/beltoforion/muparser.git

git clone https://github.com/ipa320/cob_common.git

git clone https://github.com/ros-industrial/ros_canopen.git

git clone https://github.com/ipa320/cob_extern.git

git clone https://github.com/ipa320/cob_driver.git

git clone https://github.com/KITrobotics/ati_force_torque.git -b melodic
```

# MOTIVE PACKAGE

## ros-vrpn

### build from source
```
cd src
git clone https://github.com/catkin/catkin_simple.git
cd ..
catkin_make
source devel/setup.bash

cd src
git clone https://github.com/ethz-asl/vrpn_catkin.git
cd ..
catkin build
source devel/setup.bash


cd src
git clone https://github.com/ethz-asl/glog_catkin.git
cd ..
catkin_make
source devel/setup.bash

cd src
git clone https://github.com/ethz-asl/ros_vrpn_client.git
cd ..
catkin_make
source devel/setup.bash

# See if you can find the package
rospack find catkin_simple
rospack find vrpn_catkin
```

### install from sudo apt-get

might not be able to find all dependencies

```
sudo apt-get install ros-melodic-vrpn-client-ros
source devel/setup.bash
```

Start the publisher with the ip address of Win PC
```
roslaunch vrpn.launch server:=192.168.1.166
```
roslaunch vrpn_client_ros sample.launch server:=192.168.1.166




# Dynamixel
## modify the basic.yaml

```
# You can find control table of Dynamixel on emanual (http://emanual.robotis.com/#control-table)
# Control table item has to be set Camel_Case and not included whitespace
# You are supposed to set at least Dynamixel ID
rail_servo:
  ID: 1
  Return_Delay_Time: 0
  Operating_Mode: 0
  Goal_Current: 0
  Present_Current: 0
```


```
# find the USB device

rosrun dynamixel_workbench_controllers find_dynamixel /dev/ttyUSB0

# Once you find the usb device, make change to the 'basic.yaml' and matching the port as well as buardrate
```
```
roslaunch dynamixel_workbench_controllers dynamixel_controllers_current.launch

rosservice call /dynamixel_workbench/dynamixel_command "command: ''
id: 1
addr_name: 'Goal_Current'
value: 0 "

roslaunch dynamixel_workbench_controllers dynamixel_controllers_velocity.launch

rosservice call /dynamixel_workbench/dynamixel_command "command: ''
id: 1
addr_name: 'Goal_Velocity'
value: 0 "

```

## Read more message from dynamixel
the command dynamixel_controllers.launch publish a message called DynamixelState.msg
To get more data, one can modify DynamixelState.msg to publish more

```
roscd dynamixel_workbench_msgs/
cd msg
ls
subl DynamixelStateList.msg
```
and modify the following raw message, eg
```
# This message includes basic data of dynamixel
string name
uint8  id

int32  present_position
int32  present_velocity
int16  present_current
int16  goal_current
int16  present_current
```
one can rebuild the package,
```
cd ~/Documents/catkin_ws
cd src
git clone https://github.com/ROBOTIS-GIT/dynamixel-workbench-msgs.git
cd dynamixel_workbench_msgs
cd msg
subl DynamixelStateList.msg
```


# build my own package
```
catkin_create_pkg grf_exp ati_nano vrpn_client_ros dynamixel_workbench_controllers dynamixel_workbench_msgs dynamixel_workbench_operators dynamixel_workbench_toolbox

gedit ~/.bashrc

#add 
# ~/Documents/catkin_ws/devel/setup.bash


```
rosrun grf_exp control_node.py

rosrun grf_exp exp.py


## start everything

```
# in the sh command
rosbag record /ati_gamma_chatter /vrpn_client_node/rail_position/pose

```

roslaunch rosbridge_server rosbridge_websocket.launch

roslaunch vrpn_client_ros grf_exp.launch

roslaunch ati_nano ati_sensor.launch


rosrun universal_robots talker_ur5e.py

rosrun grf_exp exp.py "velocity" 1 -10

rosrun grf_exp exp.py "current" 1 -3


rosrun grf_exp brake_test.py "current" 1 -3


roscore

roslaunch rosbridge_server rosbridge_websocket.launch

roslaunch ati_nano ati_sensor.launch

rosrun universal_robots talker_ur5e.py

rosrun grf_exp grf_exp_force_freq_sync.py 0 0 30 0 1

roslaunch dynamixel_workbench_controllers dynamixel_controllers_current.launch dxl_baud_rate:=1000000


### 2022-11-28
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch ati_nano ati_sensor.launch
roslaunch dynamixel_workbench_controllers reconfig_feet_position.launch

rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 100 0
rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 200 0
rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 300 0

rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 100 1
rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 200 1
rosrun grf_exp grf_exp_force_sync_reconf.py 0 0 0 300 1


### 2023-01-20

roscore

roslaunch ati_nano ati_sensor.launch

rosrun universal_robots talker_ur5e.py

rosrun grf_exp grf_exp_force_freq_sync.py


### 2023-02-02

roscore

roslaunch ati_nano ati_sensor.launch

rosrun universal_robots talker_ur5e.py

roslaunch dynamixel_workbench_controllers reconfig_feet_position.launch

rosrun grf_exp grf_exp_force_freq_sync.py 200


### 2023-02-27

prepare_pose = [0.21156051754951477, -1.6583412329303187, 2.066023826599121, -1.9778426329242151, -1.5712526480304163, 0.9973201155662537]

exp_pose = [0.21154853701591492, -1.6272342840777796, 2.112865924835205, -2.055852715169088, -1.5713966528521937, 0.9974279403686523]

clean_pose = [0.08152905851602554, -1.662487808858053, 1.7876863479614258, -1.6957810560809534, -1.5710609594928187, 0.866793155670166]

roscore

roslaunch ati_nano ati_sensor.launch

rosrun universal_robots talker_ur5e.py

roslaunch dynamixel_workbench_controllers reconfig_feet_position.launch

rosrun grf_exp grf_exp_force_freq_sync.py 200