from datetime import datetime

class Dispositivo:
    def __init__(self, id: int, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str):
        self.id = id
        self.codigo = codigo
        self.tipo = tipo
        self.descricao = descricao
        self.status = status
        self.data_fabricacao = data_fabricacao
        self.cliente = cliente