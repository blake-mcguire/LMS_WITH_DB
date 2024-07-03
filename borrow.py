from mysql.connector import connect, Error
from DB_connection import connect_db
from datetime import date, timedelta

current_date = date.today()
return_date = current_date + timedelta(days=10)

def set_book_availability(cursor, book_id):
    try:
        query = "UPDATE books SET is_available = False WHERE book_id = %s"
        cursor.execute(query, (book_id,))
    except Error as e:
        print(f'Error: {e}')
        
def count_active_loans(cursor, user_id):
    try:
        
        query = "SELECT COUNT(*) FROM Loans WHERE user_id = %s AND return_date IS NULL"
        cursor.execute(query, (user_id,))
        count = cursor.fetchone()[0]
        return count
    except Error as e:
        print(f"Error in count_active_loans: {e}")
        
def get_active_fines(conn, user_id):
    try:
        cursor = conn.cursor()
        query = 'SELECT fines FROM Users WHERE user_id = %s'
        cursor.execute(query, (user_id,))
        fines = cursor.fetchone()
        if fines:
            return fines[0]
        else:
            return 0
    except Error as e:
        print(f"Error occcured on get_active_fines: {e}")
                
def get_book_id(cursor, book_title):
    try:
        query = "SELECT book_id FROM Books WHERE book_title = %s"
        cursor.execute(query, (book_title,))
        books = cursor.fetchall()
        if books:
            return books
        else:
            print(f'It Looks like we dont have {book_title} in our library!')
            return None
    except Error as e:
        print(f"Error: {e}")

def get_active_user(cursor):
    try:
        query = "SELECT user_id FROM Users WHERE is_active = True"
        cursor.execute(query,)
        user_id = cursor.fetchone()
        return user_id[0]
    except Error as e:
        print(f"Error: {e}")
        
def borrow_book(conn):
    cursor = None
    try:
        cursor = conn.cursor()
        
        title = input('Please Enter The Title of the book you wish to borrow: ')
        books = get_book_id(cursor, title)
        if books is None:
            return
        book_id = books[0][0]
        
        user_id = get_active_user(cursor)
        if user_id is None:
            return
        
        total_fines = get_active_fines(conn, user_id)
        if total_fines > 0:
            print(f"You have active fines totaling {total_fines} please pay them before you can borrow a book")
            return
        
        loan_count = count_active_loans(cursor, user_id)
        if loan_count >= 3:
            print('You have 3 or more books checked out, to check out any more you must return a book/s')
            return
        
        set_book_availability(cursor, book_id)
        new_loan_query = """
        INSERT INTO Loans (user_id, book_id, loan_date, due_date)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(new_loan_query, (user_id, book_id, current_date, return_date))
        conn.commit()
        print(f"{title} has been loaned to you, Please remember to return it by {return_date}.")
    except Error as e:
        print(f"Error in borrow book: {e}")  
    finally:
        cursor.close() 
        
        # need to return all books and if the title is in their append a new item loans with all of the info about the loan
        # change the status of the book to False