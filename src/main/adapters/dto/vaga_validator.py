from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def alterar_vaga_validator(data: dict):
    query_validator = Validator({
        "id_dispositivo": {"type": "integer", "required": False, "empty": False},
        "identificacao": {"type": "string", "required": False, "empty": False},
    })
    response = query_validator.validate(data)
    if not response:
        raise HttpUnprocessableEntityError(query_validator.errors)
    
def inserir_vaga_validator(data: dict):
    query_validator = Validator({
        "id_dispositivo": {"type": "integer", "required": True, "empty": False},
        "identificacao": {"type": "string", "required": True, "empty": False},
    })
    response = query_validator.validate(data)
    if not response:
        raise HttpUnprocessableEntityError(query_validator.errors)