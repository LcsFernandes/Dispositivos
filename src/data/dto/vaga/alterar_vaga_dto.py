from dataclasses import dataclass

@dataclass(frozen=True)
class AlterarVagaDTO:
    id: int
    identificacao: str
        