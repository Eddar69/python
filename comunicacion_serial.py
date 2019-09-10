from Base_datos import Database
import serial
import psycopg2

ser = serial.Serial("com14", baudrate=9600, timeout=0.2, parity='N')

if __name__=='__main__':
    while True:
        Datos = ser.readline().decode("utf-8") # llega bit se vuelve string por el decode


        if len(Datos) > 0: # aseguro datos sean mayores que cero
            print(Datos)
            Array = Datos.split(',')  # datos es palbra y el split hace un arreglo lo uqe esta las comas
            humedad = Array[2]
            Temperatura = Array[1]  # primera posicion temp
            Modelo = Array[0]  # posicion 0 para modelo

            connection = psycopg2.connect(user="william69",
                                               password="12348517",
                                               host="william-basedatos.cjg37luxzfuj.us-west-2.rds.amazonaws.com",
                                               port="5432",
                                               database="PLC")
            cursor = connection.cursor()

            postgres_insert_query = ' INSERT INTO plc (modelo, temperatura, humedad) VALUES (%s,%s,%s)'
            record_to_insert = (Modelo, float(Temperatura), float(humedad)) # conversion la palabra a numeros enteros
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()


    # database = Database(ip='william-basedatos.cjg37luxzfuj.us-west-2.rds.amazonaws.com', user="william69", password="12348517", database="PLC")
    # data = database.execute_query("SELECT * FROM PLC", False)
    #
    # print(database.database)
    #
    # for i in data:
    #     print(i)