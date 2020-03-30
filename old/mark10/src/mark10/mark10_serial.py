#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:48:08 2012

@author: danb0b
"""

#import rospy
import serial
#import time



class Mark10Serial(serial.Serial):
    def __init__(self,port='/dev/ttyS0'):
        super(Mark10Serial,self).__init__(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)
        self.open()
        pass
    def readforce(self,*args,**kwargs):
        a=super(Mark10Serial,self).readline(*args,**kwargs)
        try:
            b = float(a.split('N')[0])
#            print b
            return b
        except:
            return


if __name__=='__main__':
#
#    ser = serial.Serial(
#        port='/dev/ttyS0',
#        baudrate=9600,
#        parity=serial.PARITY_NONE,
#        stopbits=serial.STOPBITS_ONE,
#        bytesize=serial.EIGHTBITS
#    )
#    
#    ser.open()
#    print ser.isOpen()
#    
#    while True:
#        while ser.inWaiting()>0:
#            a=ser.readline()
#            try:
#                b = float(a.split('N')[0])
#                print b
#            except:
#                pass    
    mark10 = Mark10Serial()
    while True:
        while mark10.inWaiting()>0:
            print mark10.readforce()