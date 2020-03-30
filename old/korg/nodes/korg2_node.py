#!/usr/bin/python

import roslib; roslib.load_manifest('korg')
import rospy

from korg.msg import korg_event
from korg.korg import Korg2

class KorgNode(object):
    def __init__(self):
        self.pub = rospy.Publisher('korg_event',korg_event)
        rospy.init_node('korg_node')
        self.device = Korg2()
    def run(self, freq = 10):
#        ii=0
        while not rospy.is_shutdown():
            events = self.device.read()
            for event in events:
                print event
                message = korg_event(name = event[0],value =event[1])
#                ii+=1
                rospy.loginfo(message)
                self.pub.publish(message)
            rospy.sleep(1.0/freq)
        self.device.close()
            
if __name__ == '__main__':
    try:
        node = KorgNode()
        node.run()
        
    except rospy.ROSInterruptException: pass
