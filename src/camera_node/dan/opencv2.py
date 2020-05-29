# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:12:05 2020

@author: danaukes
"""

#from: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import numpy
import colorsys

def hsb_to_rgb(value):
    value = (numpy.array(value)/numpy.array([179,255,255])).flatten().tolist()
    value = [int(item*255) for item in colorsys.hsv_to_rgb(*value)]
    value.reverse()
    return value
    
def rgb_to_hsv(value):
    value = value[::-1]
    value = numpy.array(value)/255
    value = numpy.array(colorsys.rgb_to_hsv(*value))*numpy.array([179,255,255])
    value = numpy.array(value,dtype = numpy.int).flatten().tolist()
    return value


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
# greenLower = (46, 72, 87)
# greenUpper = (76, 215, 255)
# greenLower = (33, 51, 71)
# greenUpper = (155, 255, 255)
# 
color_ranges = {}
color_ranges['red']=[((155, 47, 65),(179, 255, 255)),((0, 51, 71),(33, 255, 255))]
# color_ranges['red2']=
color_ranges['green']=[((33, 51, 71),(65, 255, 255))]
color_ranges['blue']=[((65, 51, 71),(155, 255, 255))]

pts = deque(maxlen=args["buffer"])
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
else:
    vs = cv2.VideoCapture(args["video"])
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
    # grab the current frame
    frame = vs.read()
    # handle the frame from VideoCapture or VideoStream
    frame = frame[1] if args.get("video", False) else frame
    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        break
    # resize the f\\\ame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    for key, ranges in color_ranges.items():
        blank_image = np.zeros(frame.shape[:2], dtype=np.uint8)
        for (greenLower,greenUpper) in ranges:
    
            greenAvg = (numpy.array(greenLower)+numpy.array(greenUpper))/2
            green_marker = hsb_to_rgb(greenAvg)
    
    
            mask1 = cv2.inRange(hsv, greenLower, greenUpper)
            blank_image = cv2.bitwise_or(blank_image,mask1)
        # kernel = np.ones((8,8),np.uint8)
        # kernel2 = np.ones((16,16),np.uint8)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
        mask2 = cv2.erode(blank_image, kernel, iterations=1)
        mask3 = cv2.dilate(mask2, kernel2, iterations=1)
        mask4 = cv2.erode(mask3, kernel, iterations=1)
        
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask4.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None
        centers = []
        # only proceed if at least one contour was found
        for c in cnts:
            # if len(cnts) > 0:
              # find the largest contour in the mask, then use
              # it to compute the minimum enclosing circle and
              # centroid
              # c = max(cnts, key=cv2.contourArea)
              ((x, y), radius) = cv2.minEnclosingCircle(c)
              M = cv2.moments(c)
              # only proceed if the radius meets a minimum size
              if radius > 5:
                  if M["m00"]!=0:
                      center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                      # draw the circle and centroid on the frame,
                      # then update the list of tracked points
                      cv2.circle(frame, (int(x), int(y)), int(radius),
                          green_marker, 2)
                      cv2.circle(frame, center, 5, (255,255,0), -1)
            # update the points queue
                      centers.append(center)
    #     pts.appendleft(center)
    
        # centers =
    
        # loop over the set of tracked points
    #     for i in range(1, len(pts)):
    #         # if either of the tracked points are None, ignore
    #         # them
    #         if pts[i - 1] is None or pts[i] is None:
    #             continue
    #         # otherwise, compute the thickness of the line and
    #         # draw the connecting lines
    #         thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
    #         cv2.line(frame, pts[i - 1], pts[i], greenAvg_rgb, thickness)
        # show the frame to our screen
        if key=='blue':
            cv2.imshow("test", mask4)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
    vs.stop()
# otherwise, release the camera
else:
    vs.release()
# close all windows
cv2.destroyAllWindows()    