from django.db import connection

def create_user(username, password, email):
    """
    Creates a user in the database
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                       INSERT INTO Users (username, passwrd, email, points)
                       VALUES (%s, %s, %s, %s)
                       """, [username, password, email, 0])
          
def check_user(username, password):
    """
    Checks for a user information in database and returns their name
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                       SELECT username FROM Users 
                       WHERE username = %s AND passwrd = %s
                       """, [username, password])
        return cursor.fetchall()
        
def random_champ():
    """
    Returns a random champion name
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT name
                        FROM Champions
                        ORDER BY RAND()
                        LIMIT 1
                        """)
        return cursor.fetchall()

def species_desc(name):
    """
    Returns a species description
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT shortDesc
                        FROM Species
                        WHERE name = %s
                        """, [name])
        return cursor.fetchall()
    
def region_desc(name):
    """
    Returns a region description
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT shortDesc
                        FROM Regions
                        WHERE name = %s
                        """, [name])
        return cursor.fetchall()

def update_points(username, points):
    """
    Adds points to a user
    """
    with connection.cursor() as cursor:
        cursor.execute("CALL AddPoints(%s, %s)", [username, points])

def check_name(name):
    """
    Checks for existing champion and returns a boolean 
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT *
                        FROM Champions
                        WHERE name = %s
                        """, [name])
        if (cursor.fetchall()) == ():
            return False
        return True
    
def selected_champ(name):
    """
    Returns a champs info
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT c.name, c.gender, c.rangeType, c.resource, c.releaseYear,
                        cr.regionName,
                        cp.position,
                        cs.speciesName
                        FROM Champions c
                        LEFT JOIN ChampRegion cr ON c.name = cr.champName
                        LEFT JOIN ChampPositions cp ON c.name = cp.champName
                        LEFT JOIN ChampSpecies cs ON c.name = cs.champName
                        WHERE c.name = %s
                        """, [name])
        
        info = cursor.fetchall()

        filtered_info = list(info[0])
        filtered_info[5] = {filtered_info[5]}
        filtered_info[6] = {filtered_info[6]}
        filtered_info[7] = {filtered_info[7]}

        for i in range(1, len(info)):
            filtered_info[5].add(info[i][5])
            filtered_info[6].add(info[i][6])
            filtered_info[7].add(info[i][7])

        filtered_info[5] = ", ".join(filtered_info[5])
        filtered_info[6] = ", ".join(filtered_info[6])
        filtered_info[7] = ", ".join(filtered_info[7])

        return filtered_info

def random_quoute():
    """
    Returns a random quote and the champions name
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT quote, champion
                        FROM Quotes
                        ORDER BY RAND()
                        LIMIT 1
                        """)
        return cursor.fetchall()

def random_ability():
    """
    Returns a random ability and the tyoe and champions name
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT name, type, champion
                        FROM Abilities
                        ORDER BY RAND()
                        LIMIT 1
                        """)
        return cursor.fetchall()

def leaderboard_info():
    """
    Returns the username, points and the time of last played game
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT u.username, u.points, c.changeTime 
                        FROM users u 
                        JOIN changeLog c ON u.username = c.username 
                        WHERE c.changeTime = ( SELECT MAX(c2.changeTime) 
                                                FROM changeLog c2 
                                                WHERE c2.username = u.username ) 
                        ORDER BY u.points DESC
                        """)
        data = cursor.fetchall()
        refined_data = []
        for i in range(len(data)):
            refined_data.append((data[i][0], data[i][1], data[i][2].strftime("%m/%d/%Y %H:%M:%S")),)
        return tuple(refined_data)