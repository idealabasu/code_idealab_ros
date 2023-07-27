#!/usr/bin/env python3
import rospy
from grf_exp.msg import dynamixel_goal_current
import std_msgs.msg
import roslaunch
import time
from std_msgs.msg import Header
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
# from dynamixel_workbench_msgs.srv import DynamixelCommand
# from geometry_msgs.msg import PoseStamped
from ni_daq.msg import ni_1_force_w_header
import numpy

class loadcell_buffer:
	def __init__(self,size):
		# self.data = [0.0 for i in numpy.arange(size)]
		self.data = numpy.zeros([size])
	def append(self, x):
		self.data.append(x)
	def get(self):
		return self.data	

class PubSub(object):
	def __init__(self):
		rospy.init_node('pubsub',anonymous=True)    
		self.lc_sub = rospy.Subscriber("/ni_daq",ni_1_force_w_header,self.lc_cb)        
		print("sub c")
		self.lc_pub = rospy.Publisher('lc_value',Float64,queue_size=5)
		print("pub c")
		self.lc_buffer = loadcell_buffer(5)        
		print("buf c")

	def lc_cb(self, msg):
		numpy.append(self.lc_buffer.append,numpy.array(msg.c1))
		# self.lc_buffer.append(numpy.array(msg.c1))
		print(len(numpy.array(msg.c1)))
		# print(len(self.lc_buffer.data))
		# print(msg.c1)
		print(type(self.lc_buffer.data))
		# print(len(self.lc_buffer.data))
		# newMsg = Float64MultiArray()
		# newMsg.data = numpy.array(self.lc_buffer.data,dtype=float)
		# self.lc_pub.publish(self.lc_buffer.data)

if __name__ == '__main__':
    try:
        a = PubSub()
        rospy.spin()
    except rospy.ROSInterruptException: pass