"""This module contains queries to be run in the database."""

create_songs_query: str = """
CREATE TABLE IF NOT EXISTS Songs (
	song_id SERIAL,
	artiste_id INT NOT NULL,
	song_title VARCHAR(50),
	duration FLOAT,
	year INT,
	PRIMARY KEY (song_id)
);
"""

create_artiste_query: str = """
CREATE TABLE IF NOT EXISTS Artistes (
	artiste_id SERIAL,
	name VARCHAR(50),
	location VARCHAR(50),
	latitude FLOAT,
	longitude FLOAT,
	PRIMARY KEY(artiste_id)
);
"""

create_users_query: str = """
CREATE TABLE IF NOT EXISTS Users (
	user_id SERIAL,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender CHAR,
	level VARCHAR(5),
	PRIMARY KEY(user_id)
);
"""

create_songplays_query: str = """
CREATE TABLE IF NOT EXISTS Song_Plays (
	song_play_id SERIAL NOT NULL,
	artiste_id INT,
	song_id INT,
	user_id INT
	PRIMARY KEY(artiste_id),
	FOREIGN KEY()
);
"""