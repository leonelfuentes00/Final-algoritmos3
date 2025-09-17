from .base import BaseRepo

class UserRepo(BaseRepo):
    def create(self, username: str, password_hash: str, email: str, name: str | None = None) -> int:
        return self.execute(
            "INSERT INTO user (username,password_hash,email,name) VALUES (?,?,?,?)",
            (username, password_hash, email, name),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM user WHERE id=?", (id,))
    def get_by_username(self, username: str): return self.fetch_one("SELECT * FROM user WHERE username=?", (username,))
    def list(self): return self.fetch_all("SELECT * FROM user ORDER BY id DESC")
    def delete(self, id: int): return self.execute("DELETE FROM user WHERE id=?", (id,))
