from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import date

class InserirDispositivoDTO(BaseModel):
    codigo: str
    tipo: int
    descricao: str
    status: int
    data_fabricacao: date
    cliente: Optional[str] = None  

class AlterarDispositivoDTO(BaseModel):
    id: int
    codigo: Optional[str] = None
    tipo: Optional[int] = None
    descricao: Optional[str] = None
    status: Optional[int] = None
    data_fabricacao: Optional[date] = None
    cliente: Optional[str] = None 

class VerificarCodigoDispositivoDTO(BaseModel):
    codigo: str