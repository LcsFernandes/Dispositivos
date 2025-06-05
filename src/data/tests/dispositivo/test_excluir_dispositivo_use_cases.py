import pytest
import logging
from src.data.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivoRepository:
    def __init__(self, dispositivo=None):
        self.dispositivo = dispositivo
        self.excluido = False
        self.codigo_excluido = None

    def get_dispositivo(self, codigo):
        logger.info(f"Fake get_dispositivo chamado com codigo: {codigo}")
        return self.dispositivo if self.dispositivo and self.dispositivo.codigo == codigo else None

    def excluir_dispositivo(self, codigo):
        logger.info(f"Fake excluir_dispositivo chamado com codigo: {codigo}")
        self.excluido = True
        self.codigo_excluido = codigo

class FakeDispositivo:
    def __init__(self, codigo):
        self.codigo = codigo

def test_excluir_dispositivo_sucesso():
    logger.info("Iniciando teste: test_excluir_dispositivo_sucesso")
    dispositivo = FakeDispositivo("ABC123")
    repo = FakeDispositivoRepository(dispositivo)
    use_case = ExcluirDispositivo(repo)
    use_case.excluir_dispositivo("ABC123")
    assert repo.excluido is True
    assert repo.codigo_excluido == "ABC123"
    logger.info("Dispositivo excluído com sucesso.")

def test_excluir_dispositivo_codigo_vazio():
    logger.info("Iniciando teste: test_excluir_dispositivo_codigo_vazio")
    repo = FakeDispositivoRepository()
    use_case = ExcluirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case.excluir_dispositivo("")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "codigo do dispositivo é obrigatorio" in str(exc.value)

def test_excluir_dispositivo_nao_encontrado():
    logger.info("Iniciando teste: test_excluir_dispositivo_nao_encontrado")
    repo = FakeDispositivoRepository(None)
    use_case = ExcluirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case.excluir_dispositivo("XYZ999")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "Dispositivo XYZ999 nao encontrado" in str(exc.value)
