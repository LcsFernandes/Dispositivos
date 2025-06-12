from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class ListarDispositivosDTO:
    tipo: Optional[int] = None
    status: Optional[int] = None