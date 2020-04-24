# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:08:30 2020

@author: danaukes
"""

import message_dicts as md
import message_sets as ms
from apt_data import Data,data_types

class Message(object):
    byte_order = 'little'

    def __init__(self,message):
        self.message = message

    @classmethod
    def build(cls,message_id,dest,source = 0x01,param1 = 0,param2 = 0,data = None):
        b01 = message_id.to_bytes(2,cls.byte_order)
        if data is not None:
            b23 = len(data.serialize()).to_bytes(2,cls.byte_order)
            b4 = (dest | 0x80).to_bytes(1,cls.byte_order)
        else:
            b2 = param1.to_bytes(1,cls.byte_order) 
            b3 = param2.to_bytes(1,cls.byte_order)
            b23 = b2+b3
            b4 = dest.to_bytes(1,cls.byte_order)
            
        b5 = source.to_bytes(1,cls.byte_order)
        new = cls(b01+b23+b4+b5)
        return new
        
    def parse(self):
        msg = self.message
        b01= int.from_bytes(msg[0:2],self.byte_order)
        msg_id = md.msg_rev[b01]
        
        b4 = int.from_bytes(msg[4:5],self.byte_order)
        if b4 & 0x80 == 0x80:
            print('data: ')
            b23 = int.from_bytes(msg[2:4],self.byte_order)
            print(b23,' bytes')
#            param1 = None
#            param2 = None
            data = msg[6:(6+b23)]
        else: 
#            print('no data')
#            param1 = message[2]
#            param2 = message[3]
            data = msg[2:4]
        
        data =data_types[msg_id].parse(data)
        self.msg_id = msg_id
        self.data = data
        return msg_id,data
        

        
        

#class MessageBuider(object):
#    pass
##md.message_bbd_10x.
#        
#        
#bs = b'\x10\x02'
#a = int.from_bytes(bs,'little')
#b = hex(a)
#
#c = 528
#d = c.to_bytes(2,'little')
#
#bs = b'73876440'
#s = bs.decode()
#
##mh1 = Message(md.message_general)
#

