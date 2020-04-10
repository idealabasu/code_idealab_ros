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
                setattr(new,key,value.decode())
            else:
                setattr(new,key,tipu(value))
            ii+=length
        return new
    
    def __init__(self,*args):
        for key, length, tipu, item in zip(self.names,self.sizes,self.types,args):
            if tipu is None:
                setattr(self,key+'_r',item)
            elif tipu == 'string':
                setattr(self,key,item)
                value = item.encode()
                l = len(value)
                if l>length:
                    setattr(self,key+'_r',value[:length])
                elif l==length:
                    setattr(self,key+'_r',value)
                else:
                    setattr(self,key+'_r',value+b'\x00'*(length-l))
            else:
                setattr(self,key,tipu.from_int(item))
                setattr(self,key+'_r',getattr(self,key).value)
                
    def print(self):
        for item in self.names:
            print(item+': ',getattr(self,item))
            
    def serialize(self):
        message = b''
        for key,length in zip(self.names,self.sizes):
            value = getattr(self,key+'_r')
            message+=value
        return message
            

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


class MOT_GET_VELPARAMS(Data):
    names = ['chan_ident','min_velocity','acceleration','max_velocity']
    sizes = [2,4,4,4]
    types = [APTWord,APTLong,APTLong,APTLong]
    
class MOT_GET_JOGPARAMS(Data):
    names = ['chan_ident','jog_mode','jog_step_size','jog_min_velocity','jog_acceleration','jog_max_velocity','stop_mode']
    sizes = [2,2,4,4,4,4,2]
    types = [APTWord,APTWord,APTLong,APTLong,APTLong,APTLong,APTWord]
    
class MOT_GET_GENMOVEPARAMS(Data):
    names = ['chan_ident','backlash_distance']
    sizes = [2,4]
    types = [APTWord,APTLong]

class MOT_GET_MOVERELPARAMS(Data):
    names = ['chan_ident','relative_distance']
    sizes = [2,4]
    types = [APTWord,APTLong]

class MOT_GET_MOVEABSPARAMS(Data):
    names = ['chan_ident','absolute_position']
    sizes = [2,4]
    types = [APTWord,APTLong]

class MOT_GET_HOMEPARAMS(Data):
    names = ['chan_ident','home_dir','limit_switch','home_velocity','offset_distance']
    sizes = [2,2,2,4,4]
    types = [APTWord,APTWord,APTWord,APTLong,APTLong]

class MOT_MOVE_RELATIVE(Data):
    names = ['chan_ident','relative_distance']
    sizes = [2,4]
    types = [APTWord,APTLong]
    
    
data_types = {}
data_types['HW_GET_INFO']=HW_GET_INFO
data_types['RACK_GET_BAYUSED']=RACK_GET_BAYUSED
data_types['MOT_GET_VELPARAMS']=MOT_GET_VELPARAMS
data_types['MOT_GET_JOGPARAMS']=MOT_GET_JOGPARAMS
data_types['MOT_GET_GENMOVEPARAMS']=MOT_GET_GENMOVEPARAMS
data_types['MOT_GET_MOVERELPARAMS']=MOT_GET_MOVERELPARAMS
data_types['MOT_GET_MOVEABSPARAMS']=MOT_GET_MOVEABSPARAMS
data_types['MOT_GET_HOMEPARAMS']=MOT_GET_HOMEPARAMS
data_types['MOT_MOVE_RELATIVE']=MOT_MOVE_RELATIVE

if __name__=='__main__':
    a=MOT_MOVE_RELATIVE(1,10)
