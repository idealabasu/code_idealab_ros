# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:23:51 2020

@author: danaukes
"""

class APTData(object):
    num_bytes = 2
    byte_format = 'little'

    def __init__(self,value):
        self.value = value

    @classmethod
    def from_int(cls,value):
        byte = (cls.int_to_complement(value)).to_bytes(cls.num_bytes,cls.byte_format)
        new = cls(byte)
        return new

    def to_int(self):
        value = self.byte_to_complement(int.from_bytes(self.value,self.byte_format))
        return value

    @classmethod
    def int_to_complement(cls,value):
        return value
    @classmethod
    def byte_to_complement(cls,value):
        return value
    
    def __str__(self):
        return str(self.to_int())

    def __repr__(self):
        return str(self)


class APTWord(APTData):
    num_bytes = 2

class APTByte(APTData):
    num_bytes = 1

class APTInt(APTData):
    
    @classmethod
    def int_to_complement(cls,value):
        if value<0:
            value =  (-value ^ cls.ones_comp)+1
        return value

    @classmethod
    def byte_to_complement(cls,value):
        if (value & cls.msb == cls.msb):
            value = -((value ^ cls.ones_comp)+1)
        return value

class APTShort(APTInt):
    num_bytes = 2
    ones_comp = 0xffff
    msb = 0x8000

class APTLong(APTInt):
    num_bytes = 4
    ones_comp = 0xffffffff
    msb = 0x80000000
    
    
#a = APTWord.from_int(2)
#b = APTShort.from_int(-2)
#c = APTLong.from_int(-123456789)
#
#print(a.to_int())
#print(b.to_int())
