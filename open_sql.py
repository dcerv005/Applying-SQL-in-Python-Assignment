import mysql.connector
from mysql.connector import Error
#Question 1
def connect_database():
   
    db_name = 'fitness_center_db'
    user = 'root'
    password = 'my_root_password'
    host= 'localhost'


    try:
        conn = mysql.connector.connect (
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connected to MySQL Databse successfully.")
            return conn

    except Error as e:
        print(f'Error {e}')
        return None

