"""This module contains queries to be run in the database."""

import config

drop_database_query: str = f"DROP DATABASE IF EXISTS {config.DATABASE}"
create_database_query: str = f"CREATE DATABASE {config.DATABASE}"
drop_any_table: str = "DROP TABLE IF EXISTS {table_name}"

create_artiste_query: str = """
CREATE TABLE artistes (
	id VARCHAR NOT NULL UNIQUE,
	name VARCHAR(100),
	location VARCHAR(50),
	latitude FLOAT,
	longitude FLOAT,
	PRIMARY KEY(id)
);
"""

create_users_query: str = """
CREATE TABLE users (
	id SERIAL NOT NULL UNIQUE,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender CHAR,
	level VARCHAR(5),
	PRIMARY KEY(id)
);
"""

# find a way to specify length for year since it would not be using more than 4 ints.
# P.S Assume that an artiste account deletion should also delete its songs
create_songs_query: str = """
CREATE TABLE songs (
	id VARCHAR NOT NULL UNIQUE,
	artiste_id VARCHAR NOT NULL,
	song_title VARCHAR(100) NOT NULL,
	duration FLOAT,
	year INT,
	PRIMARY KEY (id),
	CONSTRAINT fk_artistes_songs FOREIGN KEY (artiste_id) REFERENCES artistes(id)
	ON DELETE NO ACTION
);
"""

create_time_query: str = """
CREATE TABLE time (
	start_time TIME...,
	HOUR INT,
	DAY INT,
	WEEK INT,
	MONTH INT,
	YEAR INT,
	WEEKDAY INT
);
"""

create_songplays_query: str = """
CREATE TABLE songplays (
	id SERIAL NOT NULL UNIQUE,
	artiste_id INT,
	song_id INT,
	user_id INT
	PRIMARY KEY(id)
);
"""