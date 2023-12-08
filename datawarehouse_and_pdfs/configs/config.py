import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER: str = os.environ.get('user')
PASSWORD: str = os.environ.get('password')
DATABASE_NAME: str = os.environ.get('database')
HOST: str = os.environ.get('host')
MYSQL_PORT: str = os.environ.get('mysql_port')
