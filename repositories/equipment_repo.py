from .base import BaseRepo

class EquipmentRepo(BaseRepo):
    def create(self, name: str, serial: str, equipment_category_id: int | None = None) -> int:
        return self.execute(
            "INSERT INTO equipment (name,serial,equipment_category_id) VALUES (?,?,?)",
            (name, serial, equipment_category_id),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM equipment WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM equipment ORDER BY id DESC")
    def update(self, id: int, **fields):
        cols, vals = [], []
        for k, v in fields.items():
            cols.append(f"{k}=?"); vals.append(v)
        vals.append(id)
        return self.execute(f"UPDATE equipment SET {', '.join(cols)} WHERE id=?", vals)
    def delete(self, id: int): return self.execute("DELETE FROM equipment WHERE id=?", (id,))
