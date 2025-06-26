from pydantic import BaseModel, Field, constr
from typing import Optional

class InserirMovimentacaoDTO(BaseModel):
    codigo: str
    local_origem: str
    local_destino: str
    login_id: int

    class Config:
        extra = "forbid"