# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:49:31 2020

@author: danaukes
"""

import message_dicts as md
import message_sets as ms
from message import Message
import apt_types
import apt_data

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

    def send_message(self,request):
        self.device.write(request.message)
        time.sleep(.1)
        l = self.device.getQueueStatus()
        if l>0:
            s=self.device.read(self.device.getQueueStatus())
            response = Message(s)
            response.parse()
            return response
        
    def info(self,dest):
        request = Message.build(md.message_bbd_10x.HW_REQ_INFO,dest = dest, source = 0x01)
        response = self.send_message(request)
        return response

    def move_home(self,dest):
        request = Message.build(md.message_bbd_10x.MOT_MOVE_HOME,dest = dest, source = 0x01)
        response = self.send_message(request)
        return response
    
    def enable_channel(self,dest,value):
        request = Message.build(md.message_bbd_10x.MOD_SET_CHANENABLESTATE,dest = dest, source = 0x01,param1 = 0x01,param2=value)
        response = self.send_message(request)
        return response

    def rack_get_bay_used(self,bay):
        request = Message.build(md.message_bbd_10x.RACK_REQ_BAYUSED,dest = 0x11, source = 0x01,param1 = bay)
        response = self.send_message(request)
        return response

    def mot_req_velparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_VELPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response

    def mot_req_jogparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_JOGPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response

    def mot_req_genmoveparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_GENMOVEPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response

    def mot_req_moverelparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_MOVERELPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response

    def mot_req_moveabsparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_MOVEABSPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response

    def mot_req_homeparams(self,dest,channel):
        request = Message.build(md.message_bbd_10x.MOT_REQ_HOMEPARAMS,dest = dest, source = 0x01,param1 = channel)
        response = self.send_message(request)
        return response
        
    def mot_move_relative(self,dest,data):
        request = Message.build(md.message_bbd_10x.MOT_SET_MOVERELPARAMS,dest = dest, source = 0x01,data = data)
        response = self.send_message(request)
        return response

    def close(self):
        self.device.close()
        time.sleep(1)
        del self.device


class DDS300(LinearStage):
    '''
    velocity param defaults:
    acceleration = 13744
    max_velocity = 13421773
    min_velocity = 0

    jog param defaults:
    jog_acceleration = 13744
    jog_min_velocity = 0
    jog_max_velocity = 13421773
    jog_mode = 1
    jog_step_size = 1000
    stop_mode = 2
    
    backlash_distance:  0
    relative_distance:  0
    absolute_position:  0
    '''
    
    enc_cnt_per_mm = 20000
    k_velocity = 134217.73
    k_acceleration = 13.744
    

    
    
    

dds = DDS300('73876440')
dds.connect()

rc = dds.info(0x11)
r1 = dds.info(0x21)
#r2 = dds.query_channel(0x22)
#r = dds.enable_channel(0x21,0x02)
#r = dds.enable_channel(0x21,0x01)
#r3 = dds.move_home(0x21)
r1 = dds.rack_get_bay_used(0x00)
r2 = dds.rack_get_bay_used(0x01)
r3 = dds.mot_req_velparams(0x21,0x00)
r4 = dds.mot_req_jogparams(0x21,0x00)
r5 = dds.mot_req_genmoveparams(0x21,0x00)
r6 = dds.mot_req_moverelparams(0x21,0x00)
r7 = dds.mot_req_moveabsparams(0x21,0x00)
r8 = dds.mot_req_homeparams(0x21,0x00)
 

r = dds.enable_channel(0x21,0x01)
r = dds.move_home(0x21)
data = apt_data.MOT_MOVE_RELATIVE(0x00,200000)
r = dds.mot_move_relative(0x21,data)
r = dds.enable_channel(0x21,0x02)
dds.close()


#
#msg_id, data1 = r3.parse()
#d1 = apt_data.HW_GET_INFO.parse(data1)
#d1f = d1.firmware
#f = apt_types.APTLong(d1.firmware)
#print(f.to_int())