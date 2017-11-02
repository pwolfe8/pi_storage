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

def readlineCR():
	rv = ""
	while True:
		ch=ser.read()
		rv += ch
		if ch == '\r' or ch == '':
			return rv


while True:
	rcv = readlineCR()
	ser.write(rcv)
	print(rcv)
