from dataclasses import dataclass

@dataclass(frozen=True)
class BuscarVagaByIdentificacaoDTO:
    identificacao: str