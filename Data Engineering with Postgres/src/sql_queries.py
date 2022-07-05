"""This module contains queries to be run in the database."""

import config

drop_database_query: str = f"DROP DATABASE IF EXISTS {config.DATABASE}"
create_database_query: str = f"CREATE DATABASE {config.DATABASE}"
drop_any_table: str = "DROP TABLE IF EXISTS {table_name}"

create_songs_query: str = """
CREATE TABLE songs (
	song_id SERIAL NOT NULL UNIQUE,
	artiste_id INT NOT NULL,
	song_title VARCHAR(50),
	duration FLOAT,
	year INT,
	PRIMARY KEY (song_id)
);
"""

create_artiste_query: str = """
CREATE TABLE artistes (
	artiste_id SERIAL,
	name VARCHAR(50),
	location VARCHAR(50),
	latitude FLOAT,
	longitude FLOAT,
	PRIMARY KEY(artiste_id)
);
"""

create_users_query: str = """
CREATE TABLE users (
	user_id SERIAL,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender CHAR,
	level VARCHAR(5),
	PRIMARY KEY(user_id)
);
"""

create_songplays_query: str = """
CREATE TABLE songplays (
	song_play_id SERIAL NOT NULL,
	artiste_id INT,
	song_id INT,
	user_id INT
	PRIMARY KEY(artiste_id),
	FOREIGN KEY()
);
"""