from .base import BaseRepo

class WorkRepo(BaseRepo):
    def create(self, technician_employee_id: int, ticket_id: int,
               start_at: str | None, end_at: str | None, notes: str | None) -> int:
        return self.execute(
            "INSERT INTO worklog (technician_employee_id,ticket_id,start_at,end_at,notes) VALUES (?,?,?,?,?)",
            (technician_employee_id, ticket_id, start_at, end_at, notes),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM worklog WHERE id=?", (id,))
    def list_by_ticket(self, ticket_id: int):
        return self.fetch_all("SELECT * FROM worklog WHERE ticket_id=? ORDER BY id", (ticket_id,))
