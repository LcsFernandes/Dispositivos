from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class BuscarDispositivoDTO:
    id: Optional[int] = None
    codigo: Optional[str] = None