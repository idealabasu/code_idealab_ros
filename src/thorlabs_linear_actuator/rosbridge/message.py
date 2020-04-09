# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:08:30 2020

@author: danaukes
"""

import message_dicts as md
import message_sets as ms

class Message(object):
    byteorder = 'little'
    def __init__(self,message_id,dest,source = 0x01,param1 = None,param2 = None,data_packet_length = None):
        b01 = message_id.to_bytes(2,self.byteorder)
        if param1 is not None:
            b2 = param1.to_bytes(1,self.byteorder) 
            b3 = param2.to_bytes(1,self.byteorder)
            b23 = b2+b3
            b4 = dest.to_bytes(1,self.byteorder)
        else:
            b23 = data_packet_length.to_bytes(2,self.byteorder)
            b4 = dest.to_bytes(1,self.byteorder) | 0x80
        b5 = source.to_bytes(1,self.byteorder)
        self.header = b01+b23+b4+b5

class MessageBuider(object):
    pass
#md.message_bbd_10x.
        
        
bs = b'\x10\x02'
a = int.from_bytes(bs,'little')
b = hex(a)

c = 528
d = c.to_bytes(2,'little')

bs = b'73876440'
s = bs.decode()

#mh1 = Message(md.message_general)

