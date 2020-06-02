# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:12:05 2020

@author: danaukes
"""

#from: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# and https://www.learnopencv.com/shape-matching-using-hu-moments-c-python/

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
# import numpy as np
import argparse
import cv2
import imutils
import time
# import numpy
# import colorsys
# from math import pi

import idealab_tools.cv_tools.tracking as itt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

color_ranges = {}
color_ranges['red']=[((155, 47, 65),(179, 255, 255)),((0, 51, 71),(33, 255, 255))]
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
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    
    frame,centers =itt.get_colored_circles(frame,color_ranges)
    
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