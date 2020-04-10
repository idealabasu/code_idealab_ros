# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:22:12 2020

@author: danaukes
"""
import message_dicts as md

from apt_types import APTWord, APTShort, APTLong, APTByte

class Data(object):
    names = []
    sizes = []
    types = []
    pass

    @classmethod
    def parse(cls,message):
        new = cls()
        ii=0
        for key, length,tipu in zip(cls.names,cls.sizes,cls.types):
            value = message[ii:(ii+length)]
            setattr(new,key+'_r',value)
            
            if tipu is None:
                pass
            elif tipu == 'string':
                setattr(new,key+'_r',value.decode())
            else:
                setattr(new,key,tipu(value))
            ii+=length
        return new
            

class HW_GET_INFO(Data):
    names = ['serial','model','type','firmware','internal1','internal2','hw_version','mod_state','nchs']
    sizes = [4,8,2,4,48,16,2,2,2]
    types = [APTLong,'string',APTWord,None,None,None,APTWord,APTWord,APTWord]


#class MOT_GET_VELPARAMS(Data):
#    names = ['','',]
#    struct = [APTWord,]
    

class RACK_GET_BAYUSED(Data):
    names = ['bay','state']
    sizes = [1,1]
    types = [APTByte,APTByte]

    
data_types = {}
data_types['HW_GET_INFO']=HW_GET_INFO
data_types['RACK_GET_BAYUSED']=RACK_GET_BAYUSED