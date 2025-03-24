from sqlalchemy import create_engine
from setting import conf


USER = conf.get("DATABASE", "user")
PASSWORD = conf.get("DATABASE", "password")
HOST = conf.get("DATABASE", "host")
PORT = conf.get("DATABASE", "port")
DATABASE = conf.get("DATABASE", "database")

# Задаем коннект строку
connection_str = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Коннектим к базе
engine = create_engine(url=connection_str)