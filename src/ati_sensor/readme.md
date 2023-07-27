Author: Dongting Li, dongting@asu.edu
# ati_sensor package quick start


This package is based on the ati pyhon code in "code_equipment" with some small modification. The main feature:
1. connect to an ati sensor with given IP
2. auto calibration when intilized
3. ondemand calibration

Some info:
The topic is called "ati_node_chatter"
The node is "ati_node".
The sampleing rate is 1000 Hz

## usage
1. Start connection: 
```bash
roslaunch ati_sensor ati_sensor.launch ati_ip:=192.168.1.122
```
This will start a connection to ati sensor with an ip of "192.168.1.122", which is the default IP of ATI Gamma.

Known issue is, it only allows one ati sensor connection at a time, but will you really use two sensor at a time? 
2. Calibration on deman:
You can use:
```bash
rosservice call /calibrate_ati
```
to perform a calibration on demand

3. To see your data, you can use either:

```bash
rostopic echo /ati_node_chatter
```
or 
```bash
rqt_plot rqt_plot /ati_node_chatter
```