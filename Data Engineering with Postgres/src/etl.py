import os
import time
from datetime import date
from pathlib import Path
from typing import Union

import pandas as pd
from sqlalchemy import create_engine

import config

DATA_DIR: Union[str, Path] = Path("./data")
songs_data_dir = DATA_DIR / "song_data"
logs_data_dir = DATA_DIR / "log_data"

# load songs .json file

while True:
    # connect to database, create cursor and set autocommit
    try:
        engine = create_engine(
            f"postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}/{config.DATABASE}"
        )
        engine.connect()
        print("Database connection successful")
        break
    except Exception as e:  # Bad pratice I know, I'll check sqlalchemy docs to understand their exceptions better
        print("Failed to Connect to Database: {}".format(e))
        time.sleep(3)


def date_from_filename(filename: str) -> date:
    """Get year, month, day from filename"""
    year, month, day = [int(_) for _ in filename.split("-")[:3]]
    return date(year, month, day)


def merge_in_query(query: str, values: list) -> str:
    if not ("{}" in query):
        raise ValueError("query must have a `{}` for string formatting!")

    if not isinstance(values, list):
        raise TypeError("values must be a list object!")

    values_len = len(values)
    if values_len == 0:
        raise ValueError("Array or list must contain a value!")
    elif values_len == 1:
        in_values = "({!r})".format(values[0])
        return query.format(in_values)
    else:
        in_values = tuple(values)
        return query.format(in_values)


for track_id_head_1 in songs_data_dir.iterdir():
    for track_id_head_2 in track_id_head_1.iterdir():
        for track_id_head_3 in track_id_head_2.iterdir():
            for file in track_id_head_3.iterdir():
                if os.path.splitext(file.name)[-1] == ".json":
                    df = pd.read_json(file, lines=True)
                    artiste_df = df[
                        [
                            "artist_id",
                            "artist_name",
                            "artist_location",
                            "artist_latitude",
                            "artist_longitude",
                        ]
                    ]
                    artiste_df.columns = [
                        "id",
                        "name",
                        "location",
                        "latitude",
                        "longitude",
                    ]

                    songs_df = df[["song_id", "artist_id", "title", "duration", "year"]]
                    songs_df.columns = [
                        "id",
                        "artiste_id",
                        "song_title",
                        "duration",
                        "year",
                    ]

                    # check if artist_id already exists in database
                    artist_ids = artiste_df["id"].tolist()
                    query = merge_in_query(
                        "SELECT id FROM artistes WHERE id in {}", artist_ids
                    )
                    result = engine.execute(query)
                    # if artiste_id already exists, drop row in df and commit others,
                    # if it's the only one, just do nothing.
                    if result.fetchone():
                        position_mask = artiste_df.id.isin(artist_ids)
                        drop_index = artiste_df.loc[position_mask, "id"].index #specify one column so it doesn't retrieve all
                        artiste_df = artiste_df.drop(index=drop_index)
                        print(f"Shape after drop: {artiste_df.shape}")

                    artiste_df.to_sql(
                        "artistes", con=engine, if_exists="append", index=False
                    )
                    songs_df.to_sql(
                        "songs", con=engine, if_exists="append", index=False
                    )

# load logs
for year in logs_data_dir.iterdir():
	for month in year.iterdir():
		for file in month.iterdir():
			if os.path.splitext(file.name)[-1] == ".json":
				# get log date of data
				year, month, day = [int(i) for i in ymd_from_filename(file.name)]
				log_date = date(year, month, day)

				df = pd.read_json(file, lines=True)

				user_df = df[["user_id"], ["firstName", "lastName", "gender", "level"]]

				songplays_df = df[["session_id", "location", "userAgent"]]

				time_df = df[[""]]
				time_df["day"] = log_date.day
				# week
				time_df["month"] = log_date.month
				time_df["year"] = log_date.year
				time_df["weekday"] = log_date.weekday()
				user_df.to_sql()
				# songplays_df.to_sql()
				# time_df.to_sql()
