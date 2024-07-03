from mysql.connector import connect, Error
from DB_connection import connect_db

def view_all_authors(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT author_name FROM Authors"
        cursor.execute(query)
        authors = cursor.fetchall()
        for a in authors:
            print(f'{a[0]}\n')
    except Error as e:
        print(f'Error occured in view_all_user: {e}')
    finally:
        cursor.close()