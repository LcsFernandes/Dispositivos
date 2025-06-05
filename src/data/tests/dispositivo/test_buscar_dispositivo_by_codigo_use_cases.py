import pytest
from src.data.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivoByCodigo
from src.domain.entities.dispositivo import Dispositivo
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivoRepository:
    def __init__(self, dispositivo=None):
        self.dispositivo = dispositivo
        self.called_with = None

    def get_dispositivo_by_codigo(self, codigo):
        self.called_with = codigo
        return self.dispositivo

def make_dispositivo():
    return Dispositivo(
        id=1,
        codigo="ABC123",
        tipo="Sensor",
        descricao="Sensor de temperatura",
        vaga="A1",
        status=1,
        data_fabricacao="2025-01-01"
    )

def test_buscar_dispositivo_sucesso():
    logger.info("Iniciando teste: test_buscar_dispositivo_sucesso")
    dispositivo = make_dispositivo()
    repo = FakeDispositivoRepository(dispositivo)
    use_case = BuscarDispositivoByCodigo(repo)
    result = use_case.buscar_dispositivo_by_codigo("ABC123")
    logger.info(f"Resultado: {result}")
    assert result["type"] == "Dispositivos"
    assert result["data"]["id"] == dispositivo.id
    assert result["data"]["codigo"] == dispositivo.codigo
    assert result["data"]["tipo"] == dispositivo.tipo
    assert result["data"]["descricao"] == dispositivo.descricao
    assert result["data"]["vaga"] == dispositivo.vaga
    assert result["data"]["status"] == dispositivo.status
    assert result["data"]["data_fabricacao"] == dispositivo.data_fabricacao



def test_buscar_dispositivo_codigo_vazio():
    logger.info("Iniciando teste: test_buscar_dispositivo_codigo_vazio")
    repo = FakeDispositivoRepository()
    use_case = BuscarDispositivoByCodigo(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_dispositivo_by_codigo("")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "codigo do dispositivo é obrigatorio" in str(exc.value)

def test_buscar_dispositivo_nao_encontrado():
    logger.info("Iniciando teste: test_buscar_dispositivo_nao_encontrado")
    repo = FakeDispositivoRepository(None)
    use_case = BuscarDispositivoByCodigo(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_dispositivo_by_codigo("XYZ999")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "Dispositivo com código XYZ999 não encontrado." in str(exc.value)