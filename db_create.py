import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

# drop the table
sql = "DROP TABLE IF EXISTS consultants"
mycursor.execute(sql)

print("----------CREATE------------------")
sql = "CREATE TABLE consultants (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "ResourceEmployeeID VARCHAR(255),"\
    "ResourceFirstName VARCHAR(255),"\	
"ResourceLastName VARCHAR(255),"\
    "ResourceEmailAddress"
mycursor.execute(sql)

sql = "CREATE TABLE studios (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Studio VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE disciplines (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Discipline VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE titles (title_id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Title VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE resource_title (resource_id INT PRIMARY KEY,"\
    "title_id INT PRIMARY KEY"
mycursor.execute(sql)

sql = "CREATE TABLE roles (role_id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Roles VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE resource_role (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "resource_id INT,"\
    "role_id VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE resourceCostAlignment (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "CostAlignment VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE titles (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Title VARCHAR(255)"
mycursor.execute(sql)

sql = "CREATE TABLE titles (id INT AUTO_INCREMENT PRIMARY KEY,"\
    "Title VARCHAR(255)"
mycursor.execute(sql)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

