from datetime import datetime
from .base import BaseRepo

class TicketRepo(BaseRepo):
    def create(self, client_id: int, reporter_employee_id: int | None,
               team_id: int | None, state: str = "OPEN",
               created_at: str | None = None) -> int:
        created_at = created_at or datetime.utcnow().isoformat(timespec="seconds")
        return self.execute(
            """INSERT INTO ticket (client_id, reporter_employee_id, team_id, state, created_at)
               VALUES (?,?,?,?,?)""",
            (client_id, reporter_employee_id, team_id, state, created_at),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM ticket WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM ticket ORDER BY id DESC")
    def set_state(self, id: int, state: str): return self.execute("UPDATE ticket SET state=? WHERE id=?", (state, id))

    # links
    def add_employee(self, ticket_id: int, employee_id: int):
        return self.execute("INSERT OR IGNORE INTO ticket_employee (ticket_id,employee_id) VALUES (?,?)",
                            (ticket_id, employee_id))

    def add_service(self, ticket_id: int, service_id: int):
        return self.execute("INSERT OR IGNORE INTO ticket_service (ticket_id,service_id) VALUES (?,?)", (ticket_id, service_id))
