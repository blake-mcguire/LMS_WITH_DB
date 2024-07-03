from mysql.connector import connect, Error
from DB_connection import connect_db
import add_book, borrow, create_account, display_account_details, display_all_users, pay_fines, return_book, sign_in, sign_out, search_for_book, add_author, view_author_details, view_all_authors

# opens up to the sign up/sign page
# once user has succesfully signed in opens to the operations selection page
# book operations -
# Welcome to book operations!
# Enter the corresponding number for the action you would like to take:
# 1. Add Book To Library
# 2. Borrow Book
# 3. search for a book
# 4. Return a book
# return to main menu

# user operations
# 1.sign out
# 2. display account details
# 3. display all users
# 4. pay fines
# return to main menu
def set_all_users_inactive(conn):
    try:
        cursor = conn.cursor()
        update_query = "UPDATE users SET is_active = False WHERE is_active = True"
        cursor.execute(update_query)
        conn.commit()
        print("All users have been set to inactive.")
    except Error as e:
        print(f"Error updating user status: {e}")
    
    

def main():
    while True:

        user_signed_in = False
        while not user_signed_in:
            print("Welcome to Blakes Extroardinary library!")
            print('Press 1 to sign-up')
            print('Press 2 to sign-in')
            user_choice = input('1 or 2?: ')
        
            try:
                conn = connect_db()
                if user_choice == '1':
                    user_signed_in = create_account.create_account(conn)
                elif user_choice == '2':
                    user_signed_in = sign_in.sign_in(conn)
                else:
                    print('Invalid choice enter 1 or 2...')
                if user_signed_in:
                    main_menu(conn)
            except Error as e:
                print(f"Error: {e}")
            

def main_menu(conn):
    while True:
        print("\nMain Menu")
        print('1. User Operations')
        print('2. Author Operations')
        print('3. Book Operations')
        print('4. Exit Library')
        
        choice = input("\nPlease enter a number corresponding with your choice (1-4):")
        
        if choice == '1':
            user_operations(conn)
        elif choice == '2':
            author_operations(conn)
        elif choice == '3':
            book_operations(conn)
        elif choice == '4':
            print('Exiting Blakes WOnderful superb most extroardinary library...')
            set_all_users_inactive(conn)
            if conn.is_connected():
                conn.close()
            break
        else: 
            print('Please enter a valid input...')
            
            
def user_operations(conn):
    while True:
        print('USER OPERATIONS')
        print('\n1. Sign Out')
        print('2. View Account Details')
        print('3. Display all users')
        print('4. Pay Fines')
        print('5. Return to main menu...')
        
        user_op_choice = input('\nEnter Your choice: ')
        if user_op_choice == '1':
            sign_out.sign_out(conn)
            break
        elif user_op_choice == '2':
            display_account_details.display_account_details(conn)
        elif user_op_choice == '3':
            display_all_users.view_all_users(conn)
        elif user_op_choice == '4':
            pay_fines.pay_fines(conn)
        else:
            return True

def book_operations(conn):
    while True:
        try:
            print('BOOK OPERATIONS')
            print('\n1. Add Book')
            print('2. Borrow Book')
            print('3. Return Book')
            print('4. Search For Book')
            print('5. Return To main menu')
            book_op_choice = input('\nEnter your choice:')
            if book_op_choice == '1':
                add_book.add_book(conn)
            elif book_op_choice == '2':
                borrow.borrow_book(conn)
            elif book_op_choice == '3':
                return_book.return_book(conn)
            elif book_op_choice == '4':
                search_for_book.search_for_book(conn)
            elif book_op_choice == '5':
                return
            else:
                print('Please Enter a Valid Input!')

        except Error as e:
            print(f'Error on book_operations: {e}')
        
            
        
def author_operations(conn):
    try:
        print("AUTHOR OPERATIONS")
        print('\n1. Add Author')
        print('2. Search For An Author')
        print('3. View All Author Details')
        print('4. Return to Main menu')
        
        author_op_choice = input('\nWhat would you like to do?: ')
        
        if author_op_choice == '1':
            add_author.add_author(conn)
        elif author_op_choice == '2':
            view_author_details.view_author_details(conn)
        elif author_op_choice == '3':
            view_all_authors.view_all_authors(conn)
        elif author_op_choice == '4':
            return
    except Error as e:
        print(f'Error Occured: {e}')
if __name__ == "__main__":
    main()

main

# add_author needs to be debugged
# View_author_details needs to be debugged
