from dataclasses import dataclass

@dataclass(frozen=True)
class RegistrarMovimentacaoDTO:
    codigo: str
    local_origem: str
    local_destino: str
    login_id: int