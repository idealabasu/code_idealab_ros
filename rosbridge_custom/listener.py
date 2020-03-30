# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:33:41 2020

@author: danaukes
"""

from __future__ import print_function
import roslibpy

client = roslibpy.Ros(host='192.168.0.17', port=9090)
client.run()

listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')
listener.subscribe(lambda message: print('Heard talking: ' + message['data']))

try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()
except Exception as e:
    print(e)
    client.terminate()
    