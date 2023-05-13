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

# first, read through Overview and create new req record
# if new, add to db
for sheet in wb:
    print(sheet.title)
    if sheet.title == 'Overview_1':
        client_id = 0
        for row in sheet.values:
            print(row)
            if row[4] is not None:
                JobID = row[4]
                if JobID != 'Job ID':
                    print('JobID =' + str(JobID))
                    CompanyName = row[0]
                    Priority = row[1]
                    ProjectStage = row[2]
                    JobTitle = row[3]
                    Openings = row[5]

                    sql = "SELECT * FROM requisitions WHERE job_id = %s"
                    client_name = (JobID, )
                    mycursor.execute(sql, client_name)
                    myresult = mycursor.fetchall()
                    if len(myresult) == 0:
                        if CompanyName is not None:
                            sql = "SELECT client_id FROM clients WHERE client_name = %s"
                            client_name = (CompanyName, )
                            mycursor.execute(sql, client_name)
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                client_id = x[0]

                        print('client_id:' + str(client_id))

                        title_id = 0
                        sql = "SELECT title_id FROM titles WHERE title = %s"
                        title_name = (JobTitle, )
                        mycursor.execute(sql, title_name)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print('title_id:' + str(x[0]))
                            title_id = x[0]
                            sql = """INSERT INTO requisitions ( \
                                            job_id, \
                                            client_id, \
                                            priority, \
                                            project_stage, \
                                            openings, \
                                            job_title) VALUES (%s, %s, %s, %s, %s, %s)"""
                            val = [
                                (JobID, client_id, Priority, ProjectStage, Openings, title_id)
                            ]

                            mycursor.executemany(sql, val)
                            print('+++++++++++++++++JobID:' + str(JobID) + ' added to the db+++++++++++++++')

                            mydb.commit()
    else:
        for row in sheet.values:
            if row[4] is not None:
                JobID = row[4]
                if JobID != 'Job ID':
                    print('JobID =' + str(JobID))
                    DateAdded = row[0]
                    JobContact = row[2]
                    City = row[5]
                    Openings = row[6]
                    Screened = row[7]
                    Submittals = row[8]
                    Interviews = row[9]

                    contact_id = 0
                    x = JobContact.split(" ")
                    first_name = x[0]
                    last_name = x[1]
                    if last_name == '':
                        x = JobContact.split("  ")
                    first_name = x[0]
                    last_name = x[1]
                    print('found JobContact:' + first_name + ' ' + last_name)
                    sql = "SELECT employee_id FROM employees WHERE first_name = %s AND last_name = %s"
                    title_name = (first_name, last_name)
                    mycursor.execute(sql, title_name)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print('contact_id:' + str(x[0]))
                        contact_id = x[0]

                    sql = """UPDATE requisitions SET \
                                    date_added = %s, \
                                    job_contact = %s, \
                                    city = %s, \
                                    openings = %s, \
                                    candidates_screened = %s, \
                                    client_submittals = %s, \
                                    client_interviews = %s \
                                    WHERE job_id = %s"""
                    val = [
                        (DateAdded, contact_id, City, Openings, Screened, Submittals, Interviews, JobID)
                    ]

                    mycursor.executemany(sql, val)
                    print('@@@@@@@@@@@@@@@@@JobID:' + str(JobID) + ' updated in the db@@@@@@@@@@@@@@@')

                    mydb.commit()
