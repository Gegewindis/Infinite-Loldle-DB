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
    Checks for a user information in database
    """
    with connection.cursor() as cursor:
        cursor.execute("""
                       select username from Users 
                       WHERE username = %s AND passwrd = %s;
                       
                       """, [username, password])
        
        return cursor.fetchall()
        

def random_champ():
    return "NOT IMPLEMENTED"


def species_desc(name):
    return "NOT IMPLEMENTED"


def region_desc(name):
    return "NOT IMPLEMENTED"


def update_points(username, points):
    return "NOT IMPLEMENTED"


def selected_champ(name):
    return "NOT IMPLEMENTED"


def random_quoute():
    return "NOT IMPLEMENTED"


def random_ability():
    return "NOT IMPLEMENTED"