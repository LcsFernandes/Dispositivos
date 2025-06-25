from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def inserir_movimentacao_validator(data: dict):
    query_validator = Validator({
        "codigo": {"type": "string", "required": True, "empty": False},
        "local_origem": {"type": "string", "required": True, "empty": False},
        "local_destino": {"type": "string", "required": True, "empty": False},
        "login_id": {"type": "integer", "required": True, "empty": False},
    })
    response = query_validator.validate(data)
    if not response:
        raise HttpUnprocessableEntityError(query_validator.errors)