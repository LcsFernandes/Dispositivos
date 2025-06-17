from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class InserirDispositivoDTO:
    codigo: str
    tipo: int
    descricao: str
    status: int
    data_fabricacao: datetime
    cliente: Optional[str] = None
