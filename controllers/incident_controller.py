from flask_openapi3 import APIBlueprint
from flask import request
from repositories.incident_repo import IncidentRepo

bp = APIBlueprint("incidents", __name__, url_prefix="/incidents")
repo = IncidentRepo()

@bp.post("")
def create_incident():
    d = request.get_json(force=True, silent=True) or request.form
    iid = repo.create(int(d["ticket_id"]), d["description"])
    return {"id": iid}, 201

@bp.get("/by-ticket/<int:ticket_id>")
def list_incidents(ticket_id:int):
    return repo.list_by_ticket(ticket_id)
