import pytest
import logging
from unittest.mock import MagicMock
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.controllers.dispositivo_controller import (
    AlterarDispositivoController,
    BuscarDispositivosByCodigoController,
    BuscarDispositivoByIdController,
    ExcluirDispositivoController,
    InserirDispositivoController,
    ListarDispositivoController,
    VerificarStatusDispositivoController,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_alterar_dispositivo_controller():
    logger.info("Iniciando teste: test_alterar_dispositivo_controller")
    use_case = MagicMock()
    use_case.alterar_dispositivo.return_value = {"msg": "ok"}
    controller = AlterarDispositivoController(use_case)
    req = HttpRequest(body={
        "id": 1, "codigo": "A1", "tipo": 1, "descricao": "desc", "vaga": "VAGA", "status": 1, "data_fabricacao": "2025-01-01"
    })
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 201
    assert resp.body["msg"] == "ok"

def test_buscar_dispositivo_by_codigo_controller():
    logger.info("Iniciando teste: test_buscar_dispositivo_by_codigo_controller")
    use_case = MagicMock()
    dispositivo = {
        "id": 1,
        "codigo": "A1",
        "tipo": 1,
        "descricao": "desc",
        "vaga": "VAGA",
        "status": 1,
        "data_fabricacao": "2025-01-01",
        "cliente": "ClienteX"
    }
    use_case.buscar_dispositivo_by_codigo.return_value = dispositivo
    controller = BuscarDispositivosByCodigoController(use_case)
    req = HttpRequest(path_params={"codigo": "A1"})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == dispositivo

def test_buscar_dispositivo_by_id_controller():
    logger.info("Iniciando teste: test_buscar_dispositivo_by_id_controller")
    use_case = MagicMock()
    dispositivo = {
        "id": 1,
        "codigo": "A1",
        "tipo": 1,
        "descricao": "desc",
        "vaga": "VAGA",
        "status": 1,
        "data_fabricacao": "2025-01-01",
        "cliente": "ClienteX"
    }
    use_case.buscar_dispositivo_by_id.return_value = dispositivo
    controller = BuscarDispositivoByIdController(use_case)
    req = HttpRequest(path_params={"id": 1})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == dispositivo

def test_excluir_dispositivo_controller():
    logger.info("Iniciando teste: test_excluir_dispositivo_controller")
    use_case = MagicMock()
    use_case.excluir_dispositivo.return_value = {"msg": "deleted"}
    controller = ExcluirDispositivoController(use_case)
    req = HttpRequest(path_params={"codigo": "A1"})
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 204
    assert resp.body["msg"] == "deleted" 

def test_inserir_dispositivo_controller():
    logger.info("Iniciando teste: test_inserir_dispositivo_controller")
    use_case = MagicMock()
    use_case.inserir_dispositivo.return_value = {"msg": "created"}
    controller = InserirDispositivoController(use_case)
    req = HttpRequest(body={
        "codigo": "A1", "tipo": 1, "descricao": "desc", "vaga": "V1", "status": 1, "data_fabricacao": "2024-01-01", "cliente": "C1"
    })
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 201
    assert resp.body["msg"] == "created" 

def test_listar_dispositivo_controller():
    logger.info("Iniciando teste: test_listar_dispositivo_controller")
    use_case = MagicMock()
    dispositivos = [
        {
            "id": 1,
            "codigo": "A1",
            "tipo": 1,
            "descricao": "desc1",
            "vaga": "VAGA1",
            "status": 1,
            "data_fabricacao": "2025-01-01",
            "cliente": "ClienteX"
        },
        {
            "id": 2,
            "codigo": "A2",
            "tipo": 2,
            "descricao": "desc2",
            "vaga": "VAGA2",
            "status": 0,
            "data_fabricacao": "2025-01-02",
            "cliente": "ClienteY"
        },
        {
            "id": 3,
            "codigo": "A3",
            "tipo": 3,
            "descricao": "desc3",
            "vaga": "VAGA3",
            "status": 1,
            "data_fabricacao": "2025-01-03",
            "cliente": "ClienteZ"
        }
    ]
    use_case.listar_dispositivos.return_value = dispositivos
    controller = ListarDispositivoController(use_case)
    req = HttpRequest()
    resp = controller.handle(req)
    logger.info(f"Resposta: {resp}")
    assert resp.status_code == 200
    assert resp.body == dispositivos
    assert len(resp.body) == 3
    for i, dispositivo in enumerate(dispositivos):
        assert resp.body[i] == dispositivo

def test_verificar_status_dispositivo_controller():
    logger.info("Iniciando teste: test_verificar_status_dispositivo_controller")
    use_case = MagicMock()
    
    use_case.return_value = {"codigo": "A1", "status": 1}
    controller = VerificarStatusDispositivoController(use_case)
    req = HttpRequest(query_params={"codigo": "A1"})
    resp = controller.handle(req)
    logger.info(f"Resposta status=1: {resp}")
    assert resp.status_code == 200
    assert resp.body == {"codigo": "A1", "status": 1}

    use_case.return_value = {"codigo": "A2", "status": 0}
    req = HttpRequest(query_params={"codigo": "A2"})
    resp = controller.handle(req)
    logger.info(f"Resposta status=0: {resp}")
    assert resp.status_code == 200
    assert resp.body == {"codigo": "A2", "status": 0}