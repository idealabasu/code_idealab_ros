#!/usr/bin/python

import roslib; roslib.load_manifest('mark10')
import rospy
import serial

from mark10.msg import force

class Mark10Serial(serial.Serial):
    def __init__(self,port):
        super(Mark10Serial,self).__init__(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,timeout = .001)
        self.open()
        pass
    def readforce(self,*args,**kwargs):
        a = []
        while self.inWaiting()>0:
            try:
                a.append(super(Mark10Serial,self).readline(*args,**kwargs))
            except:
                return

        try:
            b = float(a[-1].split('N')[0])
            return b
        except:
            return


class Mark10Node(object):
    def __init__(self,port):
        self.pub = rospy.Publisher('mark10_force',force)
        rospy.init_node('mark10_node')
        self.device = Mark10Serial(port = port)
    def run(self, freq = 10):
        while not rospy.is_shutdown():
            f1 = self.device.readforce()
            if f1 is not None:
                message = force(f1)
                rospy.loginfo(message)
                self.pub.publish(message)
            rospy.sleep(1.0/freq)
        self.device.close()
            
if __name__ == '__main__':
    try:
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-p", "--port", default='/dev/ttyS0', help="select port")
        options, args = parser.parse_args()
        node = Mark10Node(options.port)
        node.run()
        
    except rospy.ROSInterruptException: pass
