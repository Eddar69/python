import psycopg2
import serial
class COM(object):


    def __init__ (self, port=None, boudrate=9600, bytesize=None, parity= parity_one, ):

                self.port = 'com14'
                self.boudrate = boudrate
                self.bytesize =bytesize
                self.parity = parity

    def READ_PORT(self):
        serialPort = serial.Serial(com14, 9600)

        while True:
            print(serialPort.readline())

        try:
            connection = psycopg2.connect(user="william69",
                                          password="12348517",
                                          host="william-basedatos.cjg37luxzfuj.us-west-2.rds.amazonaws.com",
                                          port="5432",
                                          database="plc")
            cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO plc (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
        record_to_insert = (5, 'One Plus 6', 950)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

