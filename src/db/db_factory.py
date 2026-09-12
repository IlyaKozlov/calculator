from db.abstract_db import AbstractDb
from db.history_db import HistoryDb


def get_db() -> AbstractDb:
    return HistoryDb()