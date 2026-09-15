import sqlite3
from pathlib import Path
from time import time

from db.abstract_db import AbstractDb


class HistoryDb(AbstractDb):
    _path = Path(__file__).parent / "History.db"

    def __init__(self):
        self._create_table()

    def _get_connection(self):
        print(f"DB PATH: {self._path}")
        print(f"DB EXISTS: {self._path.exists()}")
        return sqlite3.connect(self._path)

    def _create_table(self):
        connection = self._get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_number REAL NOT NULL,
                    operation TEXT NOT NULL,
                    second_number REAL NOT NULL,
                    timestamp REAL NOT NULL
                )
            """
        )

        connection.commit()
        connection.close()

    def history_save(self, first_number: float, operation: str, second_number: float):
        connection = self._get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO calculations (first_number, operation, second_number, timestamp)
            VALUES (?, ?, ?, ?)
            """,
            (first_number, operation, second_number, time()),
        )

        connection.commit()
        connection.close()

    def history_load(self) -> list[dict]:
        connection = self._get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
                SELECT first_number, operation, second_number, timestamp
                FROM calculations
                ORDER BY id
            """
        )

        rows = cursor.fetchall()
        connection.close()

        return [
            {
                "first_number": row[0],
                "operation": row[1],
                "second_number": row[2],
                "timestamp": row[3],
            }
            for row in rows
        ]


