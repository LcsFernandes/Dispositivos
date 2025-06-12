from dataclasses import dataclass

@dataclass(frozen=True)
class ExcluirDispositivoDTO:
    codigo: str
