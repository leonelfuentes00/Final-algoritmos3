from datetime import datetime

class Incident:
    def __init__(self, id=None, ticket_id=None, description=None, date=None):
        self.id = id
        self.ticket_id = ticket_id
        self.description = description
        self.date = date or datetime.utcnow().isoformat(timespec="seconds")
