# -*- coding: utf-8 -*-


#import rospy
import serial
import time
import rospy

from mark10.msg import force

def talker(ser):
    pub = rospy.Publisher('mark10', force, queue_size=10)
    rospy.init_node('mark10-talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        m = force(*get_value(ser))
        print(m)
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()

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
            return

def parse(string):
    try:
        force,unit = string.split(' ')
        return force,unit
    except ValueError:
        return None

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