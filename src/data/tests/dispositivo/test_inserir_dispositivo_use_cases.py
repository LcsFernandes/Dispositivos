import pytest
import logging
from datetime import date, timedelta
from src.data.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivoRepository:
    def __init__(self, vaga_existente=None):
        self.adicionado = False
        self.args = None
        self.vaga_existente = vaga_existente

    def adicionar_dispositivo(self, codigo, tipo, descricao, vaga, status, data_fabricacao, cliente):
        logger.info("Fake adicionar_dispositivo chamado")
        self.adicionado = True
        self.args = (codigo, tipo, descricao, vaga, status, data_fabricacao, cliente)

    def get_vaga_by_identificacao(self, vaga):
        logger.info(f"Fake get_vaga_by_identificacao chamado com vaga: {vaga}")
        return self.vaga_existente if self.vaga_existente == vaga else None

def test_inserir_dispositivo_sucesso():
    logger.info("Iniciando teste: test_inserir_dispositivo_sucesso")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    use_case.inserir_dispositivo(
        codigo="ABC123",
        tipo=1,
        descricao="Sensor de temperatura",
        vaga="A10",
        status=1,
        data_fabricacao=date(2024, 1, 1),
        cliente="ClienteX"
    )
    logger.info(f"Dispositivo inserido: {repo.args}")
    assert repo.adicionado is True
    assert repo.args[0] == "ABC123"
    assert repo.args[1] == 1
    assert repo.args[2] == "Sensor de temperatura"
    assert repo.args[3] == "A10"
    assert repo.args[4] == 1
    assert repo.args[5] == date(2024, 1, 1)
    assert repo.args[6] == "ClienteX"

def test_inserir_dispositivo_codigo_vazio():
    logger.info("Iniciando teste: test_inserir_dispositivo_codigo_vazio")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_codigo("")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "O codigo é obrigatorio para inserir o dispositivo" in str(exc.value)

def test_inserir_dispositivo_tipo_invalido():
    logger.info("Iniciando teste: test_inserir_dispositivo_tipo_invalido")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_tipo("sensor")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "O tipo deve ser integer" in str(exc.value)

def test_inserir_dispositivo_tipo_vazio():
    logger.info("Iniciando teste: test_inserir_dispositivo_tipo_vazio")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_tipo(None)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "O tipo é um parametro obrigatorio" in str(exc.value)

def test_inserir_dispositivo_descricao_vazia():
    logger.info("Iniciando teste: test_inserir_dispositivo_descricao_vazia")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_descricao(" ")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A descrição é obrigatória" in str(exc.value)

def test_inserir_dispositivo_vaga_none():
    logger.info("Iniciando teste: test_inserir_dispositivo_vaga_none")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_vaga(None)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A vaga é obrigatória" in str(exc.value)

def test_inserir_dispositivo_vaga_curta():
    logger.info("Iniciando teste: test_inserir_dispositivo_vaga_curta")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_vaga("A")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "Nome inválido para vaga" in str(exc.value)

def test_inserir_dispositivo_vaga_ja_cadastrada():
    logger.info("Iniciando teste: test_inserir_dispositivo_vaga_ja_cadastrada")
    repo = FakeDispositivoRepository(vaga_existente="A10")
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_vaga("A10")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A vaga A10 já esta cadastrada" in str(exc.value)

def test_inserir_dispositivo_status_invalido():
    logger.info("Iniciando teste: test_inserir_dispositivo_status_invalido")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_status(3)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "Status inválido. Valores aceitos: 1 = 'ativo' ou 0 = 'inativo'" in str(exc.value)

def test_inserir_dispositivo_status_vazio():
    logger.info("Iniciando teste: test_inserir_dispositivo_status_vazio")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_status(None)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "O status é obrigatório" in str(exc.value)

def test_inserir_dispositivo_data_fabricacao_vazia():
    logger.info("Iniciando teste: test_inserir_dispositivo_data_fabricacao_vazia")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_data_fabricacao(None)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A data de fabricação é obrigatória" in str(exc.value)

def test_inserir_dispositivo_data_fabricacao_tipo_errado():
    logger.info("Iniciando teste: test_inserir_dispositivo_data_fabricacao_tipo_errado")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_data_fabricacao("2024-01-01")
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A data de fabricação deve ser uma data válida" in str(exc.value)

def test_inserir_dispositivo_data_fabricacao_futura():
    logger.info("Iniciando teste: test_inserir_dispositivo_data_fabricacao_futura")
    repo = FakeDispositivoRepository()
    use_case = InserirDispositivo(repo)
    data_futura = date.today() + timedelta(days=1)
    with pytest.raises(Exception) as exc:
        use_case._InserirDispositivo__valida_data_fabricacao(data_futura)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "A data de fabricação Não pode ser maior do que a data atual" in str(exc.value)