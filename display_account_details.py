from mysql.connector import connection, Error
from DB_connection import connect_db

def display_account_details(conn):
    try:
        cursor = conn.cursor()
        
        query = "SELECT username, pw, email, fines FROM Users WHERE is_active = True"
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            for row in results:
                name, pw, email, fines = row
                print(f"""
ACCOUNT DETAILS:
USERNAME: {name}
PASSWORD: {pw}
EMAIL: {email}
FINES OWED: {fines}""")
        else:
            print("Im Really hoping this line never prints but there are no active users")
    except Error as e:
        print(f"Error in display_account_details: {e}")
    finally:
        cursor.close()
            