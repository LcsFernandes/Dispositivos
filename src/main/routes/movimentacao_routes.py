from flask import Blueprint, request, jsonify

from src.data.dto.movimentacao.buscar_movimentacao_dto import BuscarMovimentacaoDTO
from src.data.dto.movimentacao.registrar_movimentacao_dto import RegistrarMovimentacaoDTO

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.movimentacao.buscar_movimentacao_composer import buscar_movimentacao_composer
from src.main.composers.movimentacao.registar_movimentacao_composer import registrar_movimentacao_composer
from src.main.composers.movimentacao.listar_movimentacao_composer import listar_movimentacao_composer

from src.errors.error_handle import handle_errors

movimentacao_route_bp = Blueprint("movimentacao_routes", __name__)


@movimentacao_route_bp.route("/movimentacao/list", methods=["GET"])
def listar_movimentacoes():
    http_response = None
    
    try:
        http_response = request_adapter(request, listar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code

@movimentacao_route_bp.route("/movimentacao", methods=["POST"])
def registrar_movimentacao():
    http_response = None
    
    try:
        http_response = request_adapter(request, registrar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code

@movimentacao_route_bp.route("/movimentacao/find/<int:id_dispositivo>", methods=["GET"])
def buscar_movimentacao(id_dispositivo):
    http_response = None
    
    try:
        http_response = request_adapter(request, buscar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code