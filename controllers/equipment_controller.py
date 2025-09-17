from flask import Blueprint, request
from repositories.equipment_repo import EquipmentRepo

bp = Blueprint("equipment", __name__, url_prefix="/equipment")
repo = EquipmentRepo()

@bp.post("")
def create_equipment():
    d = request.get_json(force=True, silent=True) or request.form
    eid = repo.create(d["name"], d["serial"], d.get("equipment_category_id"))
    return {"id": eid}, 201

@bp.get("")
def list_equipment():
    return repo.list()

@bp.patch("/<int:equipment_id>")
def update_equipment(equipment_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(equipment_id, **d)
    return {"ok": True}

@bp.delete("/<int:equipment_id>")
def delete_equipment(equipment_id:int):
    repo.delete(equipment_id)
    return {"ok": True}
