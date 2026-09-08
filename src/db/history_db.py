import json
from pathlib import Path
from time import time

from db.abstract_db import AbstractDb


class HistoryDb(AbstractDb):

    _path = Path(__file__).parent / "History.db"

    def history_save(self, first_number: float, operation: str, second_number: float):
        with open(self._path, "a") as db:
            item = {"first_number": first_number,
                    "operation": operation,
                    "second_number": second_number,
                    "timestamp": time()
                    }
            print(f"add new operation to db, {item}")
            db.write(json.dumps(item) + "\n")

    def history_load(self) -> list[dict]:
        if  not self._path.exists():
            return []
        with open(self._path, "r") as db:
            return [json.loads(line) for line in db]

