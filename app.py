from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from database.database import init_db
import os

# Inicializa la base de datos
init_db()

# Definición básica de OpenAPI
info = Info(title="Helpdesk API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Importar y registrar blueprints
from controllers.auth_controller import bp as auth_bp
from controllers.client_controller import bp as client_bp
from controllers.employee_controller import bp as employee_bp
from controllers.category_controller import bp as category_bp
from controllers.service_controller import bp as service_bp
from controllers.equipment_category_controller import bp as ecat_bp
from controllers.equipment_controller import bp as equip_bp
from controllers.team_controller import bp as team_bp
from controllers.ticket_controller import bp as ticket_bp
from controllers.incident_controller import bp as incident_bp
from controllers.message_controller import bp as message_bp
from controllers.work_controller import bp as work_bp

# Registrar blueprints
app.register_api(auth_bp)
app.register_api(client_bp)
app.register_api(employee_bp)
app.register_api(category_bp)
app.register_api(service_bp)
app.register_api(ecat_bp)
app.register_api(equip_bp)
app.register_api(team_bp)
app.register_api(ticket_bp)
app.register_api(incident_bp)
app.register_api(message_bp)
app.register_api(work_bp)

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/apidocs"                  # URL que abrirás en el navegador
API_URL = "/static/swagger.yaml"          # Archivo YAML accesible

swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Helpdesk API"}
)

app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
