from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class AlterarVagaDTO:
    id: int
    deposito_id: Optional[int] = None
    identificacao: Optional[str] = None
        