#!/usr/bin/env python3

# -*- coding: utf-8 -*-


#import rospy
import serial
import time
import rospy

from mark10.msg import Force

class MyException(Exception):
    pass

def talker(ser):
    pub = rospy.Publisher('mark10', Force, queue_size=10)
    rospy.init_node('mark10-talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        try:
            force, unit = parse(get_value(ser))
            message = Force()
            message.force = float(force)
            message.unit = str(unit)
            print(message)
            rospy.loginfo(message)
            pub.publish(message)
        except MyException:
            pass
        rate.sleep()


def talker_local(ser):
    while True:
        m = get_value(ser)
        print(m)
        time.sleep(1/10)

class Mark10Serial(serial.Serial):
    def __init__(self,port='/dev/ttyUSB0'):
        super(Mark10Serial,self).__init__(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)
        self.close()
        self.open()
    def readforce(self,*args,**kwargs):
        a=super(Mark10Serial,self).readline(*args,**kwargs)
        try:
            b = float(a.split('N')[0])
#            print b
            return b
        except:
            return None,

def parse(s):
    try:
        force,unit = s.split(' ')
        return force,unit
    except ValueError:
        raise MyException()
    except AttributeError:
        raise MyException()

def get_value(ser):
    myqueue = ''    

    ser.write('?\r\n'.encode())        
    time.sleep(.01)
#    jj+=1
#    print(jj)
    while not (len(myqueue)==0 and ser.inWaiting()==0):
        if ser.inWaiting()>0:
            a=ser.read()
            b=a.decode()
#            print(a)
            myqueue+=b
        ii = myqueue.find('\r\n')
        if ii>0:
#            print('found crlf')
            fullstring = myqueue[:ii]
#            myqueue=myqueue[ii+2:]
            return fullstring
            
if __name__=='__main__':
#
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    
    try:
        talker(ser)
    except rospy.ROSInterruptException:
        pass    

#    try:
#        talker_local(ser)
#    except Exception as e:
#        print(e)

    
#    ser.open()
#    print ser.isOpen()
#    jj = 0

#    while True:
#        jj+=1
#        value = get_value(ser)
#        print(jj,value)

            
            
        
#            print(a)
#            try:
#                b = float(a.split('N')[0])
#                print b
#            except:
#                pass    
#    mark10 = Mark10Serial()
#    s = '?\n\r'.encode()
#    mark10.write(s)
#    r = mark10.readforce()
#    while True:
#        while mark10.inWaiting()>0:
#            print mark10.readforce()
