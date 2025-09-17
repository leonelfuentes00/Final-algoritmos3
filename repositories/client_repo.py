from .base import BaseRepo

class ClientRepo(BaseRepo):
    def create(self, name: str, email: str, phone: str | None = None, address: str | None = None) -> int:
        return self.execute(
            "INSERT INTO client (name,email,phone,address) VALUES (?,?,?,?)", (name, email, phone, address)
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM client WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM client ORDER BY id DESC")
    def update(self, id: int, **fields):
        cols = []
        vals = []
        for k, v in fields.items():
            cols.append(f"{k}=?")
            vals.append(v)
        vals.append(id)
        return self.execute(f"UPDATE client SET {', '.join(cols)} WHERE id=?", vals)
    def delete(self, id: int): return self.execute("DELETE FROM client WHERE id=?", (id,))
