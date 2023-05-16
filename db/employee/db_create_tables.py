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
        code VARCHAR(255), \
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
        cost_hour INT, \
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

print("----------CREATE clients------------------")
sql = """CREATE TABLE clients ( \
        client_id INT AUTO_INCREMENT PRIMARY KEY, \
        client VARCHAR(255))"""
mycursor.execute(sql)

print("----------CREATE requisition------------------")
sql = """CREATE TABLE requisitions ( \
        job_id INT PRIMARY KEY, \
        client_id INT, \
        date_added DATETIME, \
        priority VARCHAR(255), \
        project_stage VARCHAR(255), \
        openings INT, \
        job_contact INT, \
        job_title INT, \
        city VARCHAR(255), \
        candidates_screened INT, \
        client_submittals INT, \
        client_interviews INT, \
        notes VARCHAR(255), \
        FOREIGN KEY (job_contact) REFERENCES employees(employee_id), \
        FOREIGN KEY (job_title) REFERENCES titles(title_id), \
        FOREIGN KEY (client_id) REFERENCES clients(client_id))"""
mycursor.execute(sql)

# sql = "ALTER TABLE requisitions ADD FOREIGN KEY (client_id) REFERENCES clients(client_id)"
# mycursor.execute(sql)

# print("----------CREATE req_recruiter------------------")
# sql = """CREATE TABLE req_recruiter ( \
#         job_id INT PRIMARY KEY, \
#         recruiter_id INT PRIMARY KEY, \
#         FOREIGN KEY (job_id) REFERENCES requisitions(job_id), \
#         FOREIGN KEY (recruiter_id) REFERENCES employees(employee_id), \
#         client_name VARCHAR(255))"""
# mycursor.execute(sql)
#
# print("----------CREATE req_submittal------------------")
# sql = """CREATE TABLE req_submittal ( \
#         job_id INT PRIMARY KEY, \
#         submitter_id INT PRIMARY KEY, \
#         FOREIGN KEY (job_id) REFERENCES requisitions(job_id), \
#         FOREIGN KEY (submitter_id) REFERENCES employees(employee_id), \
#         client_name VARCHAR(255))"""
# mycursor.execute(sql)
#
# print("----------CREATE req_interview------------------")
# sql = """CREATE TABLE req_interview ( \
#         job_id INT PRIMARY KEY, \
#         interviewer_id INT PRIMARY KEY, \
#         FOREIGN KEY (job_id) REFERENCES requisitions(job_id), \
#         FOREIGN KEY (interviewer_id) REFERENCES employees(employee_id), \
#         interview_round INT)"""
# mycursor.execute(sql)

print("----------CREATE skillset------------------")
sql = """CREATE TABLE skillsets ( \
        skillset_id INT AUTO_INCREMENT PRIMARY KEY, \
        skillset_category VARCHAR(255), \
        skillset VARCHAR(255))"""
mycursor.execute(sql)

mydb.commit()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

