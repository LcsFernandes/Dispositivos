import pytest
import logging
from datetime import datetime
from src.data.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeMovimentacao:
    def __init__(self, id, id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo):
        self.id = id
        self.id_dispositivo = id_dispositivo
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.data_movimentacao = data_movimentacao
        self.usuario_id = usuario_id
        self.tipo = tipo

class FakeMovimentacaoRepository:
    def __init__(self, movimentacoes=None):
        self.movimentacoes = movimentacoes or []

    def get_all_movimentacoes(self):
        logger.info("Fake get_all_movimentacoes chamado")
        return self.movimentacoes

def test_listar_movimentacoes_cinco_movimentacoes():
    logger.info("Iniciando teste: test_listar_movimentacoes_cinco_movimentacoes")
    movimentacoes = [
        FakeMovimentacao(
            id=1,
            id_dispositivo=10,
            local_origem=100,
            local_destino=200,
            data_movimentacao=datetime(2025, 6, 1, 10, 0, 0),
            usuario_id=100,
            tipo=1
        ),
        FakeMovimentacao(
            id=2,
            id_dispositivo=11,
            local_origem=101,
            local_destino=201,
            data_movimentacao=datetime(2025, 6, 2, 11, 0, 0),
            usuario_id=101,
            tipo=1
        ),
        FakeMovimentacao(
            id=3,
            id_dispositivo=12,
            local_origem=102,
            local_destino=202,
            data_movimentacao=datetime(2025, 6, 3, 12, 0, 0),
            usuario_id=102,
            tipo=2
        ),
        FakeMovimentacao(
            id=4,
            id_dispositivo=13,
            local_origem=103,
            local_destino=203,
            data_movimentacao=datetime(2025, 6, 4, 13, 0, 0),
            usuario_id=103,
            tipo=2
        ),
        FakeMovimentacao(
            id=5,
            id_dispositivo=14,
            local_origem=104,
            local_destino=204,
            data_movimentacao=datetime(2025, 6, 5, 14, 0, 0),
            usuario_id=104,
            tipo=1
        ),
    ]
    repo = FakeMovimentacaoRepository(movimentacoes)
    use_case = ListarMovimentacao(repo)
    result = use_case.listar_movimentacao()
    logger.info(f"Resultado: {result}")
    assert result["type"] == "Movimentacao"
    assert len(result["data"]) == 5

    esperado = [
        {
            "id": 1,
            "id_dispositivo": 10,
            "local_origem": 100,
            "local_destino": 200,
            "data_movimentacao": datetime(2025, 6, 1, 10, 0, 0),
            "usuario_id": 100,
            "tipo": 1
        },
        {
            "id": 2,
            "id_dispositivo": 11,
            "local_origem": 101,
            "local_destino": 201,
            "data_movimentacao": datetime(2025, 6, 2, 11, 0, 0),
            "usuario_id": 101,
            "tipo": 1
        },
        {
            "id": 3,
            "id_dispositivo": 12,
            "local_origem": 102,
            "local_destino": 202,
            "data_movimentacao": datetime(2025, 6, 3, 12, 0, 0),
            "usuario_id": 102,
            "tipo": 2
        },
        {
            "id": 4,
            "id_dispositivo": 13,
            "local_origem": 103,
            "local_destino": 203,
            "data_movimentacao": datetime(2025, 6, 4, 13, 0, 0),
            "usuario_id": 103,
            "tipo": 2
        },
        {
            "id": 5,
            "id_dispositivo": 14,
            "local_origem": 104,
            "local_destino": 204,
            "data_movimentacao": datetime(2025, 6, 5, 14, 0, 0),
            "usuario_id": 104,
            "tipo": 1
        },
    ]

    for i, mov in enumerate(result["data"]):
        for campo in esperado[i]:
            assert mov[campo] == esperado[i][campo], f"Falha no campo {campo} da movimentação {i+1}"