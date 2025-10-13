from .employee import Employee

class Technician(Employee):
    def __init__(self, id=None, name=None, email=None, employee_category_id=None, user_id=None):
        super().__init__(id, name, email, "TECHNICIAN", employee_category_id, user_id)
