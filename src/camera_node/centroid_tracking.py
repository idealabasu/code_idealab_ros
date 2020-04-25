#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2 as cv
import cv_bridge

def nothing(x):
    pass

class Camera:
    def __init__(self):
#        import cv2 as cv
#        def nothing(x):
#            pass
        cv.namedWindow('image')
        cv.waitKey(1)
        cv.createTrackbar('threshold','image',127,255,nothing)
        self.bridge = cv_bridge.CvBridge()
        self.kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))    
        self.image_sub = rospy.Subscriber('usb_cam/image_raw',Image, self.image_callback)
#
    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        t = cv.getTrackbarPos('threshold','image')
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)   
        blurred = cv.GaussianBlur(gray, (5, 5), 0)    
        #    thresh = cv.threshold(blurred,127,255,cv.THRESH_BINARY)
        ret,thresh = cv.threshold(blurred,t,255,cv.THRESH_BINARY_INV)
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN,self.kernel)
        closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, self.kernel)
        _, contours, _ = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #    contours = imutils.grab_contours(contours)
#        contours_data = np.asarray(contours)
        for c in contours:
            M = cv.moments(c)
            if(M["m00"] == 0):
                M["m00"] = 1
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv.circle(image, (cX, cY), 1, (255, 255, 255), -1)
            cv.putText(image, "center", (cX - 20, cY - 20),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            #print('Centroid Location: ', [cX,cY])
            #print('Number of Contours: ',len(contours))
    
        cv.imshow('image',image)
        cv.imshow('closing',closing)
        cv.imshow('thresh',thresh)
        cv.waitKey(1)   

rospy.init_node('Camera')
cv.destroyAllWindows()
rospy.loginfo("Start Tracking")
camera_test = Camera()
#cv.destroyAllWindows()
rospy.spin()
