import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

# drop the table
sql = "DROP TABLE IF EXISTS clients"
mycursor.execute(sql)
sql = "DROP TABLE IF EXISTS consultants"
mycursor.execute(sql)
sql = "DROP TABLE IF EXISTS studios"
mycursor.execute(sql)

print("----------CREATE studios------------------")
sql = """CREATE TABLE studios (studio_id INT AUTO_INCREMENT PRIMARY KEY, \
        studio VARCHAR(255))"""
mycursor.execute(sql)

# sql = """CREATE TABLE consultant_studio ( \
#         consultant_id INT PRIMARY KEY FOREIGN KEY REFERENCES consultants(consultant_id), \
#         studio_id INT PRIMARY KEY FOREIGN KEY REFERENCES studios(studio_id)"""
# mycursor.execute(sql)

print("----------CREATE disciplines------------------")
sql = """CREATE TABLE disciplines (discipline_id INT AUTO_INCREMENT PRIMARY KEY, \
        discipline VARCHAR(255))"""
mycursor.execute(sql)

# sql = """CREATE TABLE consultant_discipline ( \
#         consultant_id INT PRIMARY KEY FOREIGN KEY REFERENCES consultants(consultant_id), \
#         discipline_id INT PRIMARY KEY FOREIGN KEY REFERENCES disciplines(discipline_id)"""
# mycursor.execute(sql)

print("----------CREATE titles------------------")
sql = """CREATE TABLE titles (title_id INT AUTO_INCREMENT PRIMARY KEY, \
        title VARCHAR(255))"""
mycursor.execute(sql)

# sql = """CREATE TABLE consultant_title ( \
#         consultant_id INT PRIMARY KEY FOREIGN KEY REFERENCES consultants(consultant_id), \
#         title_id INT PRIMARY KEY FOREIGN KEY REFERENCES titles(title_id)"""
# mycursor.execute(sql)

print("----------CREATE roles------------------")
sql = """CREATE TABLE roles (role_id INT AUTO_INCREMENT PRIMARY KEY, \
        roles VARCHAR(255))"""
mycursor.execute(sql)

# sql = """CREATE TABLE consultant_role ( \
#         consultant_id INT PRIMARY KEY FOREIGN KEY REFERENCES consultants(consultant_id), \
#         role_id INT PRIMARY KEY FOREIGN KEY REFERENCES roles(role_id)"""
# mycursor.execute(sql)

print("----------CREATE cost_alignment------------------")
sql = """CREATE TABLE cost_alignment ( \
        cost_alignment_id INT AUTO_INCREMENT PRIMARY KEY, \
        cost_alignment VARCHAR(255))"""
mycursor.execute(sql)

# sql = """CREATE TABLE consultant_cost_alignment ( \
#         consultant_id INT PRIMARY KEY FOREIGN KEY REFERENCES consultants(consultant_id), \
#         cost_alignment_id INT PRIMARY KEY FOREIGN KEY REFERENCES cost_alignment(cost_alignment_id)"""
# mycursor.execute(sql)

print("----------CREATE consultants------------------")
sql = """CREATE TABLE consultants ( \
        consultant_id INT AUTO_INCREMENT PRIMARY KEY, \
        employeeID VARCHAR(255), \
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        email_address VARCHAR(255), \
        studio_id INT, \
        discipline_id INT, \
        role_id INT, \
        title_id INT, \
        cost_alignment_id INT, \
        FOREIGN KEY (studio_id) REFERENCES studios(studio_id), \
        FOREIGN KEY (discipline_id) REFERENCES disciplines(discipline_id), \
        FOREIGN KEY (role_id) REFERENCES roles(role_id), \
        FOREIGN KEY (title_id) REFERENCES titles(title_id), \
        FOREIGN KEY (cost_alignment_id) REFERENCES cost_alignment(cost_alignment_id) \
        )"""

mycursor.execute(sql)

# mycursor.execute("ALTER TABLE consultants ADD COLUMN consultantID INT AUTO_INCREMENT PRIMARY KEY")
#
# mycursor.execute(sql)

mydb.commit()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

