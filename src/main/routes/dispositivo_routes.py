from flask import Blueprint, request
import json
from src.main.adapters.request_adapter import request_adapter

from src.main.composers.dispositivo.alterar_dispositivo_composer import alterar_dispositivo_composer
from src.main.composers.dispositivo.buscar_dispositivo_by_codigo_composer import buscar_dispositivo_by_codigo_composer
from src.main.composers.dispositivo.buscar_dispositivo_by_id_composer import buscar_dispositivo_by_id_composer
from src.main.composers.dispositivo.excluir_dispositivo_composer import excluir_dispositivo_composer
from src.main.composers.dispositivo.inserir_dispositivo_composer import inserir_dispositivo_composer
from src.main.composers.dispositivo.listar_dispositivo_composer import listar_dispositivo_composer
from src.main.composers.dispositivo.verificar_status_dispositivo_composer import verificar_status_dispositivo_composer

from src.errors.error_handle import handle_errors

dispositivo_route_bp = Blueprint("dispositivo_routes", __name__)

@dispositivo_route_bp.route("/dispositivo/list", methods=["GET"])
def listar_dispositivos():
    http_response = None
    
    try:
        http_response = request_adapter(request, listar_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@dispositivo_route_bp.route("/dispositivo", methods=["POST"])
def inserir_dispositivo():
    http_response = None
    
    try:
        http_response = request_adapter(request, inserir_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@dispositivo_route_bp.route("/dispositivo/<int:id_dispositivo>", methods=["PUT"])
def alterar_dispositivo(id_dispositivo):
    http_response = None
    
    try:
        http_response = request_adapter(request, alterar_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@dispositivo_route_bp.route("/dispositivo/<string:codigo>", methods=["DELETE"])
def excluir_dispositivo(codigo):
    http_response = None
    
    try:
        http_response = request_adapter(request, excluir_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@dispositivo_route_bp.route("/dispositivo/find_by_id/<int:id>", methods=["GET"])
def buscar_dispositivo_by_id(id):
    http_response = None
    
    try:
        http_response = request_adapter(request, buscar_dispositivo_by_id_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@dispositivo_route_bp.route("/dispositivo/find_by_codigo/<string:codigo>", methods=["GET"])
def buscar_dispositivo_by_codigo(codigo):
    http_response = None
    
    try:
        http_response = request_adapter(request, buscar_dispositivo_by_codigo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code



@dispositivo_route_bp.route("/dispositivo/verificar_status", methods=["GET"])
def verificar_status_dispositivo():
    http_response = None
    
    try:
        http_response = request_adapter(request, verificar_status_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code