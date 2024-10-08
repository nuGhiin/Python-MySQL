import mysql.connector  # Import the MySQL connector library to interact with MySQL databases

db_name = "python_test_db"  # Define the name of the database to connect to

mydbconnection = mysql.connector.connect(  # Establish a connection to the MySQL server
    host="localhost",  # The host where the MySQL server is running, usually 'localhost' for local development
    user="root",  # The MySQL username to connect with, typically 'root' for default
    passwd="password",  # The password for the MySQL user 'root'
    database=db_name  # The database to use for the connection (previously defined as 'python_test_db')
)

mycursor = mydbconnection.cursor()  # Create a cursor object to execute SQL queries

sqlquery = """  # Define an SQL query to create a table named 'Student'
            CREATE TABLE Student
            (
            Roll varchar(4),  # Create a 'Roll' column with a max length of 4 characters
            Name varchar(4)   # Create a 'Name' column with a max length of 4 characters
            )
            """

mycursor.execute(sqlquery)  # Execute the SQL query to create the table

print("table created!")  # Output a message indicating that the table has been successfully created
