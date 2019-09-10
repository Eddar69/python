
import serial

class com_serial(object):


    def __init__ (self, port, boudrate, bytesize, parity ):

        self.port = port
        self.boudrate = boudrate
        self.bytesize =bytesize
        self.parity = parity

    def READ_PORT(self):

        ser = serial.Serial(self.port,self.boudrate,)

        print("entra")
       # serialPort = serial.Serial(com14, 9600)
       #
       #  while True:
       #      print(serialPort.readline())
       #
       #  try:


