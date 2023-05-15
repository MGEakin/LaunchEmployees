import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="testing"
)

mycursor = mydb.cursor()

projector_file = open("C:\\repos\\python\\LaunchEmployees\\db\\employee\\ProjectorSkills.txt", 'r')

lineCount = 0
skillset_category = ''
skillset = ''

for line in projector_file:
    lineCount += 1

    if "*" in line:
        x = line.split("* ")
        first_name = x[0]
        skillset = x[1].strip()
        # print("category/skillset = " + skillset_category + '/' + skillset)

        sql = "SELECT * FROM skillsets WHERE skillset = %s AND skillset_category = %s"
        skillset_name = (skillset, skillset_category)
        mycursor.execute(sql, skillset_name)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            sql = """INSERT INTO skillsets (skillset, skillset_category) VALUES (%s, %s)"""
            val = [
                    (skillset, skillset_category)
                ]

            mycursor.executemany(sql, val)
            print('+++++++++++++++++skillset:' + str(skillset) + ' added to the db+++++++++++++++')

    else:
        if not line:
            print('break')
        elif "Software Quality" in line:
            print('break')
        elif "&" in line:
            print('break')
        else:
            # print("Line{}: {}".format(lineCount, line.strip()))
            skillset_category = line.strip()

mydb.commit()

projector_file.close()
