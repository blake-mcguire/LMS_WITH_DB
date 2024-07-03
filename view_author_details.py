from mysql.connector import connect, Error
from DB_connection import connect_db

def view_author_details(conn):
    try:
        cursor = conn.cursor()
        author = input('Please Enter the author you would like to search: ')
        # search through the books table and return the book id for books with
        # the same title as the user input
        # return all and unpack the return and display it nicely
        query = """
        SELECT b.book_id, b.book_title, a.author_name, a.author_id
        FROM Books b
        JOIN Authors a ON b.author_id = a.author_id
        WHERE a.author_name LIKE %s
        """
        cursor.execute(query, ('%' + author + '%',))
        
        results = cursor.fetchall()
        
        if results:
            print(f"Found book/s by {author}:")
            for book_id, title, author_name, author_id in results:
                print(f"ID: {book_id}, Title: {title}, Author: {author_name}")
        else:
            print("No books found by that author.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()