from openpyxl import load_workbook
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

wb_name = """C:\\Users\\MattEakin\\OneDrive - Launch Consulting \
Group\\Documents\\OpenReqs\\Open Requisitions Report (By Company).xlsx"""
wb = load_workbook(wb_name)

ws = wb.active

Client = ''
Author = ''
ProjectName = ''
Contingency = 0
StartDate = datetime.datetime.now()
Unbilled = 0
ProjectLength = 0
VolDiscount = 0

for sheet in wb:
    # print(sheet.title)
    for row in sheet.values:
        print(row)
        if row[1] == 'Client:':
            Client = row[2]
            Author = row[7]
        elif row[1] == 'Project:':
            ProjectName = row[2]
            Contingency = row[7]
        elif row[1] == 'Project Start Date:':
            StartDate = row[2]
            Unbilled = row[7]
        if row[1] == 'Project Length:':
            ProjectLength = row[2]
            VolDiscount = row[7]

        ResourceDiscipline = row[4]
        ResourceROLE = row[9]
        TITLE = row[11]
        ResourceCostAlignment = row[12]
        ResourceEmailAddress = row[13]

        if "Resource" in ResourceEmployeeID:
            print('header')
        else:
            discipline = 13
            if "India" in ResourceDiscipline:
                discipline = 14

            cost_alignment = 1
            if "India" in ResourceCostAlignment:
                cost_alignment = 2
            elif "LATAM" in ResourceCostAlignment:
                cost_alignment = 3

            role = 1
            if "Development" in ResourceROLE:
                discipline = 2

            title = 1
            cost_hour = 90
            if 'Senior Quality Assurance Engineer' == TITLE:
                title = 2
                cost_hour = 90
            elif 'Software Development Engineer in Test' == TITLE:
                title = 3
                cost_hour = 125
            elif 'Senior Software Development Engineer in Test' == TITLE:
                title = 4
                cost_hour = 150
            elif 'Manager, Test & Test Automation' == TITLE:
                title = 5
                cost_hour = 125
            elif 'Principal, Test & Test Automation' == TITLE:
                title = 6
                cost_hour = 150
            elif 'Director, Test & Test Automation' == TITLE:
                title = 7
                cost_hour = 175

            sql = """INSERT INTO employees \
                    (employeeID, first_name, last_name, discipline_id, cost_alignment_id, \
                    role_id, title_id, email_address, cost_hour) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = [
                (ResourceEmployeeID, ResourceFirstName, ResourceLastName, discipline, cost_alignment,
                 role, title, ResourceEmailAddress, cost_hour)
            ]

            mycursor.executemany(sql, val)
            print('+++++++++++++++++employees:' + ResourceFirstName + ' ' + ResourceLastName +
                  ' added to the db+++++++++++++++')

            mydb.commit()

