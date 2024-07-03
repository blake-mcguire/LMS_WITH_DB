import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = 'LMS_DB'
    user = 'root'
    password = ''
    host = 'localhost'
    
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user=user,
            password=password,
            host=host
        
        )
        
        if conn.is_connected():
            print("Connected To MYSQL Database Succesfully!")
            return conn
    except Error as e:
        print(f'Error: {e}')

connect_db()