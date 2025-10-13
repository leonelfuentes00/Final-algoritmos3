class WorkLog:
    def __init__(self, id=None, technician_employee_id=None, ticket_id=None,
                 start_at=None, end_at=None, notes=None):
        self.id = id
        self.technician_employee_id = technician_employee_id
        self.ticket_id = ticket_id
        self.start_at = start_at
        self.end_at = end_at
        self.notes = notes
