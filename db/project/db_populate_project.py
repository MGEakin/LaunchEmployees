import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()
#
# print("----------INSERT office------------------")
# sql = "INSERT INTO offices (code, office) VALUES (%s, %s)"
# val = [
#   ("ATL", "Atlanta"),
#   ("CHI", "Chicago"),
#   ("COL", "Columbus"),
#   ("SEA", "Seattle"),
#   ("DAL", "Dallas"),
#   ("MIN", "Minneapolis")
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
