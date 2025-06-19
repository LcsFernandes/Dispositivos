from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def inserir_dispositivo_validator(data: dict):
    query_validator = Validator({
        "codigo": {"type": "string", "required": True, "empty": False},
        "tipo": {"type": "integer", "required": True, "empty": False},
        "descricao": {"type": "string", "required": True, "empty": False},
        "status": {"type": "integer", "required": True, "empty": False},
        "data_fabricacao": {"type": "string", "required": True, "empty": False, "regex": r"^\d{4}-\d{2}-\d{2}$"},
        "cliente": {"type": "string", "required": False, "empty": True}
    })
    response = query_validator.validate(data)
    if not response:
        raise HttpUnprocessableEntityError(query_validator.errors)
    
def alterar_dispositivo_validator(data: dict):
    query_validator = Validator({
        "codigo": {"type": "string", "required": False, "empty": False},
        "tipo": {"type": "integer", "required": False, "empty": False},
        "descricao": {"type": "string", "required": False, "empty": False},
        "status": {"type": "integer", "required": False, "empty": False},
        "data_fabricacao": {"type": "string", "required": False, "empty": False, "regex": r"^\d{4}-\d{2}-\d{2}$"},
        "cliente": {"type": "string", "required": False, "empty": False}
    })
    response = query_validator.validate(data)
    if not response:
        raise HttpUnprocessableEntityError(query_validator.errors)
    

