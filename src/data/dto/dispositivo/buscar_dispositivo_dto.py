from typing import Optional

class BuscarDispositivoDTO:
    def __init__(self, id: Optional[int] = None, codigo: Optional[str] = None):
        self.id = id
        self.codigo = codigo