# LIBRARY MANAGEMENT SYSTEM WITH DATABASE
This Project Was Made As Part Of The Coding Temple SWE Bootcamp As Part Of The Backend-Core Weekend Assignments.

### PURPOSE
The Purpose of this Project was to further elaborate on the previous project, Library Management System but rather than using classes 
and objects to store data about books and users we are now storing all library related data in a MySQL database for easier access and data maintainability

### PREMISE

This Program is meant to simulate a mock online library management system via 
the command line interface.

-It allows users to create multiple accounts
-Add and check out books from the library
-and Subsequently return said books. 

Here is a list of the full functionality:

- Adding a new book with all relevant details.
- Allowing users to borrow a book, marking it as "Borrowed."
- Allowing users to return a book, marking it as "Available."
- Searching for a book by its unique identifier (title) and displaying its  details.
- Adding a new user with user details.
- Viewing user details.
- Displaying a list of all users.
- Adding a new author with author details.
- Viewing author details.
- Displaying a list of all authors.
- Quitting the application.

And additional functionality that is new to the version of this application that is linked to a database including...
  
- The ability for a user to accrue and pay off fines for late book returns
- User Authentication

### MODULARITY
The modularity of this project is broken down into files by each notable function a user will call and consolidated 
by the table the function is most associated with

USER OPERATIONS
- sign_up.py
- sign_in.py
- pay_fines.py
- create_account.py
- display_account_details.py
- display_all_users.py

AUTHOR OPERATIONS
- add_author.py
- view_all_authors.py
- view_author_details.py

BOOK OPERATIONS
- add_book.py
- borrow.py
- return_book.py
- search_for_book.py

### HOW TO USE

- To begin using this project start by cloning this github repository onto your local machine
- Install MySQL Connector into the Folder you are housing this Program using this command - pip install mysql-connector-python

1. Once the Repository is loaded onto your local machine Create a MySQL database following the instructions below...
   
   Create the database in a MySQL Workbench using the following prompt

   CREATE DATABASE LMS_DB

2. Now that you have your database created you must create 4 tables within that database, use the following commands:

CREATE TABLE Books(
    book_id INT auto_increment PRIMARY KEY,
    book_title VARCHAR(100) NOT NULL,
    author_id INT,
    genre_id INT,
    is_available Boolean DEFAULT TRUE,
    FOREIGN KEY author_id REFERENCES Authors(author_id),
    FOREIGN KEY genre_id REFERENCES Genres(genre_id)
);

CREATE TABLE Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);

CREATE TABLE Genres(
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL
);

CREATE TABLE Users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    pw VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    fines DECIMAL DEFAULT 0.00
    );

CREATE TABLE Loans(
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    loan_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    overdue_days INT,
    FOREIGN KEY user_id REFERENCES Users(user_id)
    FOREIGN KEY book_id REFERENCES Books(book_id)
);

3. Now That Your Table is set up and your database is correctly configured Update the connection data in the DB_connection.py file
    to correctly reflect your specs

   def connect_db():    
    db_name = 'LMS_DB'      
    user = 'root'         <----- UPDATE THIS TO REFLECT YOUR SPECIFICATIONS
    password = ''       
    host = 'localhost'  

    
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user=user,
            password=password,
            host=host
        
        )
        
        if conn.is_connected():
            print("Connected To MYSQL Database Succesfully!")
            return conn
    except Error as e:
        print(f'Error: {e}')

connect_db()

4. once your connection has been made open the main.py file and press run and voila you have a working library management system!
