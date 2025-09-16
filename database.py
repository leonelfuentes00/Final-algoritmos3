import sqlite3
from contextlib import contextmanager

DB_PATH = "helpdesk.db"

def _row_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = _row_factory
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
