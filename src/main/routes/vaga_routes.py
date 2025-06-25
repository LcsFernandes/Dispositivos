from flask import Blueprint, request
import json

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.vaga.alterar_vaga_composer import alterar_vaga_composer
from src.main.composers.vaga.buscar_vaga_by_id_composer import buscar_vaga_by_id_composer
from src.main.composers.vaga.buscar_vaga_by_identificacao_composer import buscar_vaga_by_identificacao_composer
from src.main.composers.vaga.inserir_vaga_composer import inserir_vaga_composer
from src.main.composers.vaga.listar_vaga_composer import listar_vaga_composer

# from src.validators.vaga_validator import inserir_vaga_validator, alterar_vaga_validator
# from src.validators.general_validators import codigo_validator, id_validator

from src.errors.error_handle import handle_errors

vaga_route_bp = Blueprint("vaga_routes", __name__)


@vaga_route_bp.route("/vaga/list", methods=["GET"])
def listar_vagas():
    http_response = None
    
    try:
        http_response = request_adapter(request, listar_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@vaga_route_bp.route("/vaga", methods=["POST"])
def inserir_vaga():
    http_response = None
    
    try:
        inserir_vaga_validator(request.get_json())
        http_response = request_adapter(request, inserir_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@vaga_route_bp.route("/vaga", methods=["PUT"])
def alterar_vaga():
    http_response = None
    
    try:
        alterar_vaga_validator(request.get_json())
        http_response = request_adapter(request, alterar_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@vaga_route_bp.route("/vaga/find_by_id/<id_vaga>", methods=["GET"])
def buscar_vaga_by_id(id):
    http_response = None
    
    try:
        id_vaga = request.view_args["id_vaga"]
        id_validator(id_vaga)

        request.view_args["id_vaga"] = int(id_vaga)
        http_response = request_adapter(request, buscar_vaga_by_id_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code


@vaga_route_bp.route("/vaga/find_by_identificacao/<identificacao>", methods=["GET"])
def buscar_vaga_by_identificacao(identificacao):
    http_response = None
    
    try:
        codigo_validator(identificacao)
        http_response = request_adapter(request, buscar_vaga_by_identificacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return json.dumps(http_response.body), http_response.status_code