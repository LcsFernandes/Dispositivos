from typing import Optional

class ListarDispositivosDTO:
    def __init__(self, tipo: Optional[int] = None, status: Optional[int] = None):
        self.tipo = tipo
        self.status = status