from flask_openapi3 import APIBlueprint
from flask import request
from repositories.category_repo import CategoryRepo

bp = APIBlueprint("categories", __name__, url_prefix="/categories")
repo = CategoryRepo()

@bp.post("")
def create_category():
    d = request.get_json(force=True, silent=True) or request.form
    cid = repo.create(d["name"], d.get("description"))
    return {"id": cid}, 201

@bp.get("")
def list_categories():
    return repo.list()

@bp.patch("/<int:category_id>")
def update_category(category_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.update(category_id, d["name"], d.get("description"))
    return {"ok": True}

@bp.delete("/<int:category_id>")
def delete_category(category_id:int):
    repo.delete(category_id)
    return {"ok": True}
