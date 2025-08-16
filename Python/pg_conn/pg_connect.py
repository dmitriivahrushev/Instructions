from dataclasses import dataclass
from contextlib import contextmanager
from typing import Optional, Dict, Tuple, List
import logging
import psycopg2


@dataclass 
class Dbconfig:
    """Класс для хранения конфигураций БД.
    host: Хост базы данных (например, "localhost").
    database: Имя базы данных.
    user: Имя пользователя.
    password: Пароль.
    port: Порт.   
    """
    host: str
    database: str
    user: str
    password: str
    port: int 


class PosgresManager:
    def __init__(self, config: Dbconfig):
        self.config = config
        self.connection = None

    def __enter__(self):
        self.get_connect()
        return self
    
    
    def get_connect(self) -> bool:
        try:
            self.connection = psycopg2.connect(
                dbname = self.config.database,
                user = self.config.user,
                password = self.config.password,
                host = self.config.host,
                port = self.config.port
            )
            logging.info(f'Соединение с {self.config.database} установлено.')
            return True
        except Exception as e:
            logging.error(f'Ошибка подключения к Базе данных!\n{e}')
            return False

    @contextmanager
    def get_cursor(self):
        if not self.connection:
            self.get_connect()
        
        cursor = self.connection.cursor()
        try:
            yield cursor
            logging.info(f'Транзакция завершена!')
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            logging.info(f'Отмена транзакции!\n{e}')
            raise
        finally:
            cursor.close()

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> List[Dict]:
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
           self.connection.close()
