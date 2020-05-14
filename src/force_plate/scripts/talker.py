#!/usr/bin/env python

import serial
import time
import rospy

from force_plate.msg import forces

class MyException(Exception):
    pass

#import serial
import serial.tools.list_ports as lp

def talker(ser):
    pub = rospy.Publisher('force_plate', forces, queue_size=10)
    rospy.init_node('fp_node', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        try:
#            force, unit = parse(get_value(ser))
            message = forces()
            message.f1, message.f2, message.f3, message.f4 = parse(get_latest(ser))
#            message.unit = str(unit)
#            print(message)
            rospy.loginfo(message)
            pub.publish(message)
        except MyException:
            pass
        rate.sleep()
        

def talker_plain(ser):
#    pub = rospy.Publisher('force_plate', force, queue_size=10)
#    rospy.init_node('force-plate-talker', anonymous=True)
#    rate = rospy.Rate(10) # 10hz
    while True:
        try:
#            force, unit = parse(get_value(ser))
#            message = force()
#            message.f1, message.f2, message.f3, message.f4 = parse(get_value(ser))
#            message.unit = str(unit)
            message = parse(get_line(ser))
            print(message)
#            rospy.loginfo(message)
#            pub.publish(message)
        except MyException:
            pass
        time.sleep(.1)
        
def parse(s):
    try:
        my_floats = [float(item) for item in s.split(',')]
        return my_floats
    except ValueError:
        raise MyException()
    except AttributeError:
        raise MyException()

def get_line(ser):
    myqueue = ''    

#    ser.write('?\n'.encode())        
#    time.sleep(.01)
#    jj+=1
#    print(jj)
    
    while True:
        if ser.inWaiting()>0:
            a=ser.read()
            b=a.decode()
#            print(a)
            if b=='\n':
                break
            else:
                myqueue+=b

    return myqueue


def get_latest(ser):
    myqueue = ''    

#    ser.write('?\n'.encode())        
#    time.sleep(.01)
#    jj+=1
#    print(jj)
    
    while True:
        if ser.inWaiting()>0:
            a=(ser.read_all()).decode()
            myqueue+=a
            if myqueue.count('\n')>=2:
                break
    lines = myqueue.split('\n')
    
    return lines[-2]


if __name__=='__main__':

    my_filter = lambda port: ('arduino' in port.manufacturer.lower()) and (port.serial_number=='75630313736351512081')
    all_ports = lp.comports()
    my_ports = [port for port in all_ports if my_filter(port)]
    assert(len(my_ports)==1)
    
    ser = serial.Serial(
    port=my_ports[0].device,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )

#    talker_plain(ser)
#        
    try:
        talker(ser)
    except rospy.ROSInterruptException:
        pass    
#    except Exception as e:
#        print(e)
#        ser.close()
