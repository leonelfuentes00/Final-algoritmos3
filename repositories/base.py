from typing import Any, Iterable
from database import get_conn

class BaseRepo:
    def fetch_one(self, sql: str, params: Iterable[Any] = ()):
        with get_conn() as c:
            return c.execute(sql, params).fetchone()

    def fetch_all(self, sql: str, params: Iterable[Any] = ()):
        with get_conn() as c:
            return c.execute(sql, params).fetchall()

    def execute(self, sql: str, params: Iterable[Any] = ()):
        with get_conn() as c:
            cur = c.execute(sql, params)
            return cur.lastrowid
