import os
from pathlib import Path
from typing import Union

import pandas as pd


DATA_DIR: Union[str, Path] = Path("./data")
songs_data_dir = DATA_DIR / "song_data"
logs_data_dir = DATA_DIR / "log_data"

# load songs .json file
for track_id_head_1 in songs_data_dir.iterdir():
	for track_id_head_2 in track_id_head_1.iterdir():
		for track_id_head_3 in track_id_head_2.iterdir():
			for file in track_id_head_3.iterdir():
				if os.path.splitext(file.name)[-1] == ".json":
					df = pd.read_json(file, lines=True)
					print(df.shape)

# load logs
for year in logs_data_dir.iterdir():
	for month in year.iterdir():
		for file in month.iterdir():
			if os.path.splitext(file.name)[-1] == ".json":
				df = pd.read_json(file, lines=True)
				print(df.shape)
