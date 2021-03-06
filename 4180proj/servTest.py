#python pc server testing code
#( echo server that echoes what you send to it back to you )
import socket
import sys
import argparse
import fcntl
import struct
import serial
import time

ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)


#parser = argparse.ArgumentParser()
#parser.add_argument("a0")
#args = parser.parse_args()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ipAddress =  get_ip_address('wlan0')
print ('server ipAddress is %s' % ipAddress)
#ipAddress = args.a0
port = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ipAddress, port)
print('starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        connection.close()
        
