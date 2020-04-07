# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:36:13 2020

@author: danaukes
"""

import time

import roslibpy

client = roslibpy.Ros(host='192.168.0.17', port=9090)
client.run()

talker = roslibpy.Topic(client, '/dancustom', 'std_msgs/String')

while client.is_connected:
    talker.publish(roslibpy.Message({'data': 'Hello World!'}))
    print('Sending message...')
    time.sleep(1)

talker.unadvertise()

client.terminate()