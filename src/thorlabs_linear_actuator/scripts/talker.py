#!/usr/bin/env python

import rospy
#from std_msgs.msg import String
from thorlabs_linear_actuator.msg import thorlab_response

def talker():
    pub = rospy.Publisher('thorlab_response', thorlab_response, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = thorlab_response()
    msg.thorlab_response = 'test'

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
