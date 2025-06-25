from dataclasses import dataclass

@dataclass(frozen=True)
class BuscarMovimentacaoDTO:
    codigo: str