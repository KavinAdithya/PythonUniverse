from datetime import datetime
import pymysql

try:
    print("Connecting to the database...")
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="KavinDharani@3",
        database="e_commerce_data"
    )
    print(connection)
    print("Connected to MySQL")

    cursor = connection.cursor()
    # cursor.execute("INSERT INTO employees1 VALUES(%s, %s, %s , %s)", (12, 'Kavin','CEO', 100000.0))
    # cursor.execute("SELECT * FROM Employees1")
    # # connection.commit()

    # cursor.execute("CREATE DATABASE e_commerce_data")
    # cursor.execute("SHOW DATABASES")

    table_creation : str = ('CREATE TABLE Bluetooth ('
                            'id int primary key auto_increment,'
                            'device_name TEXT(20),'
                            'model CHAR(20),'
                            'price DECIMAL(10, 2),'
                            'launch_data DATE)')
    insert_query : str = 'INSERT INTO Bluetooth(device_name, model, price, launch_data) VALUES(%s %s %s %s)'
    # cursor.execute('DESCRIBE bluetooth')
    # cursor.execute('ALTER TABLE Bluetooth modify launch_data TIMESTAMP')
    data : str = "" + str(datetime.now())
    print(data)
    cursor.execute(insert_query, ('One ', 'One Plus', 20000.00, '2024-10-24 16:49:41.754890'))
    # for row in cursor.fetchall():
    #     print(row)

except pymysql.MySQLError as e:
    print(f"Error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()
        print("MySQL connection is closed")
