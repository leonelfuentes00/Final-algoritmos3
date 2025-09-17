from .base import BaseRepo

class EmployeeRepo(BaseRepo):
    def create(self, name: str, email: str, employee_type: str,
               employee_category_id: int | None = None, user_id: int | None = None) -> int:
        return self.execute(
            "INSERT INTO employee (name,email,employee_type,employee_category_id,user_id) VALUES (?,?,?,?,?)",
            (name, email, employee_type, employee_category_id, user_id),
        )

    def get(self, id: int): return self.fetch_one("SELECT * FROM employee WHERE id=?", (id,))
    def list(self): return self.fetch_all("SELECT * FROM employee ORDER BY id DESC")
    def update(self, id: int, **fields):
        cols = []
        vals = []
        for k, v in fields.items():
            cols.append(f"{k}=?")
            vals.append(v)
        vals.append(id)
        return self.execute(f"UPDATE employee SET {', '.join(cols)} WHERE id=?", vals)
    def delete(self, id: int): return self.execute("DELETE FROM employee WHERE id=?", (id,))
