from flask import Blueprint, request
from repositories.client_repo import ClientRepo

bp = Blueprint("clients", __name__, url_prefix="/clients")
repo = ClientRepo()

@bp.post("")
def create_client():
    d = request.get_json(force=True, silent=True) or request.form
    cid = repo.create(d["name"], d["email"], d.get("phone"), d.get("address"))
    return {"id": cid}, 201

@bp.get("")
def list_clients():
    return repo.list()

@bp.get("/<int:client_id>")
def get_client(client_id: int):
    return repo.get(client_id) or ({"error": "not found"}, 404)

@bp.patch("/<int:client_id>")
def update_client(client_id: int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(client_id, **d)
    return {"ok": True}

@bp.delete("/<int:client_id>")
def delete_client(client_id: int):
    repo.delete(client_id)
    return {"ok": True}
