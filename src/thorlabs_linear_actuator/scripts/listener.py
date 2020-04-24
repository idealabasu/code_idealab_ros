#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import thorlab_response

def callback(data):
    rospy.loginfo("%s is age: %d" % (data.thorlab_response))

def listener():
    rospy.init_node('thorlabs_listener_node', anonymous=True)
    rospy.Subscriber("thorlab_response", thorlab_response, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()