#!/usr/bin/env python

import tornado
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
#import serial
#import time
import rospy

from photon_tcp.msg import data

class Server(TCPServer):
    """
    This is a simple echo TCP Server
    """
    message_separator = b'\r\n'

    def __init__(self, *args, **kwargs):
        self._connections = []
        super(Server, self).__init__(*args, **kwargs)

    @gen.coroutine
    def handle_stream(self, stream, address):
        """
        Main connection loop. Launches listen on given channel and keeps
        reading data from socket until it is closed.
        """
        try:
#            print('New request has come from our {} buddy...'.format(address))
            pub = rospy.Publisher('photon_tcp', data, queue_size=10)
            rospy.init_node('photon_node', anonymous=True)

            while not rospy.is_shutdown():
                try:
                    request = yield stream.read_until(self.message_separator)
                    message = data()
                    message.ip_address = str(address[0])
                    my_data = request.decode()
                    my_data = my_data.replace(self.message_separator,'')
                    message.data = my_data 
                    rospy.loginfo(message)
                    pub.publish(message)
                except StreamClosedError:
                    stream.close(exc_info=True)
                    return
                except rospy.ROSInterruptException:
                    pass
            self.stop()
#                    print(address,request.decode())
#            except StreamClosedError:
#                stream.close(exc_info=True)
#                return
#                else:
#                    try:
#                        yield stream.write(request)
#                    except StreamClosedError:
#                        stream.close(exc_info=True)
#                        return
        except Exception as e:
            if not isinstance(e, gen.Return):
                print("Connection loop has experienced an error.")
                print(e)
                raise


if __name__ == '__main__':
    Server().listen(5555)
    print('Starting the server...')
    try:
        IOLoop.instance().start()
        print('Server has shut down.')
    except KeyboardInterrupt:
        IOLoop.instance().stop()        
    except rospy.ROSInterruptException:
        pass
    

