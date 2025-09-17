from .base import BaseRepo

class EquipmentCategoryRepo(BaseRepo):
    def create(self, name: str, description: str | None = None) -> int:
        return self.execute("INSERT INTO equipment_category (name,description) VALUES (?,?)", (name, description))

    def get(self, id: int): return self.fetch_one("SELECT * FROM equipment_category WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM equipment_category ORDER BY name")
    def update(self, id: int, name: str, description: str | None):
        return self.execute("UPDATE equipment_category SET name=?, description=? WHERE id=?", (name, description, id))
    def delete(self, id: int): return self.execute("DELETE FROM equipment_category WHERE id=?", (id,))
