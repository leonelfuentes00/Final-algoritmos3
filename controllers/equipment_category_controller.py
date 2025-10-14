from flask_openapi3 import APIBlueprint
from flask import request
from repositories.equipment_category_repo import EquipmentCategoryRepo

bp = APIBlueprint("equipment_categories", __name__, url_prefix="/equipment-categories")
repo = EquipmentCategoryRepo()

@bp.post("")
def create_equipment_category():
    d = request.get_json(force=True, silent=True) or request.form
    eid = repo.create(d["name"], d.get("description"))
    return {"id": eid}, 201

@bp.get("")
def list_equipment_categories():
    return repo.list()

@bp.patch("/<int:ec_id>")
def update_equipment_category(ec_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(ec_id, d["name"], d.get("description"))
    return {"ok": True}

@bp.delete("/<int:ec_id>")
def delete_equipment_category(ec_id:int):
    repo.delete(ec_id)
    return {"ok": True}
