import pytest
import logging
from src.data.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo
from types import SimpleNamespace

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivo:
    def __init__(self, id, codigo, status):
        self.id = id
        self.codigo = codigo
        self.status = status

class FakeDispositivoRepository:
    def __init__(self, dispositivos=None):
        self.dispositivos = dispositivos or []

    def get_dispositivo_by_codigo(self, codigo):
        logger.info(f"Fake get_dispositivo_by_codigo chamado para {codigo}")
        for d in self.dispositivos:
            if d.codigo == codigo:
                return d
        return None

    def verificar_status_dispositivo(self, codigo):
        logger.info(f"Fake verificar_status_dispositivo chamado para {codigo}")
        dispositivo = self.get_dispositivo_by_codigo(codigo)
        if dispositivo:
            return {"codigo": codigo, "status": dispositivo.status}
        return None

def test_verificar_status_dispositivo_sucesso():
    logger.info("Iniciando teste: test_verificar_status_dispositivo_sucesso")
    dispositivos = [
        FakeDispositivo(id=1, codigo="B00001", status=1),
        FakeDispositivo(id=2, codigo="B00002", status=0),
    ]
    repo = FakeDispositivoRepository(dispositivos)
    use_case = VerificarStatusDispositivo(repo)
    dto = SimpleNamespace(codigo="B00001")
    result = use_case.verificar_status_dispositivo(dto)
    logger.info(f"Resultado: {result}")
    assert result == {"codigo": "B00001", "status": 1}

def test_verificar_status_dispositivo_nao_encontrado():
    logger.info("Iniciando teste: test_verificar_status_dispositivo_nao_encontrado")
    repo = FakeDispositivoRepository([])
    use_case = VerificarStatusDispositivo(repo)
    dto = SimpleNamespace(codigo="B99999")
    with pytest.raises(Exception) as excinfo:
        use_case.verificar_status_dispositivo(dto)
    assert "Dispositivo nao encontrado" in str(excinfo.value)

def test_verificar_status_dispositivo_codigo_invalido():
    logger.info("Iniciando teste: test_verificar_status_dispositivo_codigo_invalido")
    repo = FakeDispositivoRepository([])
    use_case = VerificarStatusDispositivo(repo)
    dto = SimpleNamespace(codigo=None)
    with pytest.raises(Exception) as excinfo:
        use_case.verificar_status_dispositivo(dto)
    assert "codigo do dispositivo é um campo tipo string obrigatorio" in str(excinfo.value)