import pytest
import logging
from src.data.use_cases.vaga.alterar_vaga import AlterarVaga

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeVagaRepository:
    def __init__(self):
        self.atualizado = False
        self.args = None

    def atualizar_vaga(self, id, deposito_id, identificacao):
        logger.info(f"Fake atualizar_vaga chamado: id={id}, deposito_id={deposito_id}, identificacao={identificacao}")
        self.atualizado = True
        self.args = (id, deposito_id, identificacao)

def test_alterar_vaga_sucesso():
    logger.info("Iniciando teste: test_alterar_vaga_sucesso")
    repo = FakeVagaRepository()
    use_case = AlterarVaga(repo)
    use_case.alterar_vaga(id=1, deposito_id=74, identificacao="A12")
    assert repo.atualizado is True
    assert repo.args == (1, 74, "A12")

@pytest.mark.parametrize("id", [None, "abc", -1, 0])
def test_alterar_vaga_id_invalido(id):
    repo = FakeVagaRepository()
    use_case = AlterarVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.alterar_vaga(id=id, deposito_id=74, identificacao="A12")
    assert "o id é um campo obrigatorio inteiro positivo" in str(excinfo.value)

@pytest.mark.parametrize("deposito_id", [None, "abc", -1, 0])
def test_alterar_vaga_deposito_id_invalido(deposito_id):
    repo = FakeVagaRepository()
    use_case = AlterarVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.alterar_vaga(id=1, deposito_id=deposito_id, identificacao="A12")
    assert "o deposito_id é um campo obrigatorio inteiro positivo" in str(excinfo.value)

def test_alterar_vaga_deposito_id_errado():
    repo = FakeVagaRepository()
    use_case = AlterarVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.alterar_vaga(id=1, deposito_id=99, identificacao="A12")
    assert "deposito_id informado nao pertence ao armazem de dispositivos" in str(excinfo.value)

@pytest.mark.parametrize("identificacao", [None, "", "A"])
def test_alterar_vaga_identificacao_invalida(identificacao):
    repo = FakeVagaRepository()
    use_case = AlterarVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.alterar_vaga(id=1, deposito_id=74, identificacao=identificacao)
    assert "identificacao da vaga é um campo obrigatorio" in str(excinfo.value) or \
           "Nome de identificacao para vaga invalido" in str(excinfo.value)