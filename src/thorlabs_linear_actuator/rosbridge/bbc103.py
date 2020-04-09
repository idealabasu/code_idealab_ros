# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:49:31 2020

@author: danaukes
"""

import message_dicts as md
import message_sets as ms
from message import Message

import ftd2xx
import time
import ftd2xx.defines as fd


    
#class BrushlessDCController(object):
#    
#    
#    @classmethod
#    def pos_apt(cls):
#    
#class BBD201(BrushlessDCController):

class LinearStage(object):
    enc_cnt_per_mm = 1
    k_velocity = 1
    k_acceleration = 1
    T = 102.4e-8
    
    baud_rate = 115200
    
    def pos_apt(self,pos):
        return pos*self.enc_cnt_per_mm
    
    def vel_apt(self,vel):
        return vel*(self.T)*(self.enc_cnt_per_mm)

    def acc_apt(self,acc):
        return acc*(self.T**2)*(self.enc_cnt_per_mm)
    
    def __init__(self,serial):
        self.serial = serial.encode()
    
    def connect(self):
        devices = ftd2xx.listDevices() 
        
        if not self.serial in devices:
            print("No device found. Exiting...")
            return None
        else: 
            ii = devices.index(self.serial)
            print("Initializing device...")
            device = ftd2xx.open(ii)
            device.setBaudRate(self.baud_rate)
        #    time.sleep(50/1000)
            time.sleep(1)
            device.setDataCharacteristics(fd.BITS_8,fd.STOP_BITS_1,fd.PARITY_NONE)
        #    device.setFlowControl()
            device.purge(fd.PURGE_RX|fd.PURGE_TX)
        #    time.sleep(50/1000)
            time.sleep(1)
            device.resetDevice()
            time.sleep(1)
            device.setFlowControl(fd.FLOW_RTS_CTS,0,0)
            device.setRts()
            print(device.getDeviceInfo())
            self.device = device

    def query_controller(self):
        request = Message.build(md.message_bbd_10x.HW_REQ_INFO,dest = 0x11, source = 0x01)
        self.device.write(request.message)
        time.sleep(.1)
        s=self.device.read(self.device.getQueueStatus())
        response = Message(s)
        print(s)
        return response

    def query_channel(self,channel):
        request = Message.build(md.message_bbd_10x.HW_REQ_INFO,dest = channel, source = 0x01)
        self.device.write(request.message)
        time.sleep(.1)
        s=self.device.read(self.device.getQueueStatus())
        response = Message(s)
        print(s)
        return response

    def close(self):
        self.device.close()
        time.sleep(1)
        del self.device



        
        
        

class DDS300(LinearStage):
    enc_cnt_per_mm = 20000
    k_velocity = 134217.73
    k_acceleration = 13.744
    
    
    
    

dds = DDS300('73876440')
dds.connect()
rc = dds.query_controller()
r1 = dds.query_channel(0x21)
r2 = dds.query_channel(0x22)
r3 = dds.query_channel(0x23)
dds.close()


import apt_types
import apt_data

msg_id, data1 = r3.parse()
d1 = apt_data.HW_GET_INFO.parse(data1)
d1f = d1.firmware
f = apt_types.APTLong(d1.firmware)
print(f.to_int())