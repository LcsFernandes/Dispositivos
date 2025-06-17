from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class AlterarDispositivoDTO:
    id: int
    codigo: Optional[str] = None
    tipo: Optional[int] = None
    descricao: Optional[str] = None
    status: Optional[int] = None
    data_fabricacao: Optional[datetime] = None
    cliente: Optional[str] = None