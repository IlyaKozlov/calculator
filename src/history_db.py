import json
from pathlib import Path
from time import time


class HistoryDb:

    _path = Path(__file__).parent / "History.db"

    def history_save(self, first_number: float, operation: str, second_number: float):
        with open(self._path, "a") as db:
            item = {"first_number": first_number,
                    "operation": operation,
                    "second_number": second_number,
                    "timestamp": time()
                    }
            db.write(json.dumps(item) + "\n")