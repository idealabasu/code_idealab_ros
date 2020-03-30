#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:31:13 2012

@author: meka
"""
import sys
sys.path.insert(0,'/usr/local/lib/python2.6/dist-packages/pyalsa-1.0.25-py2.6-linux-i686.egg/pyalsa/')
#sys.path.insert(0,'/usr/local/lib/python2.6/dist-packages/alsaseq-0.4.1-py2.6-linux-i686.egg
#sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages/pyalsa-1.0.25-py2.7-linux-x86_64.egg/pyalsa/')
import alsaseq
from alsaseq import Sequencer

import time

class KorgGeneric(Sequencer):
    client_name = ''
    port_name = ''
    MAXEVENTS = 100000
    events={}

    def __init__(self):
        Sequencer.__init__(self)
        clients = dict([(item[0],item[1]) for item in self.connection_list()])
        ports=dict([(clientitem[0],dict([(portitem[0],portitem[1]) for portitem in clientitem[2]])) for clientitem in self.connection_list()])
#        
        device_client,device_port = (clients[self.client_name],ports[self.client_name][self.port_name])
#        
        software_port= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_MIDI_GENERIC | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
#        softwareport= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_DIRECT_SAMPLE | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
#        
        connection = ((device_client,device_port),(self.client_id, software_port))
        self.connect_ports(*connection)
        self.mode = alsaseq.SEQ_NONBLOCK
        self.connections = [connection]
        
    def read_low_level(self):        
        events = self.receive_events(0,self.MAXEVENTS)
        data = [event.get_data() for event in events]
        return data
        
    def read(self):
        ll_events = self.receive_events(0,self.MAXEVENTS)
        data = [event.get_data() for event in ll_events]
        hlevents = []
        for item in data:
#            item2 = item.copy()
#            try:
#                del item2['control.value']
#            except:
#                print 'll_event does not have a control value'
#                pass

            try:
                eventname = self.events[(item['control.channel'],item['control.param'])]
                hlevents.append((eventname,item['control.value']))
            except KeyError:
                print 'no event for this ll_event'
                
#            for key,value in self.events.iteritems():
#                value2 = value.copy()
#                del value2['control.value']
#                if item2==value2:
                    
        return hlevents
    def close(self):
        for connection in self.connections:
            self.disconnect_ports(*connection)
    def read_continuous(self):
        while True:
            a = self.read()
            if not not a:
                for item in a:
                    print item
            time.sleep(.1)
    def read_ll_continuous(self):
        while True:
            a = self.read_low_level()
            if not not a:
                for item in a:
                    print item
            time.sleep(.1)

class Korg2(KorgGeneric):
    client_name = 'nanoKONTROL2'
    port_name = 'nanoKONTROL2 MIDI 1'
    MAXEVENTS = 100000

    events={}
    events[(0,43)] = 'rev'
    events[(0,44)] = 'fwd'
    events[(0,42)] = 'stop'
    events[(0,41)] = 'play'
    events[(0,45)] = 'rec'
    events[(0,64)] = 'ch_0_r'
    events[(0,48)] = 'ch_0_m'
    events[(0,32)] = 'ch_0_s'
    events[(0,65)] = 'ch_1_r'
    events[(0,49)] = 'ch_1_m'
    events[(0,33)] = 'ch_1_s'
    events[(0,66)] = 'ch_2_r'
    events[(0,50)] = 'ch_2_m'
    events[(0,34)] = 'ch_2_s'
    events[(0,67)] = 'ch_3_r'
    events[(0,51)] = 'ch_3_m'
    events[(0,35)] = 'ch_3_s'
    events[(0,68)] = 'ch_4_r'
    events[(0,52)] = 'ch_4_m'
    events[(0,36)] = 'ch_4_s'
    events[(0,69)] = 'ch_5_r'
    events[(0,53)] = 'ch_5_m'
    events[(0,37)] = 'ch_5_s'
    events[(0,70)] = 'ch_6_r'
    events[(0,54)] = 'ch_6_m'
    events[(0,38)] = 'ch_6_s'
    events[(0,71)] = 'ch_7_r'
    events[(0,55)] = 'ch_7_m'
    events[(0,39)] = 'ch_7_s'
    events[(0,58)] = 'track_left'
    events[(0,59)] = 'track_right'
    events[(0,46)] = 'cycle'
    events[(0,60)] = 'marker_set'
    events[(0,61)] = 'marker_left'
    events[(0,62)] = 'marker_right'
    events[(0,0)] = 'ch_0_rough'
    events[(0,1)] = 'ch_1_rough'
    events[(0,2)] = 'ch_2_rough'
    events[(0,3)] = 'ch_3_rough'
    events[(0,4)] = 'ch_4_rough'
    events[(0,5)] = 'ch_5_rough'
    events[(0,6)] = 'ch_6_rough'
    events[(0,7)] = 'ch_7_rough'
    events[(0,16)] = 'ch_0_fine'
    events[(0,17)] = 'ch_1_fine'
    events[(0,18)] = 'ch_2_fine'
    events[(0,19)] = 'ch_3_fine'
    events[(0,20)] = 'ch_4_fine'
    events[(0,21)] = 'ch_5_fine'
    events[(0,22)] = 'ch_6_fine'
    events[(0,23)] = 'ch_7_fine'

#    def __init__(self):
#        Sequencer.__init__(self)
#        clients = dict([(item[0],item[1]) for item in self.connection_list()])
#        ports=dict([(clientitem[0],dict([(portitem[0],portitem[1]) for portitem in clientitem[2]])) for clientitem in self.connection_list()])
##        
#        device_client,device_port = (clients[self.client_name],ports[self.client_name][self.port_name])
##        
#        software_port= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_MIDI_GENERIC | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
##        softwareport= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_DIRECT_SAMPLE | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
##        
#        connection = ((device_client,device_port),(self.client_id, software_port))
#        self.connect_ports(*connection)
#        self.mode = alsaseq.SEQ_NONBLOCK
#        self.connections = [connection]
#        
#    def read_low_level(self):        
#        events = self.receive_events(0,self.MAXEVENTS)
#        data = [event.get_data() for event in events]
#        return data
#        
#    def read(self):
#        ll_events = self.receive_events(0,self.MAXEVENTS)
#        data = [event.get_data() for event in ll_events]
#        hlevents = []
#        for item in data:
#            item2 = item.copy()
#            del item2['control.value']
#            for key,value in self.events.iteritems():
#                value2 = value.copy()
#                del value2['control.value']
#                if item2==value2:
#                    hlevents.append((key,item['control.value']))
#        return hlevents
#    def close(self):
#        for connection in self.connections:
#            self.disconnect_ports(*connection)
#    def read_continuous(self):
#        while True:
#            a = self.read()
#            if not not a:
#                for item in a:
#                    print item
#            time.sleep(.1)
#    def read_ll_continuous(self):
#        while True:
#            a = self.read_low_level()
#            if not not a:
#                for item in a:
#                    print item
#            time.sleep(.1)

class Korg1(KorgGeneric):
    client_name = 'nanoKONTROL'
    port_name = 'nanoKONTROL MIDI 1'
    MAXEVENTS = 100000
    
    events = {}
    events[(0,47)] = 'rev'
    events[(0,45)] = 'play' 
    events[(0,48)] = 'fwd'
    events[(0,49)] = 'loop'
    events[(0,46)] = 'stop' 
    events[(0,44)] = 'rec'
    events[(0,33)] = 'ch_0_r'
    events[(0,23)] = 'ch_0_s' 
    events[(0,34)] = 'ch_1_r'
    events[(0,24)] = 'ch_1_s'
    events[(0,35)] = 'ch_2_r'
    events[(0,25)] = 'ch_2_s'
    events[(0,36)] = 'ch_3_r'
    events[(0,26)] = 'ch_3_s'
    events[(0,37)] = 'ch_4_r'
    events[(0,27)] = 'ch_4_s'
    events[(0,38)] = 'ch_5_r'
    events[(0,28)] = 'ch_5_s'
    events[(0,39)] = 'ch_6_r'
    events[(0,29)] = 'ch_6_s'
    events[(0,40)] = 'ch_7_r'
    events[(0,30)] = 'ch_7_s'
    events[(0,41)] = 'ch_8_r'
    events[(0,31)] = 'ch_8_s' 

    events[(0,2)] = 'ch_0_rough'
    events[(0,3)] = 'ch_1_rough'
    events[(0,4)] = 'ch_2_rough'
    events[(0,5)] = 'ch_3_rough'
    events[(0,6)] = 'ch_4_rough'
    events[(0,8)] = 'ch_5_rough'
    events[(0,9)] = 'ch_6_rough'
    events[(0,12)] = 'ch_7_rough'
    events[(0,13)] = 'ch_8_rough'

    events[(0,14)] = 'ch_0_fine'
    events[(0,15)] = 'ch_1_fine'
    events[(0,16)] = 'ch_2_fine'
    events[(0,17)] = 'ch_3_fine'
    events[(0,18)] = 'ch_4_fine'
    events[(0,19)] = 'ch_5_fine'
    events[(0,20)] = 'ch_6_fine'
    events[(0,21)] = 'ch_7_fine'
    events[(0,22)] = 'ch_8_fine'
        
if __name__=='__main__':
    k = Korg1()
#    k.read_ll_continuous()
    k.read_continuous()





#Sequencer1.disconnect_ports((device_client,device_port),(Sequencer1.client_id, softwareport))
