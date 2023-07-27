#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:59:56 2022

@author: dongting
"""


from scipy.fft import fft, fftfreq, ifft
from scipy import signal
import matplotlib.pyplot as plt
import numpy
import os

def draw_fft(fname,digit,skip_header=True):
    # fname = "w_contact_ground_freq_test.csv"
    # digit = 1
    from datetime import datetime
    import pandas
    if skip_header==True:
        # data1 = pandas.read_csv(fname,header=None).to_numpy()
        # data1 = pandas.read_csv(fname,header=1)
        # pt = datetime.strptime(data1[0,0],"%Y/%m/%d/%H:%M:%S.%f")
        # total_seconds = pt.hour*3600+pt.minute*60+pt.second+pt.microsecond/100000
        # converters= lambda x:pandas.to_datetime(x, "%Y/%m/%d/%H:%M:%S.%f")
        data1 = numpy.genfromtxt(fname,delimiter=',',converters={0: lambda x: datetime.strptime(x, "%Y/%m/%d/%H:%M:%S.%f"),4: numpy.float})
        data = data1[1::,:]
    else:
        data= numpy.genfromtxt(fname,delimiter=',')
   
    N = len(data)
    T = 1/1000
   
    sampling_rate = 1000
    freq = 1/T
   
    x = data[:,0]
    y = data[:,digit]-numpy.mean(data[:,digit])
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]
   
    f, Pxx_den = signal.periodogram(y, freq)
   
    plt.subplot(211)
    plt.title("FFT")
    # fig, ax = plt.subplots()
    plt.plot(xf, 2.0/N * numpy.abs(yf[0:N//2]))
    # plt.grid()
    # plt.xlim(((30,3500)))
    plt.subplot(212)
    plt.title("PSD")
    plt.plot(f, Pxx_den)
    plt.show()
    return data

   
def draw_force(fname,digit):
    # fname = "w_contact_ground_freq_test.csv"
    # digit = 1
    data= numpy.genfromtxt(fname,delimiter=',')
    x = data[:,0]
    y = data[:,digit]
    plt.plot.loglog(x,y)
    # plt.grid()
    # plt.xlim(((30,3500)))
    plt.show()
   
   
fname1 = "ground_only_current_5-ati_node_chatter.csv"
fname2 = "pure_rail_current_5-ati_node_chatter.csv"
# fname2 = "no_contact.csv"
# fname3 = "hand_dragging.csv"

data_dir =os.path.join('data', '07-19-ros')

# fname1 = "07-06_angle_5_servo_10.csv"
# fname4 = "07-06_angle_5_servo_20.csv"
# fname5 = "07-06_angle_5_servo_30.csv"

fname1 = os.path.join(data_dir,fname1)
fname2 = os.path.join(data_dir,fname2)
# fname5 = os.path.join(data_dir,fname5)


# data_dir = "data/07-05-onyx-round"
# fname2 = "0705-onyx_round-servo_dragging_30_nocontact.csv"
# fname3 = "0705-onyx_round-servo_no_dragging.csv"


# fname2 = os.path.join(data_dir,fname2)
# fname3 = os.path.join(data_dir,fname3)


digit=6
plt.figure()
data1 = draw_fft(fname1,digit)
data2 = draw_fft(fname2,digit)

# draw_fft(fname2,digit1)
# draw_fft(fname3,digit1)
# plt.legend({fname1,fname2,fname3})

# draw_force(fname1,digit=1)
# draw_force(fname2,digit=1)
# draw_force(fname3,digit=1)

# plt.show()