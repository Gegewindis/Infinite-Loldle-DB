# :iphone: Infinite Loldle DB
The backend, including the database and the API, for the Infinite Loldle website. Built with django and mysql.

## :wrench: Technologies
* Django
* mySQL
* Python

## :rocket: Features
* REST API for the website to send requests to the database
* Simple database tool which lets you modify the database
* Script to insert CSV files directly to a database
* The schema and the ER-diagram for the database

## :round_pushpin: The Process
Started off by creating the ER-diagram which afterwards was turned into schema. The data was gathered from league-wikis. The server side was created with python framework Django, and the queries were manually created by us. A tool was also created which can help us interact with the database in an easier way.

## :heavy_exclamation_mark: Requirements
Make sure to have the following python modules installed for the server to work correctly:
* django
* django-cors-headers
* mysqlclient
* mysql-connector-python

## :vertical_traffic_light: Setting up DB and running API
1. Clone the repository to your local machine.
2. Make sure to install all of the above requirements.
3. Go to /Schema. There you will find the schema needed for your database.
4. Go to */Data/CSV_to_sql*, configure the DBName and DBPass and run the script. This will insert the data into the DB.
5. After the DB is set up you have to Configure the DB name and password in the django server settings found at */Django Server/infinite_loldle_server/infinite_loldle_server/settings.py*.
6. Lastly you have traverse to */Django Server/infinite_loldle_server* and run the command **python manage.py runserver** and the API should be up and running, ready to receive queries.
