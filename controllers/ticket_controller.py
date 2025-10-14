from flask_openapi3 import APIBlueprint
from flask import request
from repositories.ticket_repo import TicketRepo

bp = APIBlueprint("tickets", __name__, url_prefix="/tickets")
repo = TicketRepo()

@bp.post("")
def open_ticket():
    d = request.get_json(force=True, silent=True) or request.form
    tid = repo.create(
        client_id=int(d["client_id"]),
        reporter_employee_id=d.get("reporter_employee_id"),
        team_id=d.get("team_id"),
        state="OPEN",
    )
    return {"id": tid}, 201

@bp.post("/<int:ticket_id>/employees")
def link_employee(ticket_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.add_employee(ticket_id, int(d["employee_id"]))
    return {"ok": True}

@bp.post("/<int:ticket_id>/services")
def link_service(ticket_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.add_service(ticket_id, int(d["service_id"]))
    return {"ok": True}

@bp.patch("/<int:ticket_id>/state")
def set_state(ticket_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.set_state(ticket_id, d["state"])
    return {"ok": True}

@bp.get("")
def list_tickets():
    return repo.list()

@bp.get("/<int:ticket_id>")
def get_ticket(ticket_id:int):
    return repo.get(ticket_id) or ({"error":"not found"}, 404)
