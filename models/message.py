from datetime import datetime

class Message:
    def __init__(self, id=None, ticket_id=None, sender_employee_id=None,
                 content=None, date=None):
        self.id = id
        self.ticket_id = ticket_id
        self.sender_employee_id = sender_employee_id
        self.content = content
        self.date = date or datetime.utcnow().isoformat(timespec="seconds")
