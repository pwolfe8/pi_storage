import time
import serial

ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
while True:
#  msg = 'hello thar'
 # print 'sending: ', msg
#  ser.write(msg)
  data = ser.read(16)
  print 'received: ', data
  print 'sending: ', data
  ser.write(data)
#  time.sleep(1)
  
