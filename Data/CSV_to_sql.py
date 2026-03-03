import mysql.connector


def insertInfo(info: dict, cursor: mysql.connector.cursor) -> None:
    for table in info.keys():
        cursor.execute("DESCRIBE " + table)

        fetchall_info = cursor.fetchall()
        attributes = ""

        for row in fetchall_info:
            attributes = ", ".join([row[0] for row in fetchall_info])

        for set in info[table]:
            print("INSERT INTO " + table + " (" + attributes + ") VALUES (" + set + ")")
            cursor.execute("INSERT INTO " + table + " (" + attributes + ") VALUES (" + set + ")")


def getInfo(filepath: str) -> dict:
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


def CSVToMySQL(filepaths: list[str], DBName: str, DBPass: str) -> None:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=DBPass)
    cursor = mydb.cursor()
    cursor.execute("USE " + DBName)

    for path in filepaths:
        print(path)
        info = getInfo(path)
        insertInfo(info, cursor)

    mydb.commit()


if __name__ == "__main__":
    CSVToMySQL(["Data/champions_info.txt", "Data/abilities_info.txt", "Data/quotes_info.txt", "Data/regions_info.txt", "Data/species_info.txt", "Data/champion_positions_info.txt", "Data/champ_species_info.txt", "Data/champ_region_info.txt"], "infloldle", "georgeadrian2005@")