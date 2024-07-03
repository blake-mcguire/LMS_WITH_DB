from mysql.connector import connect, Error
from DB_connection import connect_db
def instantiate_author(cursor, name):
    try:
        insert_query = "INSERT INTO Authors (author_name) VALUES (%s)"
        cursor.execute(insert_query, (name,))
        print('Author added!')
    except Error as e:
        print(f"Error in instantiate_author: {e}")
def check_if_author_exists(cursor, name):
    try:
        query = "SELECT author_id FROM Authors WHERE author_name = %s"
        cursor.execute(query, (name,))
        author_id = cursor.fetchall()
        return author_id
    except Error as e:
        print(f"Error in check_if_author_exists: {e}")
        
def add_author(conn):
    try:
        cursor = conn.cursor()
        author = input("Enter the name of the author you would like to add...")
        if check_if_author_exists(cursor, author):
            print(f"{author} is already in our records!")
        else:
            instantiate_author(cursor, author)
    except Error as e:
        print(f'Error in add_author: {e}')
    finally:
        cursor.close()