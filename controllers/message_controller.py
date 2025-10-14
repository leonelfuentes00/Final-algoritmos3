from flask_openapi3 import APIBlueprint
from flask import request
from repositories.message_repo import MessageRepo

bp = APIBlueprint("messages", __name__, url_prefix="/messages")
repo = MessageRepo()

@bp.post("")
def create_message():
    d = request.get_json(force=True, silent=True) or request.form
    mid = repo.create(int(d["ticket_id"]), int(d["sender_employee_id"]), d["content"])
    return {"id": mid}, 201

@bp.get("/by-ticket/<int:ticket_id>")
def list_messages(ticket_id:int):
    return repo.list_by_ticket(ticket_id)
