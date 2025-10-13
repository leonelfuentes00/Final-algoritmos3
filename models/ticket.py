from datetime import datetime
from .enums import TicketStatus, Priority

class Ticket:
    def __init__(self, id=None, client_id=None, reporter_employee_id=None,
                 team_id=None, state=TicketStatus.OPEN,
                 priority=Priority.MEDIUM, created_at=None):
        self.id = id
        self.client_id = client_id
        self.reporter_employee_id = reporter_employee_id
        self.team_id = team_id
        self.state = state
        self.priority = priority
        self.created_at = created_at or datetime.utcnow().isoformat(timespec="seconds")
