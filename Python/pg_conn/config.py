import os
from dotenv import load_dotenv
load_dotenv()


class Config:
# Параметры подключения к БД

    class PostgresLocal:
        host = os.getenv('POSTGRES_LOCAL_HOST')
        user = os.getenv('POSTGRES_LOCAL_USER')
        password = os.getenv('POSTGRES_LOCAL_PASSWORD')
        db_name = os.getenv('POSTGRES_LOCAL_DB_name')
        port = os.getenv('POSTGRES_LOCAL_PORT')
