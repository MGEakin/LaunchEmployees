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
    # print(sheet.title)
    CompanyName_raw = sheet['A5'].value
    CompanyName = CompanyName_raw[14:]
    # print('CompanyName =' + CompanyName)
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
    # print(sheet.title)
    for row in sheet.values:
        # print(row)
        if row[0] is not None:
            if isinstance(row[0], datetime.datetime):
                print('type ==  datetime.datetime')
            else:
                # print('type !=  none')
                JobTitle_raw = row[0]
                if "Job Title" in JobTitle_raw:
                    JobTitle = JobTitle_raw[11:]
                    # print('JobTitle==' + JobTitle)

                    sql = "SELECT * FROM titles WHERE title = %s"
                    title_name = (JobTitle,)
                    mycursor.execute(sql, title_name)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        sql_client = "INSERT INTO titles (title) VALUES ('" + JobTitle + "')"
                        mycursor.execute(sql_client)
                        print('+++++++++++++++++' + JobTitle + ' added to the db+++++++++++++++')

                        mydb.commit()

# third, read through sheets and pull all recruiters.
# if new, add to db
for sheet in wb:
    # print(sheet.title)
    if sheet.title == 'Overview_1':
        for row in sheet.values:
            # print(row)
            if row[6] is not None:
                Recruiter_raw = row[6]
                if Recruiter_raw != 'name' and Recruiter_raw != 'Focused Recruiter(s)':
                    x = Recruiter_raw.split(" ")
                    first_name = x[0]
                    last_name = x[1]
                    # print('found recruiter:' + first_name + ' ' + last_name)
                    sql = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s"
                    title_name = (first_name, last_name)
                    mycursor.execute(sql, title_name)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        sql_client = "INSERT INTO employees (first_name, last_name, title_id) VALUES (%s, %s, %s)"
                        val = [
                            (first_name, last_name, 1)
                        ]

                        mycursor.executemany(sql_client, val)
                        print('+++++++++++++++++' + first_name + ' ' + last_name + ' added to the db+++++++++++++++')

                        mydb.commit()

# Lastly, read through sheets and pull all job contacts.
# if new, add to db
for sheet in wb:
    # print(sheet.title)
    if sheet.title != 'Overview_1':
        for row in sheet.values:
            # print(row)
            if row[2] is not None:
                Recruiter_raw = row[2]
                if Recruiter_raw != 'Job Contact':
                    x = Recruiter_raw.split(" ")
                    # print(x)
                    first_name = x[0]
                    last_name = x[1]
                    if last_name == '':
                        x = Recruiter_raw.split("  ")
                    first_name = x[0]
                    last_name = x[1]
                    # print('found recruiter:' + first_name + ' ' + last_name)
                    sql = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s"
                    title_name = (first_name, last_name)
                    mycursor.execute(sql, title_name)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        sql_client = "INSERT INTO employees (first_name, last_name) VALUES (%s, %s)"
                        val = [
                            (first_name, last_name)
                        ]

                        mycursor.executemany(sql_client, val)
                        print('+++++++++++++++++' + first_name + ' ' + last_name + ' added to the db+++++++++++++++')

                        mydb.commit()
