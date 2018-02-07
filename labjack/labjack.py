# -*- coding: utf-8 -*-

import u3

class AnalogReader(object):
    ch_an= []
    ch_an.append(u3.AIN(0))
    ch_an.append(u3.AIN(1))
    ch_an.append(u3.AIN(2))
    ch_an.append(u3.AIN(3))
    
    def __init__(self,baseobj):
        self.u3 = baseobj
        self.u3.getCalibrationData()
        self.u3.configAnalog(0)
        self.u3.configAnalog(1)
        self.u3.configAnalog(2)
        self.u3.configAnalog(3)

    def readall(self):
        raw = self.u3.getFeedback(self.ch_an)
        scaled = [self.u3.binaryToCalibratedAnalogVoltage(item, isLowVoltage = False) for item in raw]
        return scaled
    def read(self,channel):
        raw, = self.u3.getFeedback(u3.AIN(channel))
        scaled = self.u3.binaryToCalibratedAnalogVoltage(raw, isLowVoltage = False)
        return scaled

    def writedac(self,channel,value):
        raw = self.u3.voltageToDACBits(value, dacNumber = channel , is16Bits = False)
        if raw>255:
            raw=255
        if raw<0:
            raw=0
        self.u3.getFeedback(u3.DAC0_8(raw)) 

d=AnalogReader(u3.U3())