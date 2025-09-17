from flask import Blueprint, request
from repositories.work_repo import WorkRepo

bp = Blueprint("work", __name__, url_prefix="/work")
repo = WorkRepo()

@bp.post("")
def create_work():
    d = request.get_json(force=True, silent=True) or request.form
    wid = repo.create(
        int(d["technician_employee_id"]), int(d["ticket_id"]),
        d.get("start_at"), d.get("end_at"), d.get("notes"),
    )
    return {"id": wid}, 201

@bp.get("/by-ticket/<int:ticket_id>")
def list_work(ticket_id:int):
    return repo.list_by_ticket(ticket_id)
