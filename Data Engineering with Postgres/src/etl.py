import os
from datetime import date
from pathlib import Path
from typing import Union

import pandas as pd
from pendulum import time

DATA_DIR: Union[str, Path] = Path("./data")
songs_data_dir = DATA_DIR / "song_data"
logs_data_dir = DATA_DIR / "log_data"

# load songs .json file

def ymd_from_filename(filename: str):
	"""Get year, month, day from filename"""
	year, month, day = filename.split("-")[:3]
	return year, month, day

for track_id_head_1 in songs_data_dir.iterdir():
	for track_id_head_2 in track_id_head_1.iterdir():
		for track_id_head_3 in track_id_head_2.iterdir():
			for file in track_id_head_3.iterdir():
				if os.path.splitext(file.name)[-1] == ".json":
					df = pd.read_json(file, lines=True)
					artiste_df = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]]
					songs_df = df[["song_id", "artist_id", "title", "duration", "year"]]
					artiste_df.to_sql()
					songs_df.to_sql()

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
