from .base import BaseRepo

class CategoryRepo(BaseRepo):
    def create(self, name: str, description: str | None = None) -> int:
        return self.execute("INSERT INTO category (name,description) VALUES (?,?)", (name, description))

    def get(self, id: int): return self.fetch_one("SELECT * FROM category WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM category ORDER BY name")
    def update(self, id: int, name: str, description: str | None):
        return self.execute("UPDATE category SET name=?, description=? WHERE id=?", (name, description, id))
    def delete(self, id: int): return self.execute("DELETE FROM category WHERE id=?", (id,))
