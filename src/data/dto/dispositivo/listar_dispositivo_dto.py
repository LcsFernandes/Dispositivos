from dataclasses import dataclass

@dataclass(frozen=True)
class ListarDispositivoDTO:
    page: int
    page_size: int
