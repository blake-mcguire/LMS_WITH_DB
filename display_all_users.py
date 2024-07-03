from mysql.connector import connection, Error
from DB_connection import connect_db

def view_all_users(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT username FROM Users"
        cursor.execute(query)
        usernames = cursor.fetchall()
        for user in usernames:
            print(f'{user[0]}\n')
    except Error as e:
        print(f'Error occured in view_all_user: {e}')
    finally:
        cursor.close()
        