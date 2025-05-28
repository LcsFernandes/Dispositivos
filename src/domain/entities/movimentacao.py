from datetime import datetime

class Movimentacao:
    def __init__(self, id: int, local_origem: int, local_destino: int, data_movimentacao: datetime, usuario_id: int, tipo: int):
        self.id = id
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.data_movimentacao = data_movimentacao
        self.usuario_id = usuario_id
        self.tipo = tipo

        