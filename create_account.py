from mysql.connector import connect, Error
from DB_connection import connect_db
import re
def insantiate_new_user(cursor, conn, username, email, password):
    try:
        insert_query = "INSERT INTO Users (username, email, pw, is_active) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (username, email, password, True))
        conn.commit()
        print(f"New user created, Welcome {username}")
    except Error as e:
        print(f'Error in instantiate_new_user: {e}')

def check_if_email_exists(cursor, email):
    try:
        query = "SELECT user_id FROM Users WHERE email = %s"
        cursor.execute(query, (email,))
        email = cursor.fetchall()
        if email:
            return True
        else:
            return False
    except Error as e:
        print(f"Error in check_if_email_exists: {e}")


def check_if_username_exists(cursor, username):
    try:
        query = "SELECT user_id FROM Users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchall()
        if user:
            return True
        else:
            return False
    except Error as e:
        print(f'Error in check_if_username_exists: {e}')
            

def create_account(conn):
    try:
        cursor = conn.cursor()
        # need to take inputs of username password and email
        # if there is already a user with that email
        # or a user with that username you may not create the account
        # check if any users with the name exist
        # if not check if any users with the email exist
        # if not add the account to the users table 
        # update the user to reflect that is the active user
        user_name = input("Enter The Username you would like to have: ")
        email_ = input("Enter Your Email: ")
        pass_word = input("""Enter the a strong password 
    (At least 8 Characters, 1 special character, and 1 uppercase)
    Enter Here: """) #Need to regex validate the password and the email
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#~+=])[A-Za-z\d@$!%*?&#~=+]{8,}$")
        if not password_pattern.match(pass_word):
            print('Password is Weak! Try again...')
        elif check_if_username_exists(cursor, user_name):
            print("That Username is taken!")
        elif check_if_email_exists(cursor, email_):
            print("An account with that email already exists!")
        else: 
            insantiate_new_user(cursor, conn, user_name, email_, pass_word)
            return True
    except Error as e:
        print(f"Error in create_account: {e}")
    finally:
        cursor.close() 
        
        