from pydantic import BaseModel, Field, constr
from typing import Optional

class InserirMovimentacaoDTO(BaseModel):
    codigo_dispositivo: str
    local_origem: str
    local_destino: str

    class Config:
        extra = "forbid"