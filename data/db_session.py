import sqlite3
from utils.paths import DB_FILE_PATH
import contextlib


class DatabaseManager:
    def __init__(self):
        self.connector = None
        self.last_id = 0

    def connect(self, db_path: str):
        self.connector = sqlite3.connect(
            db_path, check_same_thread=False
        )

    def execute(self, sql_command: str) -> list:
        if self.connector is None:
            raise Exception("Отсутствует подключение. "
                            "Воспользуйтесь методом .connect(db_path")
        with contextlib.closing(
                sqlite3.Cursor(self.connector)) as cursor:
            try:
                result = cursor.execute(sql_command)
                self.last_id = cursor.lastrowid
                self.connector.commit()

            except sqlite3.Error as error:
                print('ОШИБКА В:', sql_command)
                raise error

            finally:
                return result.fetchall()

    def get_last_id(self):
        return self.last_id




GlobalDBManager = DatabaseManager()
GlobalDBManager.connect(DB_FILE_PATH)

