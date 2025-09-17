from datetime import datetime
from .base import BaseRepo

class MessageRepo(BaseRepo):
    def create(self, ticket_id: int, sender_employee_id: int, content: str, date: str | None = None) -> int:
        date = date or datetime.utcnow().isoformat(timespec="seconds")
        return self.execute(
            "INSERT INTO message (ticket_id,sender_employee_id,date,content) VALUES (?,?,?,?)",
            (ticket_id, sender_employee_id, date, content),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM message WHERE id=?", (id,))
    def list_by_ticket(self, ticket_id: int):
        return self.fetch_all("SELECT * FROM message WHERE ticket_id=? ORDER BY id", (ticket_id,))
