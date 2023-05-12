import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE testing")
mycursor.execute("CREATE DATABASE testing")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
