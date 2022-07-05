import os
from dotenv import load_dotenv

load_dotenv()

DATABASE: str = os.environ["DATABASE"]
DATABASE_USER: str = os.environ["DB_USER"]
DATABASE_PASSWORD: str = os.environ["DB_PASSWORD"]
DATABASE_HOST: str = os.environ["DB_HOST"]
DATABASE_PORT: int = int(os.environ["DB_PORT"])
