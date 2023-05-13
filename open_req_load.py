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

# first, read through sheets and pull all company names.
# if new, add to db
for sheet in wb:
    print(sheet.title)
    CompanyName_raw = sheet['A5'].value
    CompanyName = CompanyName_raw[14:]
    print('CompanyName =' + CompanyName)
    sql = "SELECT * FROM clients WHERE client_name = %s"
    client_name = (CompanyName, )
    mycursor.execute(sql, client_name)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        sql_client = "INSERT INTO clients (client_name) VALUES ('" + CompanyName + "')"
        mycursor.execute(sql_client)
        print('+++++++++++++++++' + CompanyName + ' added to the db+++++++++++++++')

        mydb.commit()

# second, read through sheets and pull all job titles.
# if new, add to db
for sheet in wb:
    print(sheet.title)
    for row in sheet.values:
        print(row)
        if row[0] is not None:
            if isinstance(row[0], datetime.datetime):
                print('type ==  datetime.datetime')
            else:
                print('type !=  none')
                JobTitle_raw = row[0]
                if "Job Title" in JobTitle_raw:
                    JobTitle = JobTitle_raw[11:]
                    print('JobTitle==' + JobTitle)

                    sql = "SELECT * FROM titles WHERE title = %s"
                    title_name = (JobTitle,)
                    mycursor.execute(sql, title_name)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        sql_client = "INSERT INTO titles (title) VALUES ('" + JobTitle + "')"
                        mycursor.execute(sql_client)
                        print('+++++++++++++++++' + JobTitle + ' added to the db+++++++++++++++')

                        mydb.commit()

    # for row in sheet.values:
    #     if sheet.title != "Overview_1":
    #         print()
    #         Priority = row[1]
    #         ProjectStage = row[2]
    #         JobTitle = row[3]
    #         JobID = row[4]
    #         Openings = row[5]
    #         FocusedRecruiter = row[6]

        # if sheet.title == "Overview_1":
        #     print(row)
        #     CompanyName = row[0]
        #     Priority = row[1]
        #     ProjectStage = row[2]
        #     JobTitle = row[3]
        #     JobID = row[4]
        #     Openings = row[5]
        #     FocusedRecruiter = row[6]
        #
        #     if JobID != "None" or JobID != "Job ID":
        #         sql = "SELECT * FROM customers WHERE address = %s"
        #         adr = ("Yellow Garden 2", )
        #         mycursor.execute(sql, adr)
        #         myresult = mycursor.fetchall()
        #
        #         for x in myresult:
        #             print(x)
        # else:
        #     break
        #
        # discipline = 13
        # if "India" in ResourceDiscipline:
        #     discipline = 14
        #
        # cost_alignment = 1
        # if "India" in ResourceCostAlignment:
        #     cost_alignment = 2
        # elif "LATAM" in ResourceCostAlignment:
        #     cost_alignment = 3
        #
        # role = 1
        # if "Development" in ResourceROLE:
        #     discipline = 2
        #
        # title = 1
        # if 'Senior Quality Assurance Engineer' == TITLE:
        #     title = 2
        # elif 'Software Development Engineer in Test' == TITLE:
        #     title = 3
        # elif 'Senior Software Development Engineer in Test' == TITLE:
        #     title = 4
        # elif 'Manager, Test & Test Automation' == TITLE:
        #     title = 5
        # elif 'Principal, Test & Test Automation' == TITLE:
        #     title = 6
        # elif 'Director, Test & Test Automation' == TITLE:
        #     title = 7
        #
        # sql = """INSERT INTO employees \
        #         (employeeID, first_name, last_name, discipline_id, cost_alignment_id, \
        #         role_id, title_id, email_address) \
        #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        # val = [
        #     (ResourceEmployeeID, ResourceFirstName, ResourceLastName, discipline, cost_alignment,
        #      role, title, ResourceEmailAddress)
        # ]
        #
        # mycursor.executemany(sql, val)
        #
        # mydb.commit()

