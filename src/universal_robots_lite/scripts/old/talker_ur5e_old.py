#!/usr/bin/env python3

import rospy
from universal_robots.msg import position
from universal_robots.msg import position_command

import numpy
import urx
import time
import math
import sys
import math3d as m3d

def Init_ur5(ur5_port):
    try:
        tcp = ((0,0,0,0,0,0))
        payload_m = 1
        payload_location = (0,0,0.5)
        ur5 = urx.Robot(ur5_port)
        time.sleep(3)
        ur5.set_tcp(tcp)
        ur5.set_payload(payload_m, payload_location)
    except:
        print("Can not connect, check connection and try again")    
    if ur5.host == ur5_port:
        print("UR5 connected at: " + ur5_port)
    else:
        print("Can not connect, check connection and try again")    
    return ur5


# def move_ur5(ur5,moving_vector,v,a,wait_f_r):
#     current_pose = ur5.get_pose()
#     current_pose.pos[:] += moving_vector
#     ur5.movel(current_pose,vel=v,acc=a,wait=wait_f_r)

# def callback(command):
#     pos = numpy.array(command.p)
#     ori = numpy.array(command.q)
#     vel = command.vel
#     acc = command.acc
#     wait_f_r = command.wait_flag
#     move_ur5(ur5,pos,vel,acc,wait_f_r)
#     pass

def move_ur5(ur5,moving_vector,v,a,w,type):
    if type == 'tran':
        current_pose = ur5.get_pose()   
        current_pose.pos[:] += moving_vector
        ur5.movel(current_pose,vel=v,acc=a,wait=w)
    else:   
        current_pose = ur5.get_pose()
        Tct = m3d.Transform()
        Tct.pos = m3d.Vector(0,0,0)
        Tct.orient = m3d.Orientation.new_euler(moving_vector, encoding='XYZ')
        new_pos = current_pose*Tct
        ur5.movel(new_pos,vel=v,acc=a,wait=w)

def callback(command):
    print("in callback")
    pos_vector = numpy.array(command.pos)
    ori_vector = numpy.array(command.RPY)
    vel = command.vel
    acc = command.acc
    wait_flag = command.wait_flag
    if all(v == 0 for v in ori_vector):
        m_type = 'tran'
        vector = pos_vector
    else:
        m_type = 'rotate'
        vector = ori_vector
    move_ur5(ur5,vector,v=vel,a=acc,w=wait_flag,type=m_type)
    pass

def talker():
    pub = rospy.Publisher('ur5_chatter', position, queue_size=10)
    # rospy.init_node('ur5', anonymous=True)
    rate = rospy.Rate(500) # 10hz
    while not rospy.is_shutdown():
        pose=ur5.get_pose()
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
        pub.publish(data)
        rate.sleep()

# def save_ur5_location(fname):
#     end_location = ur5.getj()
#     numpy.savetxt(fname,end_location,fmt='%.18e', delimiter=',')
#     # "2022-06-18-end-position.csv"
# ##---------------------------------------##

# def pick_ur5_location(fname):
#     ## Move to Saved location
#     # "2022-06-18-end-position.csv"
#     exp_pose = numpy.genfromtxt(fname)
#     ur5.movej(exp_pose,acc=0.1,vel=0.05,wait=True)

if __name__ == '__main__': 
    try:
        rospy.get_published_topics()
        print(rospy.get_published_topics())
        ros_running = True
    except ConnectionRefusedError as e:
        ros_running = False
    if ros_running:
        try:
            print("trying to connect")
            ur5 = Init_ur5("192.168.1.104")
            rospy.init_node('ur5_talker_node', anonymous=False)
            rospy.Subscriber('ur5_control', position_command, callback)
            talker()
        except rospy.ROSInterruptException:
            ur5.close()
