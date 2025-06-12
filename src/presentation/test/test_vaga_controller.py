import pytest
import logging
from unittest.mock import MagicMock
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.controllers.vaga_controller import (
    AlterarVagaController,
    BuscarVagaByIdController,
    BuscarVagaByIdentificacaoController,
    ListarVagasController,
    InserirVagaController,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_alterar_vaga_controller():
    logger.info("Iniciando teste: test_alterar_vaga_controller")
    use_case = MagicMock()
    use_case.alterar_vaga.return_value = {"msg": "vaga alterada"}
    controller = AlterarVagaController(use_case)
    req = HttpRequest(body={"id": 1, "identificacao": "A12"})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 201
    assert resp.body["msg"] == "vaga alterada"

def test_buscar_vaga_by_id_controller():
    logger.info("Iniciando teste: test_buscar_vaga_by_id_controller")
    use_case = MagicMock()
    vaga = {"id": 1, "deposito_id": 74, "identificacao": "A12"}
    use_case.buscar_vaga_by_id.return_value = vaga
    controller = BuscarVagaByIdController(use_case)
    req = HttpRequest(path_params={"id": 1})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == vaga

def test_buscar_vaga_by_identificacao_controller():
    logger.info("Iniciando teste: test_buscar_vaga_by_identificacao_controller")
    use_case = MagicMock()
    vaga = {"id": 1, "deposito_id": 74, "identificacao": "A12"}
    use_case.buscar_vaga_by_identificacao.return_value = vaga
    controller = BuscarVagaByIdentificacaoController(use_case)
    req = HttpRequest(path_params={"identificacao": "A12"})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == vaga

def test_listar_vagas_controller():
    logger.info("Iniciando teste: test_listar_vagas_controller")
    use_case = MagicMock()
    vagas = [
        {"id": 1, "deposito_id": 74, "identificacao": "A12"},
        {"id": 2, "deposito_id": 74, "identificacao": "B13"},
        {"id": 3, "deposito_id": 74, "identificacao": "C14"},
    ]
    use_case.listar_vagas.return_value = vagas
    controller = ListarVagasController(use_case)
    req = HttpRequest()
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == vagas
    assert len(list(resp.body)[0]) == 3

def test_inserir_vaga_controller():
    logger.info("Iniciando teste: test_inserir_vaga_controller")
    use_case = MagicMock()
    use_case.inserir_vaga.return_value = {"msg": "vaga inserida"}
    controller = InserirVagaController(use_case)
    req = HttpRequest(body={"deposito_id": 74, "identificacao": "A12"})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 201
    assert resp.body["msg"] == "vaga inserida"