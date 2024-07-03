from mysql.connector import connect, Error
from DB_connection import connect_db 
from datetime import date
current_date = date.today()

def set_book_availability(cursor, book_id):
    try:
        query = "UPDATE books SET is_available = True WHERE book_id = %s"
        cursor.execute(query, (book_id,))
    except Error as e:
        print(f'Error: {e}')
        
def get_active_user(cursor):
    try:
        query = "SELECT user_id FROM Users WHERE is_active = True"
        cursor.execute(query,)
        user_id = cursor.fetchone()
        print(user_id)
        return user_id
    except Error as e:
        print(f"Error: {e}")

def check_who_is_on_loan(cursor, book_id):
    try:
        query = "SELECT user_id FROM Loans WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        user_id = cursor.fetchone()
        print(user_id)
        return user_id
    except Error as e:
        print(f"Error: {e}")            

def set_loan_as_returned(cursor, book_id):
    query = "UPDATE Loans SET return_date = %s WHERE book_id = %s"
    cursor.execute(query, (current_date, book_id))
    print("Loan status set to returned!")

def get_due_return_differential(cursor, book_id):
    try:
        query = """
        SELECT DATEDIFF(return_date, due_date) AS overdue_days
        FROM Loans
        WHERE book_id = %s AND return_date IS NOT NULL
        """
        cursor.execute(query, (book_id,))
        result = cursor.fetchone()
        print(result)
        
        if result:
            overdue_days = result[0]
            if overdue_days > 0:
                fine_amount = overdue_days * 3
                print(f"You were {overdue_days} late, and incurred a fine amount of {fine_amount}")
                return fine_amount
            else:
                print('Book returned on Time, No fines Incurred')
        else:
            print("No Loan found for this Book!")
    except Error as e:
        print(f"Error: {e}")

def add_fine_to_user(cursor, user_id, amount):
    try:
        query = """
        UPDATE Users
        Set fines = fines + %s
        WHERE user_id = %s
        """ 
        cursor.execute(query, (amount, user_id))
    except Error as e:
        print(f"Error: {e}")
              
def book_loan_validation(cursor, book_title):
    try:
        query = "SELECT book_id, is_available FROM Books WHERE book_title = %s"
        cursor.execute(query, (book_title,))
        result = cursor.fetchone()
        print(result)
        if result:
            book_id, is_available = result
            if not is_available and get_active_user(cursor) == check_who_is_on_loan(cursor, book_id):
                set_loan_as_returned(cursor, book_id)
                fine_add = get_due_return_differential(cursor, book_id)
                print(fine_add)
                if fine_add and fine_add > 0:
                    add_fine_to_user(cursor, get_active_user(cursor), fine_add)
                    set_book_availability(cursor, book_id)
            else:
                print("This book Isn't currently loaned to you!")
        else:
            print('It doesnt look like we have that book in our library!')
    except Error as e:
        print(f"Error: {e}")
        




def return_book(conn):
    try:
        cursor = conn.cursor()
        
        title = input('Please Enter The Title of the book you would like to return: ')
        book_loan_validation(cursor, title)
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        