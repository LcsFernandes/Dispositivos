from dataclasses import dataclass

@dataclass(frozen=True)
class InserirVagaDTO:
    deposito_id: int
    idenfificacao: int