from datetime import datetime
from .base import BaseRepo

class IncidentRepo(BaseRepo):
    def create(self, ticket_id: int, description: str, date: str | None = None) -> int:
        date = date or datetime.utcnow().isoformat(timespec="seconds")
        return self.execute("INSERT INTO incident (ticket_id,description,date) VALUES (?,?,?)",
                            (ticket_id, description, date))

    def get(self, id: int): return self.fetch_one("SELECT * FROM incident WHERE id=?", (id,))
    def list_by_ticket(self, ticket_id: int):
        return self.fetch_all("SELECT * FROM incident WHERE ticket_id=? ORDER BY id", (ticket_id,))
