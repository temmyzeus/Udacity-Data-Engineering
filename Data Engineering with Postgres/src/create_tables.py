import time

import config
import psycopg2

from sql_queries import (
	create_artiste_query, 
	create_database_query,
	create_songplays_query, 
	create_songs_query,
	create_users_query, 
	drop_any_table,
	drop_database_query
	)


def drop_database(cursor):
	try:
		cursor.execute(drop_database_query)
		print("Database Dropped!")
	except psycopg2.Error as e:
		print("Error dropping database: {}".format(e))

def create_database(cursor):
	try:
		cursor.execute(create_database_query)
		print("Database Created!")
	except psycopg2.Error as e:
		print("Error creating database: {}".format(e))

def drop_tables(cursor):
	table_names: list[str] = ["songs", "artistes", "users", "songplays", "time"]
	for table_name in table_names:
		try:
			cursor.execute(drop_any_table.format(table_name=table_name))
			print(f"Dropping {table_name} table")
		except psycopg2.Error as e:
			print("Error dropping {} table: {}".format(table_name, e))

def create_tables(cursor):
	try:
		cursor.execute(create_artiste_query)
		print("Table created")
	except psycopg2.Error as e:
		print("Error creating Table: {}".format(e))
	
	try:
		cursor.execute(create_songs_query)
		print("Table created")
	except psycopg2.Error as e:
		print("Error creating Table: {}".format(e))

	try:
		cursor.execute(create_users_query)
		print("Table created")
	except psycopg2.Error as e:
		print("Error creating Table: {}".format(e))

	# create time relation
	# Create songplays relation

def main():
	while True:
	# connect to database, create cursor and set autocommit
		try:
			conn = psycopg2.connect(
				database=config.DATABASE,
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

	drop_database(cursor)
	create_database(cursor)
	drop_tables(cursor)
	create_tables(cursor)

	cursor.close()
	conn.close()

if __name__ == "__main__":
	main()
