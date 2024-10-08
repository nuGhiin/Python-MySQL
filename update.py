import mysql.connector
db_name ="python_test_db"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database=db_name
)

mycursor = mydbconnection.cursor()

sqlquery = """ 
            UPDATE Student
            SET Name ='KKP'
            WHERE Name ='tANJ'
            """

mycursor.execute(sqlquery) 
mydbconnection.commit() # database er kuno entry change hole as update, insert hole comit korte hoy

print("data updated!")