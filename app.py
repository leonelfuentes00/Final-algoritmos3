from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from database.database import init_db
import yaml, os

init_db()

app = Flask(__name__)
CORS(app)

with open(os.path.join("docs", "swagger.yaml"), "r", encoding="utf-8") as f:
    template = yaml.safe_load(f)
Swagger(app, template=template)

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

app.register_blueprint(auth_bp)
app.register_blueprint(client_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(category_bp)
app.register_blueprint(service_bp)
app.register_blueprint(ecat_bp)
app.register_blueprint(equip_bp)
app.register_blueprint(team_bp)
app.register_blueprint(ticket_bp)
app.register_blueprint(incident_bp)
app.register_blueprint(message_bp)
app.register_blueprint(work_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
