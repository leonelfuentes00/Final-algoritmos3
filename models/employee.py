class Employee:
    def __init__(self, id=None, name=None, email=None, employee_type=None,
                 employee_category_id=None, user_id=None):
        self.id = id
        self.name = name
        self.email = email
        self.employee_type = employee_type  # ADMINISTRATOR / OPERATOR / TECHNICIAN
        self.employee_category_id = employee_category_id
        self.user_id = user_id
