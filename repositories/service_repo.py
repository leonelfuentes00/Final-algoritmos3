from .base import BaseRepo

class ServiceRepo(BaseRepo):
    def create(self, name: str, description: str | None = None, category_id: int | None = None) -> int:
        return self.execute(
            "INSERT INTO service (name,description,category_id) VALUES (?,?,?)",
            (name, description, category_id),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM service WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM service ORDER BY id DESC")
    def update(self, id: int, **fields):
        cols, vals = [], []
        for k, v in fields.items():
            cols.append(f"{k}=?"); vals.append(v)
        vals.append(id)
        return self.execute(f"UPDATE service SET {', '.join(cols)} WHERE id=?", vals)
    def delete(self, id: int): return self.execute("DELETE FROM service WHERE id=?", (id,))
