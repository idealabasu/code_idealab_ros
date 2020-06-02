#!/usr/bin/env python3

# -*- coding: utf-8 -*-


#import rospy
import serial
import time
import rospy
import cv2 as cv
import cv_bridge
import sys

import idealab_tools.cv_tools.tracking as itt
from sensor_msgs.msg import Image,CompressedImage
from tracking.msg import marker

import imutils

class MyException(Exception):
    pass

#def talker(ser):

#    rate = rospy.Rate(50) # 10hz

print(sys.version)
        
class ROSCamera(object):
    def __init__(self):
#        import cv2 as cv
        def nothing(x):
            pass
        cv.namedWindow('image')
        cv.waitKey(1)
        cv.createTrackbar('threshold','image',127,255,nothing)
        
        self.pub = rospy.Publisher('marker1', marker, queue_size=10)
        
#        rospy.init_node('tracker-talker', anonymous=True)
        self.bridge = cv_bridge.CvBridge()
#        self.kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))    
        self.image_sub = rospy.Subscriber('/image_raw',Image, self.image_callback)

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        
        image = imutils.resize(image, width=600)
    
        image,centers =itt.get_colored_circles(image,color_ranges)
        
#        t = cv.getTrackbarPos('threshold','image')

        if not rospy.is_shutdown():
            try:
                for key, list1 in centers.items():
                    for item in list1:
                        message = marker()
                        message.color = key
                        message.x = item[0]
                        message.y = item[1]
                        print(message)
                        rospy.loginfo(message)
                        self.pub.publish(message)
            except MyException:
                pass
#            rate.sleep()

if __name__=='__main__':

#    try:
#        talker(ser)
#    except rospy.ROSInterruptException:
#        pass    
#


    rospy.init_node('Camera',anonymous=True)
    cv.destroyAllWindows()
    rospy.loginfo("Start Tracking")
    camera_test = ROSCamera()
    #cv.destroyAllWindows()
    rospy.spin()
        