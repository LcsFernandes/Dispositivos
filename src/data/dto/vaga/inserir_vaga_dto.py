from dataclasses import dataclass

@dataclass(frozen=True)
class InserirVagaDTO:
    identificacao: int