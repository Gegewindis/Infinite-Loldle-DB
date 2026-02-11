import mysql.connector

# Arguments
filepath = "data/champions_info.txt"
password = "georgeadrian2005@"
dbName = "infLoldle"

mydb = mysql.connector.connect(host="localhost", user="root", passwd=password)

cursor = mydb.cursor()

cursor.execute("USE " + dbName)

def insertInfo(info):
    for table in info.keys():
        cursor.execute("DESCRIBE " + table)

        fetchall_info = cursor.fetchall()
        attributes = ""

        for row in fetchall_info:
            attributes = ", ".join([row[0] for row in fetchall_info])

        for set in info[table]:
            print("INSERT INTO " + table + " (" + attributes + ") VALUES (" + set + ")")
            cursor.execute("INSERT INTO " + table + " (" + attributes + ") VALUES (" + set + ")")


def getInfo():
    info = {}
    current_table = None

    with open(filepath, "r") as fh:
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
