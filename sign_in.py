from mysql.connector import connect, Error
from DB_connection import connect_db

def return_user_id(cursor, email_or_username):
    try:
        query = "SELECT user_id FROM Users WHERE username = %s OR email = %s"
        cursor.execute(query, (email_or_username, email_or_username))
        user_id = cursor.fetchone()
        if user_id:
            return user_id[0]
        else:
            return None
    except Error as e:
        print(f"Error in return_user_id: {e}")

def check_if_password_is_correct(cursor, user_id, password):
        try:
        
            query = "SELECT pw FROM Users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result and result[0] == password:
                return True  
            else:
                return False  
        except Error as e:
            print(f"Error in check_if_password_is_correct: {e}")
            return False  
        
def sign_in(conn):
    try:
        cursor = conn.cursor()
        email_or_username = input('Enter Your Email or username: ')
        password = input("Enter your password")
        # return the user_id asscoaiated with the input email or username input
        # if so check if the password is associate with the user_id 
        # if so update the user_ids is active status to True
        # give entry
        user_id = return_user_id(cursor, email_or_username)
        if user_id:
             if check_if_password_is_correct(cursor, user_id, password):
                set_active_query = "UPDATE Users SET is_active = %s WHERE user_id = %s"
                cursor.execute(set_active_query, (True, user_id))
                conn.commit()
                print("Login Succesful, Welcome!")
                return True
             else: 
                print("Incorrect Password, Try again!")
                return False
        else:
            print("User associated with that email/username could not be found!")
            return False
    except Error as e:
        print(f"Error in sign_in: {e}")