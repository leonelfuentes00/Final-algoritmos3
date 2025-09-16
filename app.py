from flask import Flask, jsonify, request
from flasgger import Swagger
import yaml
import dataclasses
from database import init_db
from managers import IncidenteManager, TicketManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
with open("swagger.yml", "r", encoding="utf-8") as f:
    swagger_template = yaml.safe_load(f)

swagger = Swagger(app, template=swagger_template)

init_db()
incidente_manager = IncidenteManager()
ticket_manager = TicketManager()

CLIENTES = ["Juan Perez", "Maria Gomez"]
SERVICIOS = ["Reparacion PC", "Instalacion de Red"]

# ------------------------------
# Endpoints de incidentes
# ------------------------------
@app.route("/api/incidentes/", methods=["GET"])
def listar_incidentes():
    """
    Lista todos los incidentes registrados.
    ---
    tags:
      - Incidentes
    """
    return jsonify([dataclasses.asdict(i) for i in incidente_manager.listar()])


@app.route("/api/incidentes/", methods=["POST"])
def crear_incidente():
    """
    Crea un nuevo incidente.
    ---
    tags:
      - Incidentes
    """
    data = request.json
    incidente = incidente_manager.crear(data["descripcion"], data["tipo"])
    return jsonify(dataclasses.asdict(incidente)), 201


@app.route("/api/incidentes/<int:incidente_id>", methods=["GET"])
def obtener_incidente(incidente_id):
    """
    Obtiene un incidente por su ID.
    ---
    tags:
      - Incidentes
    """
    incidente = incidente_manager.obtener(incidente_id)
    if incidente:
        return jsonify(dataclasses.asdict(incidente))
    return jsonify({"error": "Incidente no encontrado"}), 404


# ------------------------------
# Endpoints de tickets
# ------------------------------
@app.route("/api/tickets/", methods=["GET"])
def listar_tickets():
    """
    Lista todos los tickets registrados.
    ---
    tags:
      - Tickets
    """
    return jsonify([dataclasses.asdict(t) for t in ticket_manager.listar()])


@app.route("/api/tickets/", methods=["POST"])
def crear_ticket():
    """
    Crea un nuevo ticket.
    ---
    tags:
      - Tickets
    """
    data = request.json
    incidente = incidente_manager.obtener(data["incidente_id"])
    if not incidente:
        return jsonify({"error": "Incidente no válido"}), 400

    cliente = CLIENTES[data.get("cliente_idx", 0)]
    servicio = SERVICIOS[data.get("servicio_idx", 0)]
    ticket = ticket_manager.crear(cliente, servicio, incidente.id)
    return jsonify(dataclasses.asdict(ticket)), 201


@app.route("/api/tickets/<int:ticket_id>", methods=["GET"])
def obtener_ticket(ticket_id):
    """
    Obtiene un ticket por su ID.
    ---
    tags:
      - Tickets
    """
    ticket = ticket_manager.obtener(ticket_id)
    if ticket:
        return jsonify(dataclasses.asdict(ticket))
    return jsonify({"error": "Ticket no encontrado"}), 404


@app.route("/api/tickets/<int:ticket_id>/close", methods=["PUT"])
def cerrar_ticket(ticket_id):
    """
    Cierra un ticket.
    ---
    tags:
      - Tickets
    """
    ticket = ticket_manager.cerrar(ticket_id)
    if ticket:
        return jsonify(dataclasses.asdict(ticket))
    return jsonify({"error": "Ticket no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=8000)
