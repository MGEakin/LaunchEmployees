import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

print("----------CREATE burden_type------------------")
sql = """CREATE TABLE burden_types (burden_type_id INT AUTO_INCREMENT PRIMARY KEY, \
        code VARCHAR(255), \
        burden_type VARCHAR(255), \
        burden INT)"""
mycursor.execute(sql)

print("----------INSERT burden_type------------------")
sql = "INSERT INTO burden_types (code, burden_type, burden) VALUES (%s, %s, %s)"
val = [
  ("SUB", "Sub Contractor", 5),
  ("W2", "W2 - Project Employee", 20),
  ("FTE", "Full Time Employee", 30),
  ("LDR", "Leader", 0)
]

mycursor.executemany(sql, val)

print("----------CREATE office------------------")
sql = """CREATE TABLE offices (office_id INT AUTO_INCREMENT PRIMARY KEY, \
        code VARCHAR(255), \
        office VARCHAR(255))"""
mycursor.execute(sql)

print("----------INSERT office------------------")
sql = "INSERT INTO offices (code, office) VALUES (%s, %s)"
val = [
  ("ATL", "Atlanta"),
  ("CHI", "Chicago"),
  ("COL", "Columbus"),
  ("SEA", "Seattle"),
  ("DAL", "Dallas"),
  ("MIN", "Minneapolis")
]

mycursor.executemany(sql, val)

print("----------CREATE project------------------")
sql = """CREATE TABLE projects ( \
        project_id INT AUTO_INCREMENT PRIMARY KEY, \
        project_name VARCHAR(255), \
        client_id INT, \
        FOREIGN KEY (client_id) REFERENCES clients(client_id), \
        start_date DATETIME, \
        length INT, \
        authors VARCHAR(255))"""

mycursor.execute(sql)

print("----------CREATE project_role------------------")
sql = """CREATE TABLE project_role ( \
        project_role_id INT AUTO_INCREMENT PRIMARY KEY, \
        project_id INT, \
        FOREIGN KEY (project_id) REFERENCES projects(project_id), \
        role_id INT, \
        FOREIGN KEY (role_id) REFERENCES roles(role_id), \
        employee_id INT, \
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id), \
        office_id INT, \
        FOREIGN KEY (office_id) REFERENCES offices(office_id), \
        discipline_id INT, \
        FOREIGN KEY (discipline_id) REFERENCES disciplines(discipline_id), \
        burden_type_id INT, \
        FOREIGN KEY (burden_type_id) REFERENCES burden_types(burden_type_id), \
        bill_rate INT, \
        hours_week INT, \
        start_week INT, \
        end_week INT)"""
mycursor.execute(sql)

mydb.commit()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

