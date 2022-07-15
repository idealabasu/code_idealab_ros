# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:44:06 2021

@author: dongting
"""
import numpy
import time
counts_per_unit = numpy.array([1000000]*3+[1000000]*3)
TCP_PORT = 49152
BUFFER_SIZE = 1024
order = 'big'

def Init_Ati_Sensor(TCP_IP):
    import socket
    print("Initilizing ati sensor")
    # global TCP_IP, TCP_PORT, BUFFER_SIZE, order

    print("Start connection to "+TCP_IP)
    # global message
    message = b''
    message  += (0x1234).to_bytes(2,byteorder=order,signed=False)
    message  += (2).to_bytes(2,order)
    message  += (1).to_bytes(4,order)
#    message = b'\x124\x00\x02\x00\x00\x00\x01'
    # global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
    s.connect((TCP_IP, TCP_PORT))
    print("Sensor connected")
    return s,message

def extract_raw(packet):
    import socket
    raw = []
    for ii in range(6):
        byte = packet[12+ii*4:12+ii*4+4]
        value = int.from_bytes(byte,byteorder=order,signed=True)
        raw.append(value)
    return raw
   
def extract_scaling(packet):
    import socket
    raw = []
    for ii in range(6):
        byte = packet[ii+2:ii+4]
        value = int.from_bytes(byte,byteorder=order,signed=False)
        raw.append(value)
    return raw

def Calibrate_Ati_Sensor(s,TCP_IP,message): 
    import socket
    import numpy as np
    s.connect((TCP_IP, TCP_PORT))
    # global calib_data
    calib_data = np.zeros([1,6])
    for j in range(0,10000):
        s.send(message)
        data = s.recv(BUFFER_SIZE)
        data2 = np.array(extract_raw(data))
        scaled_data = data2/counts_per_unit
        calib_data = calib_data + scaled_data
    calib_data = calib_data/10000
    return calib_data
		
def get_data(s,message):
    import time
    import numpy as np
    import socket
    time_a = time.time()
    s.send(message)
    data = s.recv(BUFFER_SIZE)
    data2 = np.array(extract_raw(data))
    ati_data = data2/counts_per_unit
    # current_f = 1/(time.time()-time_a)
    return ati_data

if __name__=='__main__':

    TCP_IP = "192.168.1.122"
    #TCP_IP = "192.168.1.121"
  
    ati_gamma,message = Init_Ati_Sensor(TCP_IP)
    calib_data = Calibrate_Ati_Sensor(ati_gamma,TCP_IP,message)    
    print("Calibrating")
    time.sleep(3)
    print("calibration finish")
    time_a = time.time()
    for item in range(0,1000):
        force = get_data(ati_gamma,message)-calib_data  
    time_b = time.time()-time_a
    rate = str(10000/time_b)
    print("Sampling Rate is: "+rate)

