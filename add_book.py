from mysql.connector import connect, Error
from DB_connection import connect_db  # Assuming connect_db is your function to connect to the DB

def get_or_create_author(cursor, author_name):
    try:
        query = "SELECT author_id FROM Authors WHERE author_name = %s"
        cursor.execute(query, (author_name,))
        author = cursor.fetchone()
        if author:
            return author[0]
        else:
            insert_query = "INSERT INTO Authors (author_name) VALUES (%s)"
            cursor.execute(insert_query, (author_name,))
            return cursor.lastrowid
    except Error as e:
        print(f"Error in get_or_create_author: {e}")

def get_or_create_genre(cursor, genre_name):
    try:
        query = "SELECT genre_id FROM Genres WHERE genre_name = %s"
        cursor.execute(query, (genre_name,))
        genre = cursor.fetchone()
        if genre:
            return genre[0]
        else:
            insert_query = "INSERT INTO Genres (genre_name) VALUES (%s)"
            cursor.execute(insert_query, (genre_name,))
            return cursor.lastrowid
    except Error as e:
        print(f"Error in get_or_create_genre: {e}")

def add_book(conn):
    try:
        cursor = conn.cursor()

        book_name = input('Please enter the Title of the book: ')
        author_name = input('Enter the name of the author who wrote the book: ')
        genre_name = input('What Genre is the book in?: ')

        author_id = get_or_create_author(cursor, author_name)
        genre_id = get_or_create_genre(cursor, genre_name)

        insert_query = """
            INSERT INTO Books (book_title, author_id, genre_id, is_available)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (book_name, author_id, genre_id, True))

        conn.commit()
        print("Book added successfully!")

    except Error as e:
        print(f"Error in add_book: {e}")
    finally:
        cursor.close()

def main():
    try:
        conn = connect_db()
        add_book(conn)
    except Error as e:
        print(f"Error in main: {e}")
    finally:
        if conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()