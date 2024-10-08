import mysql.connector  # Import the MySQL connector library to interact with MySQL databases

mydbconnection = mysql.connector.connect(  # Establish a connection to the MySQL server
    host="localhost",  # Specify the host where the MySQL server is running, 'localhost' for local development
    user="root",  # The MySQL username to connect with, usually 'root' by default
    passwd="password"  # The password for the 'root' MySQL user
)
print(mydbconnection)  # Print the connection object to confirm successful connection to the MySQL server

db_name = "python_test_db"  # Define the name of the database you want to create

mycursor = mydbconnection.cursor()  # Create a cursor object to execute SQL queries

sqlquery = "CREATE DATABASE " + db_name  # Define an SQL query to create a database by concatenating the database name

mycursor.execute(sqlquery)  # Execute the SQL query to create the database on the MySQL server
