from flask import Flask
from src.main.routes.dispositivo_routes import dispositivo_route_bp
from src.main.routes.movimentacao_routes import movimentacao_route_bp
from src.main.routes.vaga_routes import vaga_route_bp

app = Flask(__name__)

app.register_blueprint(dispositivo_route_bp)
app.register_blueprint(movimentacao_route_bp)
app.register_blueprint(vaga_route_bp)
