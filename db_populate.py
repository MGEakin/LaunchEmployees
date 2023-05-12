import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

print("----------INSERT studios------------------")
sql = "INSERT INTO studios (studio) VALUES ('Technology')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Business')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Data & AI')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Cloud & Infrastructure')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Cybersecurity')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Software Engineering')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Technology Strategy & Architecture')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Management Consulting')"
mycursor.execute(sql)
sql = "INSERT INTO studios (studio) VALUES ('Digital Business Transformation')"
mycursor.execute(sql)

print("----------INSERT roles------------------")
sql = "INSERT INTO roles (role) VALUES ('Quality Assurance Engineer')"
mycursor.execute(sql)
sql = "INSERT INTO roles (role) VALUES ('Software Development Engineer in Test')"
mycursor.execute(sql)

print("----------INSERT titles------------------")
sql = "INSERT INTO titles (title) VALUES ('Quality Assurance Engineer')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Senior Quality Assurance Engineer')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Software Development Engineer in Test')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Senior Software Development Engineer in Test')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Manager, Test & Test Automation')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Principal, Test & Test Automation')"
mycursor.execute(sql)
sql = "INSERT INTO titles (title) VALUES ('Director, Test & Test Automation')"
mycursor.execute(sql)

mydb.commit()

print("----------INSERT disciplines------------------")
sql = "INSERT INTO disciplines (discipline, studio_id) VALUES (%s, %s)"
val = [
  ("Data Governance", 3),
  ("Data Architecture & Engineering", 3),
  ("AI & Data Science", 3),
  ("Data Analytics & Visualization", 3),
  ("Enterprise Engineering", 4),
  ("Cloud Solutions", 4),
  ("IT Cybersecurity", 5),
  ("ICS/OT Cybersecurity", 5),
  ("Regulatory Compliance", 5),
  ("Application Security", 5),
  ("DevSecOps", 6),
  ("Site Reliability", 6),
  ("Test & Test Automation", 6),
  ("Architecture & Development", 6),
  ("Technology Strategy", 7),
  ("Solution Architecture", 7),
  ("Leadership Advisory", 8),
  ("Organizational Effectiveness & Change", 8),
  ("Learning & Development", 8),
  ("Business Program Management & Analysis", 8),
  ("Agile Transformation", 9),
  ("Digital Delivery Management", 9),
  ("Human Experience Design", 9),
  ("Product Strategy & Analysis", 9),
]

mycursor.executemany(sql, val)

mydb.commit()
