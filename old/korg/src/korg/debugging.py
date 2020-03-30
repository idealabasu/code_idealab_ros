# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:49:21 2012

@author: danb0b
"""

import sys
#sys.path.insert(0,'/usr/local/lib/python2.6/dist-packages/pyalsa-1.0.25-py2.6-linux-i686.egg/pyalsa/')
#sys.path.insert(0,'/usr/local/lib/python2.6/dist-packages/alsaseq-0.4.1-py2.6-linux-i686.egg
#sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages/pyalsa-1.0.25-py2.7-linux-x86_64.egg/pyalsa/')

import alsaseq
from alsaseq import Sequencer


self = Sequencer()
client_name = 'nanoKONTROL'
port_name = 'nanoKONTROL MIDI 1'
#Sequencer.__init__(self)
clients = dict([(item[0],item[1]) for item in self.connection_list()])
ports=dict([(clientitem[0],dict([(portitem[0],portitem[1]) for portitem in clientitem[2]])) for clientitem in self.connection_list()])
#        
device_client,device_port = (clients[client_name],ports[client_name][port_name])
#        
software_port= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_MIDI_GENERIC | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
#        softwareport= self.create_simple_port(name = 'softwaretitle',type = alsaseq.SEQ_PORT_TYPE_DIRECT_SAMPLE | alsaseq.SEQ_PORT_TYPE_APPLICATION, caps = alsaseq.SEQ_PORT_CAP_WRITE | alsaseq.SEQ_PORT_CAP_SUBS_WRITE)
#        
connection = ((device_client,device_port),(self.client_id, software_port))
self.connect_ports(*connection)
self.mode = alsaseq.SEQ_NONBLOCK
#self.connections = [connection]
