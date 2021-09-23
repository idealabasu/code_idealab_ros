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
from universal_robots.msg import position


import numpy
import urx
import time
import math


def Init_ur5(ur5_port):
    try:
        tcp = ((0,0,0,0,0,0))
        payload_m = 1
        payload_location = (0,0,0.5)
        import urx      
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

def talker():
    pub = rospy.Publisher('ur53_chatter', position, queue_size=10)
    rospy.init_node('ur5e', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        loc=ur5e.get_pose()
        orient = loc.get_orient()
        q = orient.unit_quaternion
        
        data = position()
        
        data.q[0] = q[0]
        data.q[1] = q[1]
        data.q[2] = q[2]
        data.q[3] = q[3]
        data.p[0] = loc.pos[0]
        data.p[1] = loc.pos[1]
        data.p[2] = loc.pos[2]
        
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        ur5e = Init_ur5("192.168.1.103")
        talker()
    except rospy.ROSInterruptException:
        pass
