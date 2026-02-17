-- Game
CREATE TABLE
    Champions (
        name VARCHAR(20),
        gender VARCHAR(10), --Int?
        rangeType VARCHAR(10), --Int?
        resource VARCHAR(20),
        releaseYear YEAR,
        PRIMARY KEY (name)
    );

CREATE TABLE
    Abilities (
        name VARCHAR(30),
        type VARCHAR(20), --int
        champion VARCHAR(20),
        PRIMARY KEY (name),
        FOREIGN KEY (champion) REFERENCES Champions (name)
    );

CREATE TABLE
    Quotes (
        qouteID INT AUTO_INCREMENT,
        quote VARCHAR(255) UNIQUE,
        champion VARCHAR(20),
        PRIMARY KEY (qouteID),
        FOREIGN KEY (champion) REFERENCES Champions (name)
    );

CREATE TABLE
    Regions (
        name VARCHAR(20),
        shortDesc VARCHAR(200),
        PRIMARY KEY (name)
    );

CREATE TABLE
    Species (
        name VARCHAR(20),
        shortDesc VARCHAR(200),
        PRIMARY KEY (name)
    );

CREATE TABLE
    ChampPositions (
        champName VARCHAR(20),
        position VARCHAR(5),
        PRIMARY KEY (champName, position),
        FOREIGN KEY (champName) REFERENCES Champions (name)
    );

CREATE TABLE
    ChampSpecies (
        champName VARCHAR(20),
        speciesName VARCHAR(20),
        PRIMARY KEY (champName, speciesName),
        FOREIGN KEY (champName) REFERENCES Champions (name),
        FOREIGN KEY (speciesName) REFERENCES Species (name)
    );

CREATE TABLE
    ChampRegion (
        champName VARCHAR(20),
        regionName VARCHAR(20),
        PRIMARY KEY (champName, regionName),
        FOREIGN KEY (champName) REFERENCES Champions (name),
        FOREIGN KEY (regionName) REFERENCES Regions (name)
    );

-- History
CREATE TABLE
    Users (
        username VARCHAR(20),
        passwrd VARCHAR(50),
        email VARCHAR(30) UNIQUE,
        points INT,
        PRIMARY KEY (username)
    );

CREATE TABLE
    ChangeLog (
        gameID INT AUTO_INCREMENT,
        score INT,
        changeType VARCHAR(20), --Int?
        changeTime DATE,
        username VARCHAR(20) UNIQUE,
        PRIMARY KEY (gameID),
        FOREIGN KEY (username) REFERENCES Users (username)
    );