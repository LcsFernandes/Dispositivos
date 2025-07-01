from pydantic import BaseModel, Field, constr
from typing import Optional, Dict
from datetime import date

class InserirDispositivoDTO(BaseModel):
    codigo: str
    tipo: int
    descricao: str
    status: int
    data_fabricacao: date
    cliente: Optional[str] = None

    class Config:
        extra = "forbid"

class AlterarDispositivoDTO(BaseModel):
    codigo: Optional[str] = None
    tipo: Optional[int] = None
    descricao: Optional[str] = None
    status: Optional[int] = None
    data_fabricacao: Optional[date] = None
    cliente: Optional[str] = None
    
    class Config:
        extra = "forbid"

class DispositivoData(BaseModel):
    codigo: str
    tipo: int
    descricao: str
    status: int
    data_fabricacao: date
    cliente: Optional[str] = None

class DispositivoOutputDTO(BaseModel):
    type: str = Field("Dispositivos")
    data: DispositivoData

class VerificarStatusDispositivo(BaseModel):
    codigo: str
    status: str

class VerificarStatusDispositivoOutput(BaseModel):
    type: str = Field("Dispositivos")
    data: VerificarStatusDispositivo



