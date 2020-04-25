#!/usr/bin/env python
import rospy
from robotiq_ft_sensor.msg import ft_sensor
from std_msgs.msg import Int32
from sensor_msgs.msg import Image


def callback(msg):
    #print(msg.Fx)
#    msg.data
    rospy.loginfo(msg.data)

def listener():
    rospy.init_node('listener')
   # Fx = rospy.Subscriber("robotiq_ft_sensor",ft_sensor,callback)
    rospy.Subscriber("centroid",Int32,callback)
    rospy.spin()

listener = listener()
