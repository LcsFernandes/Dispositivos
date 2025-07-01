from dataclasses import dataclass

@dataclass(frozen=True)
class ListarMovimentacaoDTO:
    page: int
    page_size: int