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
                    timestamp REAL NOT NULL,
                    session_id TEXT NOT NULL DEFAULT 'default'
                )
            """
        )

        columns = [row[1] for row in cursor.execute("PRAGMA table_info(calculations)")]
        if "session_id" not in columns:
            cursor.execute(
                "ALTER TABLE calculations ADD COLUMN session_id TEXT NOT NULL DEFAULT 'default'"
            )

        connection.commit()
        connection.close()

    def history_save(
        self, first_number: float, operation: str, second_number: float, session_id: str = "default"
    ):
        connection = self._get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
                        INSERT INTO calculations (first_number, operation, second_number, timestamp, session_id)
            VALUES (?, ?, ?, ?, ?)
            """
            , (first_number, operation, second_number, time(), session_id),

        )

        connection.commit()
        connection.close()

    def history_clear(self, session_id: str | None = None):
        connection = self._get_connection()
        if session_id is None:
            connection.execute("DELETE FROM calculations")
        else:
            connection.execute("DELETE FROM calculations WHERE session_id = ?", (session_id,))
        connection.commit()
        connection.close()

    def history_load(
        self, operation: str | None = None, session_id: str | None = None
    ) -> list[dict]:
        connection = self._get_connection()
        cursor = connection.cursor()
        conditions = []
        parameters = []
        if operation is not None:
            conditions.append("operation = ?")
            parameters.append(operation)
        if session_id is not None:
            conditions.append("session_id = ?")
            parameters.append(session_id)

        query = """
            SELECT first_number, operation, second_number, timestamp
            FROM calculations
        """
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY id"
        cursor.execute(query, parameters)

        rows = cursor.fetchall()
        connection.close()

        return [
            {
                "first_number": row[0],
                "operation": row[1],
                "second_number": row[2],
                "timestamp": row[3]
            }
            for row in rows
        ]


