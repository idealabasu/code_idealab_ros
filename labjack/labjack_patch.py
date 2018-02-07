#! /usr/bin/env python

PKG_NAME = 'ah_control'

import roslib; roslib.load_manifest(PKG_NAME)
import rospy

from ah_control.msg import HandCommand, FingerCommand

from labjack import *
#from labjackwrapper import *

# TEST
from roslib.msg import Header
test_pub = rospy.Publisher('test_out', Header)

def callback(hand_command):
    ''' Callback for the hand command topic.  Takes a hand command message and
        applies the brake commands for each finger present via the labjack
        interface.
        
        @param hand_command The latest HandCommand object
    '''  
    test_pub.publish(Header(stamp=rospy.Time.now()))
    # for each finger command in the message, apply the brake settings
    for cmd in hand_command.finger_cmds:
        # Verify that the finger index is valid
        if cmd.index < 0 or cmd.index >= HandCommand.NUM_FINGERS:
            continue
        
        # loop through each joint
        for j in range(3):
            if cmd.brakes[j]:
#                test_pub.publish(Header(stamp=rospy.Time.now()))
                joint[cmd.index][j].positive()
#                test_pub.publish(Header(stamp=rospy.Time.now()))
            else:
#                test_pub.publish(Header(seq=0, stamp=rospy.Time.now()))
                joint[cmd.index][j].off()
#                test_pub.publish(Header(seq=1, stamp=rospy.Time.now()))

#==============================================================================
#sample lock sequence from m3ah_hand_control.py for reference
#            if self.mode[0] < 3 and self.fng_sel[0] == mec.ALL_FINGERS:
#			for i in range(len(self.hand.command.cmdfinger)):
#				if self.base_brake == 1 :
#					joint[i][0].positive()
#				else :
#					joint[i][0].off()
#				
#				if self.prox_brake == 1 :
#					joint[i][1].positive()
#				else :
#					joint[i][1].off()
#
#				if self.dist_brake == 1 :
#					joint[i][2].positive()
#				else :
#					joint[i][2].off()        
#==============================================================================    

def labjackPatch():
    ''' Main loop function for the labjack patch node
    '''
    rospy.init_node('labjack')
    
    # make sure all are off to begin with
    for fngr in range(4):
        for j in range(3):
            joint[fngr][j].off()

    print 'All  brakes are OFF... waiting for commands'    
    
    #subscribe to hand commands to get brake messages
    rospy.Subscriber('command', HandCommand, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        labjackPatch()
    # Catch any interrupts (like Ctrl-C from the terminal)
    except rospy.ROSInterruptException: pass
