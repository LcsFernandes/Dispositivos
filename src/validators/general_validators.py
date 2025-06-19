from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def codigo_validator(codigo: str):
    if not isinstance(codigo, str) or not codigo.strip():
        raise HttpUnprocessableEntityError("Codigo inválido.")

    
def id_validator(id_dispositivo: str):
    try:
        id_dispositivo = int(id_dispositivo)

        if id_dispositivo <= 0:
            raise HttpUnprocessableEntityError("Id deve ser um numero inteiro positivo")
    except Exception:
       raise HttpUnprocessableEntityError("Id deve ser um numero inteiro positivo") 