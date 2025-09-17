from flask import Blueprint, request
from repositories.user_repo import UserRepo

bp = Blueprint("auth", __name__, url_prefix="/auth")
repo = UserRepo()

@bp.post("/register")
def register():
    d = request.get_json(force=True, silent=True) or request.form
    uid = repo.create(d["username"], d["password"], d["email"], d.get("name"))
    return {"id": uid}, 201
