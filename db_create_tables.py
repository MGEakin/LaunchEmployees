import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

# mycursor.execute("DROP DATABASE testing")
# mycursor.execute("CREATE DATABASE testing")

# # drop the table
# sql = "DROP TABLE IF EXISTS clients"
# mycursor.execute(sql)
# sql = "DROP TABLE IF EXISTS consultants"
# mycursor.execute(sql)
# sql = "DROP TABLE IF EXISTS employees"
# mycursor.execute(sql)
# sql = "DROP TABLE IF EXISTS studios"
# mycursor.execute(sql)

print("----------CREATE studios------------------")
sql = """CREATE TABLE studios (studio_id INT AUTO_INCREMENT PRIMARY KEY, \
        studio VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE disciplines------------------")
sql = """CREATE TABLE disciplines (discipline_id INT AUTO_INCREMENT PRIMARY KEY, \
        discipline VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE titles------------------")
sql = """CREATE TABLE titles (title_id INT AUTO_INCREMENT PRIMARY KEY, \
        title VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE roles------------------")
sql = """CREATE TABLE roles (role_id INT AUTO_INCREMENT PRIMARY KEY, \
        role VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE cost_alignment------------------")
sql = """CREATE TABLE cost_alignment ( \
        cost_alignment_id INT AUTO_INCREMENT PRIMARY KEY, \
        cost_alignment VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE employees------------------")
sql = """CREATE TABLE employees ( \
        employee_id INT AUTO_INCREMENT PRIMARY KEY, \
        employeeID VARCHAR(255), \
        first_name VARCHAR(255), \
        last_name VARCHAR(255), \
        email_address VARCHAR(255), \
        discipline_id INT, \
        role_id INT, \
        title_id INT, \
        cost_alignment_id INT, \
        FOREIGN KEY (discipline_id) REFERENCES disciplines(discipline_id), \
        FOREIGN KEY (role_id) REFERENCES roles(role_id), \
        FOREIGN KEY (title_id) REFERENCES titles(title_id), \
        FOREIGN KEY (cost_alignment_id) REFERENCES cost_alignment(cost_alignment_id) \
        )"""

mycursor.execute(sql)

sql = """ALTER TABLE studios ADD COLUMN studioLead INT"""
mycursor.execute(sql)

sql = "ALTER TABLE studios ADD FOREIGN KEY (studioLead) REFERENCES employees(employee_id)"
mycursor.execute(sql)

sql = """ALTER TABLE disciplines ADD COLUMN studio_id INT"""
mycursor.execute(sql)

sql = """ALTER TABLE disciplines ADD FOREIGN KEY (studio_id) REFERENCES studios(studio_id)"""
mycursor.execute(sql)

sql = """ALTER TABLE disciplines ADD COLUMN disciplineLead INT"""
mycursor.execute(sql)

sql = "ALTER TABLE disciplines ADD FOREIGN KEY (disciplineLead) REFERENCES employees(employee_id)"
mycursor.execute(sql)

print("----------CREATE company------------------")
sql = """CREATE TABLE clients ( \
        client_id INT AUTO_INCREMENT PRIMARY KEY, \
        client_name VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE requisition------------------")
sql = """CREATE TABLE requisitions ( \
        job_id INT PRIMARY KEY, \
        client_id INT, \
        date_added DATETIME, \
        openings INT)"""
mycursor.execute(sql)

sql = "ALTER TABLE requisitions ADD FOREIGN KEY (client_id) REFERENCES clients(client_id)"
mycursor.execute(sql)


mydb.commit()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

