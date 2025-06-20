from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class RegistrarMovimentacaoDTO:
    id_dispositivo: int
    local_origem: int
    local_destino: int
    login_id: int