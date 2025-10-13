class User:
    def __init__(self, id=None, username=None, password_hash=None, email=None, name=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.name = name
