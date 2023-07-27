import numpy
import socket
import time
import os
import datetime
import matplotlib.pyplot as plt
import urx
import serial
import math
import math3d as m3d
import yaml
import logging
import time
import matplotlib
import matplotlib.pyplot as plt
from numpy import pi

import numpy as np
from scipy.signal import butter,filtfilt

def Init_ur5(ur5_port):
    tcp = ((0,0,0.1476,0,0,0))
    payload_m = 0.61
    payload_location = (0,0,0)    
    ur5 = urx.Robot(ur5_port)
    time.sleep(5)
    ur5.set_tcp(tcp)
    ur5.set_payload(payload_m, payload_location)
    return ur5

def move_ur5(ur5,moving_vector,v,a,wait=False):
    current_pose = ur5.get_pose()
    current_pose.pos[:] += moving_vector
    ur5.movel(current_pose,vel=v,acc=a,wait=wait)

def rotate_around_h(ur5,angle_r,v,a,w): 
    # this code is designed so that rotate the x axis of the TCP make sure tcp is correctly configureed
    # if rotate around the base flange, set tcp as zeros
    # rotate around a axis
    # Tct.orient = m3d.Orientation.new_euler((pi/2,0,0), encoding='XYZ')
    # rotate around y-axis
    # Tct.orient = m3d.Orientation.new_euler((0,pi/2,0), encoding='XYZ')
    # rotate around z-axis
    # Tct.orient = m3d.Orientation.new_euler((0,0,pi/2), encoding='XYZ')
    pose = ur5.get_pose()
    Tct = m3d.Transform()
    Tct.pos = m3d.Vector(0,0,0)
    Tct.orient = m3d.Orientation.new_euler(angle_r, encoding='XYZ')
    new_pos = pose*Tct
    ur5.movel(new_pos,vel=v,acc=1,wait=w)
	
def shake_a_clean(ur5):
	import time
	shake_vel = 0.1
	for item in range(2):
		clean_angle  = numpy.array([pi/4,0,0])
		rotate_around_h(ur5,clean_angle,shake_vel,1,True)
		time.sleep(1)
		rotate_around_h(ur5,-2*clean_angle,shake_vel,1,True)
		time.sleep(1)
		rotate_around_h(ur5,clean_angle,shake_vel,1,True)
		time.sleep(1)
		clean_angle  = numpy.array([0,pi/4,0])
		rotate_around_h(ur5,clean_angle,shake_vel,1,True)
		time.sleep(1)
		rotate_around_h(ur5,-2*clean_angle,shake_vel,1,True)
		time.sleep(1)
		rotate_around_h(ur5,clean_angle,shake_vel,1,True)
		time.sleep(1)
  

if __name__=="main":
    ur5_port = "192.168.1.104"
    if ur5_port == "192.168.1.104":
        moving_vector_left = numpy.array((1,1,0))*math.sqrt(2)/2
        moving_vector_right = -numpy.array((1,1,0))*math.sqrt(2)/2
        moving_vector_forward = numpy.array((1,-1,0))*math.sqrt(2)/2
        moving_vector_backward = numpy.array((-1,1,0))*math.sqrt(2)/2
        moving_vector_up = numpy.array((0,0,1))
        moving_vector_down = numpy.array((0,0,-1))
    
    if ur5_port == "192.168.1.103":
        moving_vector_left = numpy.array((1,0,0))
        moving_vector_right = numpy.array((-1,0,0))
        moving_vector_forward = numpy.array((0,-1,0))
        moving_vector_backward = numpy.array((0,1,0))
        moving_vector_up = numpy.array((0,0,1))
        moving_vector_down = numpy.array((0,0,-1))
    ur5 = Init_ur5(ur5_port)
    prepare_pos_0 = [-1.4427674452411097,-1.3111127058612269,1.8012299537658691,-2.058236900960104,-1.5705226103412073,5.7142510414123535]
    ur5.movej(prepare_pos_0,vel=0.05,acc=1,wait=True,threshold=5)
#    pose_90 = [-0.75*pi,-pi/2,pi/2,-pi/2,-pi/2,55/36*pi]
#    ur5.movej(pose_90,vel=0.08,acc=1,wait=True,threshold=5)
