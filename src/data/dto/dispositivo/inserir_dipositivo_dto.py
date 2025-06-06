from datetime import datetime
from typing import Optional

class InserirDispositivoDTO:
    def __init__(
        self,
        codigo: str,
        tipo: int,
        descricao: str,
        vaga: str,
        status: int,
        data_fabricacao: datetime,
        cliente: Optional[str]
    ):
        self.codigo = codigo
        self.tipo = tipo
        self.descricao = descricao
        self.vaga = vaga
        self.status = status
        self.data_fabricacao = data_fabricacao
        self.cliente = cliente
