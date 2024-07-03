from mysql.connector import connect, Error
from DB_connection import connect_db



def search_for_book(conn):
    try:
        
        cursor = conn.cursor()
        book = input('Please Enter the book you would like to search')
        # search through the books table and return the book id for books with
        # the same title as the user input
        # return all and unpack the return and display it nicely
        query = """
        SELECT b.book_id, b.book_title, a.author_name
        FROM Books b
        JOIN Authors a ON b.author_id = a.author_id
        WHERE b.book_title LIKE %s
        """
        cursor.execute(query, ('%' + book + '%',))
        
        results = cursor.fetchall()
        
        if results:
            print("Found book/s:")
            for book_id, title, author_name in results:
                print(f"ID: {book_id}, Title: {title}, Author: {author_name}")
        else:
            print("No books found with that title.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
    
        