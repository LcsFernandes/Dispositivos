from datetime import datetime

class Movimentacao:
    def __init__(self, id: int, codigo: str, local_origem: str, local_destino: str, data_movimentacao: datetime, usuario: str):
        self.id = id
        self.codigo = codigo
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.data_movimentacao = data_movimentacao
        self.usuario = usuario

        