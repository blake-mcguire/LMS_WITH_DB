from mysql.connector import connect, Error
from DB_connection import connect_db

def sign_out(conn):
    try:
        
        cursor = conn.cursor()
        query = "UPDATE Users SET is_active = False WHERE is_active = True"
        cursor.execute(query)
        conn.commit()
        
        print("Signed Out, Returning to main menu...")
    except Error as e:
        print(f"Error in sign_out: {e}")
    finally:
        cursor.close()        
       