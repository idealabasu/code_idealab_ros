#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from ati_nano.msg import force_torque
import numpy
import read_ati_gamma as gamma
import sys
import std_msgs.msg

def talker(rec_queue_size,pub_rate):
    pub = rospy.Publisher('ati_gamma_chatter', force_torque, queue_size=rec_queue_size)
    
    rate = rospy.Rate(pub_rate) # 10hz
    while not rospy.is_shutdown():
        # force = gamma.get_data(ati_gamma,message)      
        force = gamma.get_data(ati_gamma,message)-calib_data 
        data = force_torque()
        data.header.stamp = rospy.Time.now()
        data.fx = force[0][0]
        data.fy = force[0][1]
        data.fz = force[0][2]
        data.tx = force[0][3]
        data.ty = force[0][4]
        data.tz = force[0][5]
        # data.fx = force[0]
        # data.fy = force[1]
        # data.fz = force[2]
        # data.tx = force[3]
        # data.ty = force[4]
        # data.tz = force[5]
        # rospy.loginfo(data)
        # rospy.loginfo(current_f)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':

    TCP_IP = sys.argv[1]
    rec_queue_size = int(sys.argv[2])
    pub_rate = int(sys.argv[3])
    # print(rec_queue_size)
    # print(pub_rate)
    # TCP_IP = "192.168.1.122"
    #TCP_IP = "192.168.1.121"
    ati_gamma,message = gamma.Init_Ati_Sensor(TCP_IP)
    calib_data = gamma.Calibrate_Ati_Sensor(ati_gamma,TCP_IP,message)
    # force = gamma.get_data(ati_gamma,message)-calib_data
    # print(force)
    rospy.init_node('ati_gamma', anonymous=False)
    rospy.loginfo("ATI started")
    try:
        talker(rec_queue_size,pub_rate)
    except rospy.ROSInterruptException:
        pass
