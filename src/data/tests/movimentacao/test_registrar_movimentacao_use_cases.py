import pytest
import logging
from datetime import datetime
from types import SimpleNamespace
from src.data.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeMovimentacaoRepository:
    def __init__(self):
        self.registrado = False
        self.args = None

    def registrar_movimentacao(self, id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo):
        logger.info(f"Fake registrar_movimentacao chamado: id_dispositivo={id_dispositivo}, local_origem={local_origem}, local_destino={local_destino}, data_movimentacao={data_movimentacao}, usuario_id={usuario_id}, tipo={tipo}")
        self.registrado = True
        self.args = (id_dispositivo, local_origem, local_destino, usuario_id, tipo)

class FakeDispositivoRepository:
    def __init__(self, dispositivos=None):
        self.dispositivos = dispositivos or []

    def get_dispositivo_by_id(self, id_dispositivo):
        logger.info(f"Fake get_dispositivo_by_id chamado: id_dispositivo={id_dispositivo}")
        for d in self.dispositivos:
            if d.id == id_dispositivo:
                return d
        return None

class FakeVagaRepository:
    def __init__(self, vagas=None):
        self.vagas = vagas or []

    def get_vaga_by_id(self, id_vaga):
        logger.info(f"Fake get_vaga_by_id chamado: id_vaga={id_vaga}")
        for v in self.vagas:
            if v.id == id_vaga:
                return v
        return None

class FakeDispositivo:
    def __init__(self, id):
        self.id = id

class FakeVaga:
    def __init__(self, id):
        self.id = id

def test_registrar_movimentacao_sucesso():
    logger.info("Iniciando teste: test_registrar_movimentacao_sucesso")
    dispositivo = FakeDispositivo(id=1)
    vaga_origem = FakeVaga(id=10)
    vaga_destino = FakeVaga(id=20)
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([dispositivo])
    repo_vaga = FakeVagaRepository([vaga_origem, vaga_destino])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=1,
        local_origem=10,
        local_destino=20,
        usuario_id=100,
        tipo=1
    )
    use_case.registrar_movimentacao(dto)
    assert repo_mov.registrado is True
    assert repo_mov.args[:4] == (1, 10, 20, 100)
    assert repo_mov.args[4] == 1

def test_registrar_movimentacao_dispositivo_invalido():
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([])
    repo_vaga = FakeVagaRepository([FakeVaga(id=10), FakeVaga(id=20)])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=999,
        local_origem=10,
        local_destino=20,
        usuario_id=100,
        tipo=1
    )
    with pytest.raises(Exception) as excinfo:
        use_case.registrar_movimentacao(dto)
    assert "Dispositivo id 999 nao encontrado" in str(excinfo.value)

@pytest.mark.parametrize("local", [None, -1])
def test_registrar_movimentacao_local_invalido(local):
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([FakeDispositivo(id=1)])
    repo_vaga = FakeVagaRepository([FakeVaga(id=10), FakeVaga(id=20)])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=1,
        local_origem=local,
        local_destino=20,
        usuario_id=100,
        tipo=1
    )
    with pytest.raises(Exception) as excinfo:
        use_case.registrar_movimentacao(dto)
    assert "local é um campo inteiro positivo obrigatório" in str(excinfo.value)

def test_registrar_movimentacao_vaga_nao_encontrada():
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([FakeDispositivo(id=1)])
    repo_vaga = FakeVagaRepository([FakeVaga(id=10)])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=1,
        local_origem=10,
        local_destino=99,
        usuario_id=100,
        tipo=1
    )
    with pytest.raises(Exception) as excinfo:
        use_case.registrar_movimentacao(dto)
    assert "Vaga nao encontrada" in str(excinfo.value)

@pytest.mark.parametrize("usuario_id", [None, "abc", -1, 0])
def test_registrar_movimentacao_usuario_invalido(usuario_id):
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([FakeDispositivo(id=1)])
    repo_vaga = FakeVagaRepository([FakeVaga(id=10), FakeVaga(id=20)])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=1,
        local_origem=10,
        local_destino=20,
        usuario_id=usuario_id,
        tipo=1
    )
    with pytest.raises(Exception) as excinfo:
        use_case.registrar_movimentacao(dto)
    assert "usuario_id é um campo inteiro positivo obrigatório" in str(excinfo.value)

@pytest.mark.parametrize("tipo", [None, "abc", -1, 0])
def test_registrar_movimentacao_tipo_invalido(tipo):
    repo_mov = FakeMovimentacaoRepository()
    repo_disp = FakeDispositivoRepository([FakeDispositivo(id=1)])
    repo_vaga = FakeVagaRepository([FakeVaga(id=10), FakeVaga(id=20)])
    use_case = RegistrarMovimentacao(repo_mov, repo_disp, repo_vaga)
    dto = SimpleNamespace(
        id_dispositivo=1,
        local_origem=10,
        local_destino=20,
        usuario_id=100,
        tipo=tipo
    )
    with pytest.raises(Exception) as excinfo:
        use_case.registrar_movimentacao(dto)
    assert "tipo é um campo inteiro positivo obrigatório" in str(excinfo.value)