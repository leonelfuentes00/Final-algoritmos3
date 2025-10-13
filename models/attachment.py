class Attachment:
    def __init__(self, id=None, ticket_id=None, filename=None, path=None, uploaded_at=None):
        self.id = id
        self.ticket_id = ticket_id
        self.filename = filename
        self.path = path
        self.uploaded_at = uploaded_at
