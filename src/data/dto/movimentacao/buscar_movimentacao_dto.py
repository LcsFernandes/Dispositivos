from dataclasses import dataclass

@dataclass(frozen=True)
class BuscarMovimentacaoDTO:
    id_dispositivo: int