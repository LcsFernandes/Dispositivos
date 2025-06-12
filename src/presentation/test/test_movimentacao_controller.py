import pytest
import logging
from unittest.mock import MagicMock
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.controllers.movimentacao_controller import (
    BuscarMovimentacaoController,
    ListarMovimentacaoController,
    RegistrarMovimentacaoController,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_buscar_movimentacao_controller():
    logger.info("Iniciando teste: test_buscar_movimentacao_controller")
    use_case = MagicMock()
    movimentacao = {
        "id": 1,
        "id_dispositivo": 10,
        "local_origem": 1,
        "local_destino": 2,
        "data_movimentacao": "2025-01-01 10:00:00",
        "usuario_id": 100,
        "tipo": 1
    }
    use_case.buscar_movimentacao.return_value = movimentacao
    controller = BuscarMovimentacaoController(use_case)
    req = HttpRequest(path_params={"id_dispositivo": 10})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == movimentacao

def test_listar_movimentacao_controller():
    logger.info("Iniciando teste: test_listar_movimentacao_controller")
    use_case = MagicMock()
    movimentacoes = [
        {
            "id": 1,
            "id_dispositivo": 10,
            "local_origem": 1,
            "local_destino": 2,
            "data_movimentacao": "2025-01-01 10:00:00",
            "usuario_id": 100,
            "tipo": 1
        },
        {
            "id": 2,
            "id_dispositivo": 11,
            "local_origem": 2,
            "local_destino": 3,
            "data_movimentacao": "2025-01-02 11:00:00",
            "usuario_id": 101,
            "tipo": 2
        }
    ]
    use_case.listar_movimentacao.return_value = movimentacoes
    controller = ListarMovimentacaoController(use_case)
    req = HttpRequest()
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == movimentacoes
    assert len(resp.body) == 2

def test_registrar_movimentacao_controller():
    logger.info("Iniciando teste: test_registrar_movimentacao_controller")
    use_case = MagicMock()
    movimentacao = {
        "id": 1,
        "id_dispositivo": 10,
        "local_origem": 1,
        "local_destino": 2,
        "data_movimentacao": "2025-01-01 10:00:00",
        "usuario_id": 100,
        "tipo": 1
    }
    use_case.registrar_movimentacao.return_value = movimentacao
    controller = RegistrarMovimentacaoController(use_case)
    req = HttpRequest(body={
        "id_dispositivo": 10,
        "local_origem": 1,
        "local_destino": 2,
        "data_movimentacao": "2025-01-01 10:00:00",
        "usuario_id": 100,
        "tipo": 1
    })
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 201
    assert resp.body == movimentacao