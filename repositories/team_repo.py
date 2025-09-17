from .base import BaseRepo

class TeamRepo(BaseRepo):
    def create(self, name: str, description: str | None = None) -> int:
        return self.execute("INSERT INTO team (name,description) VALUES (?,?)", (name, description))

    def get(self, id: int): return self.fetch_one("SELECT * FROM team WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM team ORDER BY id DESC")
    def update(self, id: int, name: str, description: str | None):
        return self.execute("UPDATE team SET name=?, description=? WHERE id=?", (name, description, id))
    def delete(self, id: int): return self.execute("DELETE FROM team WHERE id=?", (id,))

    def add_member(self, team_id: int, employee_id: int):
        return self.execute(
            "INSERT OR IGNORE INTO team_employee (team_id,employee_id) VALUES (?,?)",
            (team_id, employee_id),
        )
