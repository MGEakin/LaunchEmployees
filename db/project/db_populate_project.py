import mysql.connector
from openpyxl import load_workbook

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

wb = load_workbook("C:\\repos\\python\\LaunchEmployees\\db\\employee\\TestAutomation.xlsx")

ws = wb.active

for sheet in wb:
    # print(sheet.title)
    for row in sheet.values:
        # print(row)
        ResourceEmployeeID = row[0]
        ResourceFirstName = row[1]
        ResourceLastName = row[2]
        ResourceStudio = row[3]
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

