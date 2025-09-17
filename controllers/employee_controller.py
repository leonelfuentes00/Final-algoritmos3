from flask import Blueprint, request
from repositories.employee_repo import EmployeeRepo

bp = Blueprint("employees", __name__, url_prefix="/employees")
repo = EmployeeRepo()

@bp.post("")
def create_employee():
    d = request.get_json(force=True, silent=True) or request.form
    eid = repo.create(d["name"], d["email"], d["employee_type"], d.get("employee_category_id"), d.get("user_id"))
    return {"id": eid}, 201

@bp.get("")
def list_employees():
    return repo.list()

@bp.get("/<int:employee_id>")
def get_employee(employee_id:int):
    return repo.get(employee_id) or ({"error":"not found"}, 404)

@bp.patch("/<int:employee_id>")
def update_employee(employee_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(employee_id, **d)
    return {"ok": True}

@bp.delete("/<int:employee_id>")
def delete_employee(employee_id:int):
    repo.delete(employee_id)
    return {"ok": True}
