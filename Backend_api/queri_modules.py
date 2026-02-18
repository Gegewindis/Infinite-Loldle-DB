import mysql.connector

filepath = "data/champion_positions_info.txt"
password = "georgeadrian2005@"
dbName = "infLoldle"

mydb = mysql.connector.connect(host="localhost", user="root", passwd=password)

cursor = mydb.cursor(dictionary=True)

def selectRandomChampion():
    randomChamp = """
    SELECT name
    FROM Champions
    ORDER BY RAND()
    LIMIT 1
    """
    cursor.execute(randomChamp)
    return cursor.fetchone()

def getChampData(champName):
    allChampData = """
    SELECT c.name, c.gender, c.rangeType, c.resource, c.releaseYear,
    cr.regionName,
    cp.position,
    cs.speciesName
    FROM Champions c
    LEFT JOIN ChampRegion cr ON c.name = cr.champName
    LEFT JOIN ChampPositions cp ON c.name = cp.champName
    LEFT JOIN ChampSpecies cs ON c.name = cs.champName
    WHERE c.name = %s
    """
    cursor.execute(allChampData, (champName,))
    return cursor.fetchall() # Migth need changes, retuirns some with one value and others with more then one value, but thats a logic based problem rigth?

def getSpeciesDesc(speciesName):
    speciesDesc = """
    SELECT shortDesc
    FROM Species
    WHERE name = %s
    """
    cursor.execute(speciesDesc, (speciesName,))
    return cursor.fetchone()


def getRegionDesc(regionName):
    regionDesc = """
    SELECT shortDesc
    FROM Regions
    WHERE name = %s
    """
    cursor.execute(regionDesc, (regionName,))
    return cursor.fetchone()

def getRandomQuoute():
    randomQuoute = """
    SELECT quote, champion
    FROM Quotes
    ORDER BY RAND()
    LIMIT 1
    """
    cursor.execute(randomQuoute)
    return cursor.fetchone()


def getRandomAbility():
    randomAbility = """
    SELECT name, type, champion
    FROM Abilities
    ORDER BY RAND()
    LIMIT 1
    """
    cursor.execute(randomAbility)
    return cursor.fetchone()

def updatePoints(username, points):
    return "NOT IMPLEMENTED"

""""
def checkChampion(randomChamp, userGuess):
    check = {
        "gender": userGuess["gender"] == randomChamp["gender"],
        "rangeType": userGuess["rangeType"] == randomChamp["rangeType"],
        "resource": userGuess["resource"] == randomChamp["resource"],
        "releaseYear": userGuess["releaseYear"] == randomChamp["releaseYear"],
        "regionName": userGuess["regionName"] == randomChamp["regionName"],
        "position": userGuess["position"] == randomChamp["position"],
        "speciesName": userGuess["speciesName"] == randomChamp["speciesName"]

        abilitie["abilityName"] = bool(set(randomChamp["abilityName"]) & set(userGuess["abilityName"]))
        quotes["quote"] = bool(set(randomChamp["quote"]) & set(userChampion["quote"]))
    }
    #check here later if releaseYear is larger or smaller. Not sure how we wanna implement that, web or here in sql?

    return check
"""
"""
def userChampion(champName):
    champ = 
    SELECT *
    FROM Champions
    WHERE name = %s

    cursor.execute(champ, (champName,))
    return cursor.fetchone()
    

def champRegion(champName):
    region = 
    SELECT regionName
    FROM ChampRegion
    WHERE champName = %s
    
    cursor.execute(region, (champName,))
    return cursor.fetchone()

def champPosition(champName):
    position = 
    SELECT position
    FROM ChampPositions
    WHERE champName = %s
    
    cursor.execute(position, (champName,))
    return cursor.fetchone()

def champSpecies(champName):
    species = 
    SELECT speciesName
    FROM ChampSpecies
    WHERE champName = %s
    
    cursor.execute(species, (champName,))
    return cursor.fetchone()


def championAbilityData(champName):
    championAbilityJoin = 
    SELECT c.name, c.gender, c.rangeType, c.resource, c.releaseYear,
    a.name AS abilityName, a.type AS abilityType
    FROM Champions c
    LEFT JOIN Abilities a ON c.name = a.champion
    WHERE c.name = %s
    
    cursor.execute(championAbilityJoin, (champName,))
    return cursor.fetchall()

def championQuotesData(champName):
    championQuoteJoin = 
    SELECT c.name, c.gender, c.rangeType, c.resource, c.releaseYear, q.quoteID, q.quote
    FROM Champions c
    LEFT JOIN Quotes q on c.name = q.champion
    WHERE c.name = %s
    
    cursor.execute(championQuoteJoin, (champName,))
    return cursor.fetchall()
"""