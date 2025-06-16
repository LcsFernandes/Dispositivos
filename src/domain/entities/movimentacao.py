from datetime import datetime

class Movimentacao:
    def __init__(self, id: int, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, login_id: int):
        self.id = id
        self.id_dispositivo = id_dispositivo
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.data_movimentacao = data_movimentacao
        self.login_id = login_id

        