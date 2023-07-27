'''
Created on Fri May 14 14:44:06 2021
@author: Dongting Li; dongting@asu.edu.
For future idealab student, feel free to contact me for questions.
'''

import socket
import numpy
import time

class atiSensor:
    def __init__(self, tcp_ip='192.168.1.122', max_retries=3):
        """
        "192.168.1.121 is the default ATI sensor IP address"
        Initialize the atiSensor object, establish the connection and perform calibration.

        TCP_IP: IP address of the sensor.
        max_retries: Maximum number of retries to establish a connection.
        """
        self.max_retries = max_retries
        self.calib_data = [0,0,0,0,0,0]
        self.TCP_IP = tcp_ip
        self.CALIBRATE_NUM = 10000  # Number of samples for calibration
        self.TCP_PORT = 49152  # TCP port for the sensor
        self.BUFFER_SIZE = 1024  # Buffer size for data received from the sensor
        self.ORDER = 'big'  # Byte order for data received from the sensor
        self.COUNTS_PER_UNIT = numpy.array([1000000] * 6)  # Unit conversion factors for sensor data
        self._init_connection()  # Establish the connection
        self._calibrate()  # Perform calibration

    def _init_connection(self):
        """
        Establish a connection to the sensor, with retries in case of timeout.
        """
        print("Initializing ATI sensor")
        print("Start connection to " + self.TCP_IP)
        retries = 0
        while retries < self.max_retries:
            try:
                # Construct the connection message
                message = b''
                message += (0x1234).to_bytes(2, byteorder=self.ORDER, signed=False)
                message += (2).to_bytes(2, self.ORDER)
                message += (1).to_bytes(4, self.ORDER)

                # Establish the connection
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(2)
                s.connect((self.TCP_IP, self.TCP_PORT))
                print("Sensor connected")

                # Save the socket and message for future use
                self.s = s
                self.message = message
                return
            except socket.timeout:
                print("Connection timeout, retrying...")
                retries += 1
                time.sleep(1)  # Wait before trying to reconnect
        # If we've exhausted all retries, raise an error
        raise ConnectionError(f"Could not connect to the sensor at {self.TCP_IP} after {self.max_retries} attempts.")

    def _extract_raw(self, packet):
        """
        Extract the raw sensor data from a packet.

        packet: Byte data received from the sensor.
        """
        raw = []
        for ii in range(6):
            byte = packet[12 + ii * 4:12 + ii * 4 + 4]
            #  This line is slicing a chunk of 4 bytes from the packet for each iteration of the loop.
            #  For example, during the first iteration (when ii is 0), it will take the bytes from index 12 to 15.
            #  In the next iteration, it will take bytes from index 16 to 19, and so on.
            value = int.from_bytes(byte, byteorder=self.ORDER, signed=True)
            raw.append(value)
            # raw will contain 6 integer values, each derived from a 4-byte chunk of the packet. These values are the raw measurements from the sensor.
        return raw

    def _calibrate(self):
        """
        Calibrate the sensor. Once this function is called, the sensor will be automatically calibrated.
        """
        calib_data_list = []
        for j in range(0, self.CALIBRATE_NUM):
            self.s.send(self.message)
            data = self.s.recv(self.BUFFER_SIZE)
            data2 = numpy.array(self._extract_raw(data))
            calib_data_list.append(data2)
        calib_data = numpy.array(calib_data_list)
        scaled_data = calib_data / self.COUNTS_PER_UNIT
        self.calib_data = numpy.sum(scaled_data, axis=0) / self.CALIBRATE_NUM
        print("Calibration finished, current offset is",self.calib_data)

    def get_data(self):
        """
        Retrieve calibrated data from the sensor.
        """
        self.s.send(self.message)
        data = self.s.recv(self.BUFFER_SIZE)
        data2 = numpy.array(self._extract_raw(data))
        ati_data = data2 / self.COUNTS_PER_UNIT-self.calib_data
        return ati_data

if __name__ == '__main__':
    # Refer to readme for sensor connection, the TCP_IP is the ip address for the sensor, you should set it in your ethernet adapter's IP v4 manual settings
    # Once you set it, you should be able to access it using your browser.
    # ATI has a switch on board to control the IP address, check out their manula to see how to set it.
    TCP_IP = "192.168.1.122"  # IP address of the sensor
    ati_sensor = atiSensor(TCP_IP)  # Create an atiSensor object

    # Here is just an example of calling calivration, althought the sensor init calibrate the sensor already.
    try:
        ati_sensor._calibrate()
    except:
        raise ConnectionError(f"Unable to calibrate")
    while True:
        force = ati_sensor.get_data()  # Retrieve calibrated data
        time.sleep(0.01)
        print(force)  # Print the data

    # To use the code out of this main function, simply use "from read_ati_class import atiSensor"
