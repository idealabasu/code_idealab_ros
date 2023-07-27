#!/usr/bin/env python3 

from bagpy import bagreader
import bagpy
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import scipy
import sys


def draw_fft(data,digit):
    from scipy.fft import fft, fftfreq, ifft
    from scipy import signal
    import numpy
    N = len(data)
    T = (data[-1,0]-data[0,0])/len(data)
   
    freq = 1/T
   
    x = data[:,0]
    data = data - data[0,:]
    y = data[:,digit]-numpy.mean(data[:,digit])
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]
   
    f, Pxx_den = signal.periodogram(y, freq)
   
    plt.subplot(221)
    plt.title("FFT")
    # fig, ax = plt.subplots()
    plt.plot(xf, 2.0/N * numpy.abs(yf[0:N//2]))
    # plt.grid()
    # plt.xlim(((30,3500)))
    plt.subplot(222)
    plt.title("PSD")
    plt.plot(f, Pxx_den)
    plt.show()

    plt.subplot(223)
    plt.plot(data[:,digit])
#    return data


def read_ros_bag_data(fname):
#    fname = 'sd_velocity_30.bag'
    bag_data = bagreader(fname)
    ATI_MSG = bag_data.message_by_topic('/ati_node_chatter')
    ati_data = pd.read_csv(ATI_MSG).to_numpy()
    ati_data[:,0] = ati_data[:,0]-ati_data[0,0]
    
    #plt.plot(ati_data[:,5:8])
    
    MOCAP_MSG =  bag_data.message_by_topic('/vrpn_client_node/rail_position/pose')
    mocap_data = pd.read_csv(MOCAP_MSG,header=1).to_numpy()
    mocap_data[:,0] = mocap_data[:,0]-mocap_data[0,0]
    mocap_data[:,5:8] = 1000*( mocap_data[0,5:8] - mocap_data[:,5:8])
    
#    DXL_STATE_MSG =  bag_data.message_by_topic('/dynamixel_workbench/dynamixel_state')
#    dxl_state_data = pd.read_csv(DXL_STATE_MSG,header=1).to_numpy()
#    mocap_data[:,0] = mocap_data[:,0]-mocap_data[0,0]
#    mocap_data[:,5:8] = 1000*( mocap_data[0,5:8] - mocap_data[:,5:8])
    plt.subplot(224)
    plt.plot(mocap_data[:,5])
   
#    mocap_distance_interpolate = scipy.interpolate.interp1d(mocap_data[:,0],mocap_data[:,6],fill_value="extrapolate")
    return ati_data
#plt.plot(ati_data[:,0],mocap_distance_interpolate(ati_data[:,0]))
#plt.plot(mocap_distance_interpolate(ati_data[:,0]),ati_data[:,6])
#plt.plot(mocap_data[:,0],mocap_data[:,6])

#data_top = pd.read_csv(MOCAP_MSG).head()
#for row in data_top.columns:
#    print(row, end = " ")

if __name__ == '__main__':
    fname = sys.argv[1]
    ati_data = read_ros_bag_data(fname)
    draw_fft(ati_data,5)
    plt.figure()