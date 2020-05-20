# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:59:52 2020

@author: danaukes
"""

import serial

device = serial.Serial('COM6',
                       baudrate=9600,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       xonxoff=True)

s = 'IN;PA;VS30;PU100,100;PU0,0;!PG;'
b = s.encode()
device.write(b)
device.close()
