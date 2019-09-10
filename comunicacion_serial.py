from Base_datos import Database

if __name__=='__main__':

    database = Database(ip='william-basedatos.cjg37luxzfuj.us-west-2.rds.amazonaws.com', user="william69", password="12348517", database="PLC")
    data = database.execute_query("SELECT * FROM PLC", False)

    print(database.database)

    for i in data:
        print(i)