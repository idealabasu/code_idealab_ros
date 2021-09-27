#!/usr/bin/env python3

import rospy
from universal_robots.msg import position
from universal_robots.msg import position_command


import numpy
import urx
import time
import math


def Init_ur5(ur5_port):
    try:
        tcp = ((0,0,0,0,0,0))
        payload_m = 1
        payload_location = (0,0,0.5)
        ur5 = urx.Robot(ur5_port)
        ur5.set_tcp(tcp)
        ur5.set_payload(payload_m, payload_location)
    except:
            print("Can not connect, check connection and try again")    
    if ur5 == None:
        print("Can not connect, check connection and try again")
    elif ur5.host == ur5_port:
        print("UR5 connected at: " + ur5_port)
    else:
        print("Can not connect, check connection and try again")    
    return ur5


def move_ur5(ur5,moving_vector,v,a,wait=False):
    current_pose = ur5.get_pose()
    current_pose.pos[:] += moving_vector
    ur5.movel(current_pose,vel=v,acc=a,wait=wait)

def callback(command):
    vector = numpy.array(command.p)
    move_ur5(ur5e,vector,0.01,1,wait=False)
    pass

def talker():
    pub = rospy.Publisher('ur5e_chatter', position, queue_size=10)
#    rospy.init_node('ur5e', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pose=ur5e.get_pose()
        orient = pose.get_orient()
        q = orient.unit_quaternion
        
        data = position()
        
        data.q[0] = q[0]
        data.q[1] = q[1]
        data.q[2] = q[2]
        data.q[3] = q[3]
        data.p[0] = pose.pos[0]
        data.p[1] = pose.pos[1]
        data.p[2] = pose.pos[2]
        
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.get_published_topics()
        ros_running = True
    except ConnectionRefusedError as e:
        ros_running = False
    
    
    if ros_running:
        try:
            ur5e = Init_ur5("192.168.1.103")
            rospy.init_node('ur5e_control', anonymous=True)
            rospy.Subscriber('/ur5e_control', position_command, callback)
            talker()
            ur5e.close()
            print('finished talker')
        except rospy.ROSInterruptException:
            ur5e.close()
    else:
        ur5e = Init_ur5("192.168.1.103")
