import time
import psycopg2

import config
from sql_queries import (
	create_songs_query,
	create_artiste_query,
	create_users_query,
	create_songplays_query,
)

while True:
	# connect to database, create curosor and set autocommit, \
	# while making sure the latter is dependeny on the previous one
	try:
		conn = psycopg2.connect(
			databse=config.DATABASE,
			user=config.DATABASE_USER,
			password=config.DATABASE_PASSWORD,
			host=config.DATABASE_HOST,
			port=config.DATABASE_PORT
		)
		print("Database connection successful")
		break
	except psycopg2.Error as e:
		print("Failed to Connect to Database: {}".format(e))
		time.sleep(3)

cursor = conn.cursor(); print("Cursor Created!")
conn.set_session(autocommit=True)

# Check if database exists

try:
	cursor.execute(create_songs_query)
	print("Table created or exists!")
except psycopg2.Error as e:
	print("Error creating Table: {}".format(e))

try:
	cursor.execute(create_songs_query)
	print("Table created or exists!")
except psycopg2.Error as e:
	print("Error creating Table: {}".format(e))

try:
	cursor.execute(create_artiste_query)
	print("Table created or exists!")
except psycopg2.Error as e:
	print("Error creating Table: {}".format(e))

try:
	cursor.execute(create_users_query)
	print("Table created or exists!")
except psycopg2.Error as e:
	print("Error creating Table: {}".format(e))
