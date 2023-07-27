#!/usr/bin/env python3
import rospy
import sys
import roslaunch
import time
from grf_exp.msg import dynamixel_goal_current
from ati_nano.msg import force_torque
import std_msgs.msg
from universal_robots.msg import position
from universal_robots.msg import position_command
import numpy
import math
from math import pi
import rosnode
import matplotlib.pyplot as plt



def callback_ft(data):
	global z_force
	z_force = data.fz
	# print(z_force)
	return z_force

def ft_listener():
	# rospy.init_node('ft_listener',anonymous=True)
	global z_force
	rospy.Subscriber("ati_node_chatter", force_torque, callback_ft)
	# rospy.spin()

class AnimationPlot:

    def animate(self, i, dataList, ser):
        dataList.append(z_force)              # Add to the list holding the fixed number of points to animate
        dataList = dataList[-50:]                           # Fix the list size so that the animation plot 'window' is x number of points        
        ax.clear()                                          # Clear last data frame        
        self.getPlotFormat()
        ax.plot(dataList)                                   # Plot new data frame
        

    def getPlotFormat(self):
        ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
        ax.set_title("Arduino Data")                        # Set title of figure
        ax.set_ylabel("Value")       




if __name__ == '__main__':

    plt.ion() # Stop matplotlib windows from blocking

    	
    global z_force
    z_force=0
    time_a = time.time()   
    
    freq = 10
    window_time = 1
    window_size = window_time*freq
        
#    fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window
#    ax = fig.add_subplot(111) 
    
#    realTimePlot = AnimationPlot()
    
    rospy.init_node('fft_plot_node',disable_signals=True)
    ft_listener()  
    
    window_data = []
    while  True:
        if len(window_data) <window_size:
            window_data.append(z_force)
        else:
            window_data[1::].append(z_force)
            time.sleep(1)
        print(window_data)
        

#    try:

#    except:
#        pass