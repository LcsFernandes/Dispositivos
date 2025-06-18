from flask import Flask, request
from src.main.routes.dispositivo_routes import dispositivo_route_bp
from src.main.routes.movimentacao_routes import movimentacao_route_bp
from src.main.routes.vaga_routes import vaga_route_bp
from src.infra.logger.logger import get_logger
import time

app = Flask(__name__)

app.register_blueprint(dispositivo_route_bp)
app.register_blueprint(movimentacao_route_bp)
app.register_blueprint(vaga_route_bp)

logger = get_logger()

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    duration = time.time() - getattr(request, 'start_time', time.time())
    # Parâmetros enviados (query, form, json)
    params = {
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True)
    }
    # Corpo da resposta (atenção: pode ser grande!)
    response_data = response.get_data(as_text=True)
    logger.info(
        f"{request.method} {request.path} | Status: {response.status_code} | Tempo: {duration:.4f}s | "
        f"IP: {request.remote_addr} | Params: {params} | Response: {response_data}"
    )
    return response