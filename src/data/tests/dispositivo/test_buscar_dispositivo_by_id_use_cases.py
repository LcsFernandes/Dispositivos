import pytest
from src.data.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivoById
from src.domain.entities.dispositivo import Dispositivo
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivoRepository:
    def __init__(self, dispositivo=None):
        self.dispositivo = dispositivo
        self.called_with = None

    def get_dispositivo_by_id(self, id: int):
        self.called_with_id = id
        return self.dispositivo if self.dispositivo and self.dispositivo.id == id else None


def make_dispositivo():
    return Dispositivo(
        id=1,
        codigo="ABC123",
        tipo=2,
        descricao="Sensor de temperatura",
        vaga="A1",
        status=1,
        data_fabricacao="2025-01-01"
    )

def test_buscar_dispositivo_by_id_sucesso():
    logger.info("Iniciando teste: test_buscar_dispositivo_by_id_sucesso")
    dispositivo = make_dispositivo()
    repo = FakeDispositivoRepository(dispositivo)
    use_case = BuscarDispositivoById(repo)
    result = use_case.buscar_dispositivo_by_id(1)
    logger.info(f"Resultado: {result}")
    assert result["type"] == "Dispositivos"
    assert result["data"]["id"] == dispositivo.id
    assert result["data"]["codigo"] == dispositivo.codigo
    assert result["data"]["tipo"] == dispositivo.tipo
    assert result["data"]["descricao"] == dispositivo.descricao
    assert result["data"]["vaga"] == dispositivo.vaga
    assert result["data"]["status"] == dispositivo.status
    assert result["data"]["data_fabricacao"] == dispositivo.data_fabricacao


def test_buscar_dispositivo_by_id_invalido():
    logger.info("Iniciando teste: test_buscar_dispositivo_by_id_invalido")
    repo = FakeDispositivoRepository()
    use_case = BuscarDispositivoById(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_dispositivo_by_id(-1)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "id do dispositivo é um parametro obrigatório inteiro positivo" in str(exc.value)

def test_buscar_dispositivo_by_id_nao_encontrado():
    logger.info("Iniciando teste: test_buscar_dispositivo_by_id_nao_encontrado")
    repo = FakeDispositivoRepository(None)
    use_case = BuscarDispositivoById(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_dispositivo_by_id(999)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "Dispositivo com id 999 não encontrado." in str(exc.value)