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
sql = "INSERT INTO titles (title) VALUES (%s)"
val = [
  ('Associate Recruiter', ),
  ('Recruiter', ),
  ('Sr Technical Recruiter', ),
  ('Senior Recruiter', ),
  ('Manager, Recruiting', ),
  ('Managing Director, Mexico', ),
  ('Quality Assurance Engineer', ),
  ('Senior Quality Assurance Engineer', ),
  ('Software Development Engineer in Test',),
  ('Senior Software Development Engineer in Test', ),
  ('Manager, Test & Test Automation', ),
  ('Principal, Test & Test Automation', ),
  ('Director, Test & Test Automation',)
]
mycursor.executemany(sql, val)

print("----------INSERT cost_alignment------------------")
sql = "INSERT INTO cost_alignment (cost_alignment) VALUES (%s)"
val = [
  ("Launch US", ),
  ("Launch India", ),
  ("Launch LATAM",)
]

mycursor.executemany(sql, val)

mydb.commit()

print("----------INSERT disciplines------------------")
sql = "INSERT INTO disciplines (code, discipline, studio_id) VALUES (%s, %s, %s)"
val = [
  ("DG", "Data Governance", 3),
  ("DAE", "Data Architecture & Engineering", 3),
  ("AI", "AI & Data Science", 3),
  ("DA", "Data Analytics & Visualization", 3),
  ("EE", "Enterprise Engineering", 4),
  ("CS", "Cloud Solutions", 4),
  ("ITCS", "IT Cybersecurity", 5),
  ("OTCS", "ICS/OT Cybersecurity", 5),
  ("RC", "Regulatory Compliance", 5),
  ("AS", "Application Security", 5),
  ("DSO", "DevSecOps", 6),
  ("SR", "Site Reliability", 6),
  ("TTA", "Test & Test Automation", 6),
  ("TTA-I", "Test & Test Automation - India", 6),
  ("AD", "Architecture & Development", 6),
  ("TS", "Technology Strategy", 7),
  ("SA", "Solution Architecture", 7),
  ("LA", "Leadership Advisory", 8),
  ("OEC", "Organizational Effectiveness & Change", 8),
  ("LD", "Learning & Development", 8),
  ("BPM", "Business Program Management & Analysis", 8),
  ("AT", "Agile Transformation", 9),
  ("DDM", "Digital Delivery Management", 9),
  ("HED", "Human Experience Design", 9),
  ("PSA", "Product Strategy & Analysis", 9),
]

mycursor.executemany(sql, val)

mydb.commit()
