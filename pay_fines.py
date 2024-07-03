from mysql.connector import connect, Error
from DB_connection import connect_db
def get_current_user_fines(cursor):
    try:
        query = "SELECT fines FROM Users WHERE is_active = True"
        cursor.execute(query)
        fine_amount = cursor.fetchone()
        return fine_amount[0] if fine_amount else 0
    except Error as e:
        print(f"Error in find current_user_fines: {e}")
    
def pay_fines(conn):
    try:
        cursor = conn.cursor()
        fine_amount = get_current_user_fines(cursor)
        if fine_amount > 0:
            print(f"Your Current fine amount is {fine_amount}. Would you like to pay now? Yes/No?")
            user_response = input("Enter: ").lower()
            if user_response == 'yes':
                update_query = "UPDATE Users SET fines = 0 WHERE is_active = True"
                cursor.execute(update_query)
                conn.commit()
                print("All debts cleared. A receipt will be emailed to you shortly!")
            elif user_response == 'no':
                return
            else:
                print('Enter a valid repsonse')
                
        else:
            print("No fines to be paid at the moment!")
    except Error as e:
        print(f"Error in pay_fines: {e}")
    finally:
        cursor.close()
            
        # need to get the fines of the current active user.
    # need to check if the users fine amount is greater than 0
    # if so display the amount to the user 
    # give a yes or no option to pay the fines off
    # if no return
    # if yes say: "A Receipt will be emailed to (user_email)"
    # set the users fine value to 0
    