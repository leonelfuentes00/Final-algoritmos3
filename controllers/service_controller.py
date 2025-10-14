from flask_openapi3 import APIBlueprint
from flask import request
from repositories.service_repo import ServiceRepo

bp = APIBlueprint("services", __name__, url_prefix="/services")
repo = ServiceRepo()

@bp.post("")
def create_service():
    d = request.get_json(force=True, silent=True) or request.form
    sid = repo.create(d["name"], d.get("description"), d.get("category_id"))
    return {"id": sid}, 201

@bp.get("")
def list_services():
    return repo.list()

@bp.patch("/<int:service_id>")
def update_service(service_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(service_id, **d)
    return {"ok": True}

@bp.delete("/<int:service_id>")
def delete_service(service_id:int):
    repo.delete(service_id)
    return {"ok": True}
