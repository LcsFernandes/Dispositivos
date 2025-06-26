from pydantic import BaseModel, Field, constr
from typing import Optional

class InserirVagaDTO(BaseModel):
    identificacao: str

    class Config:
        extra = "forbid"

class AlterarVagaDTO(BaseModel):
    identificacao: str

    class Config:
        extra = "forbid"