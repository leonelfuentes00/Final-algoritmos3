from flask import Blueprint, request
from repositories.team_repo import TeamRepo

bp = Blueprint("teams", __name__, url_prefix="/teams")
repo = TeamRepo()

@bp.post("")
def create_team():
    d = request.get_json(force=True, silent=True) or request.form
    tid = repo.create(d["name"], d.get("description"))
    return {"id": tid}, 201

@bp.post("/<int:team_id>/members")
def add_member(team_id:int):
    d = request.get_json(force=True, silent=True) or request.form
    repo.add_member(team_id, int(d["employee_id"]))
    return {"ok": True}

@bp.get("")
def list_teams():
    return repo.list()
