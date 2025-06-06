from datetime import datetime
from typing import Optional

class AlterarDispositivoDTO:
    def __init__(
        self,
        id: int,
        codigo: Optional[str] = None,
        tipo: Optional[int] = None,
        descricao: Optional[str] = None,
        vaga: Optional[str] = None,
        status: Optional[int] = None,
        data_fabricacao: Optional[datetime] = None,
        cliente: Optional[str] = None
    ):
        self.id = id
        self.codigo = codigo
        self.tipo = tipo
        self.descricao = descricao
        self.vaga = vaga
        self.status = status
        self.data_fabricacao = data_fabricacao
        self.cliente = cliente