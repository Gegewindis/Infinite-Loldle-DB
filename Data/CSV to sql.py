import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="georgeadrian2005@")

cursor = mydb.cursor()

cursor.execute("USE infloldle")


def insertInfo(info):
    for table in info.keys():
        cursor.execute("DESCRIBE " + table)

        fetchall_info = cursor.fetchall()
        attributes = ""

        for row in fetchall_info:
            attributes = ", ".join([row[0] for row in fetchall_info])

        for set in info[table]:
            cursor.execute("INSERT INTO " + table + " (" + attributes + ") VALUES (" + set + ")")


def getInfo():
    info = {}
    current_table = None

    with open("champions_info.txt", "r") as fh:
        lines = fh.readlines()

    for line in lines:
        line = line.strip()
        if line == '':
            pass

        elif "," not in line:
            current_table = line
            info[line] = []

        else:
            info[current_table].append(line)

    return info



info = getInfo()

insertInfo(info)

mydb.commit()
