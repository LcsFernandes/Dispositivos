import pytest
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeMovimentacao:
    def __init__(self, id, id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo):
        self.id = id
        self.id_dispositivo = id_dispositivo
        self.local_origem = local_origem
        self.local_destino = local_destino
        self.data_movimentacao = data_movimentacao
        self.usuario_id = usuario_id
        self.tipo = tipo

class FakeMovimentacaoRepository:
    def __init__(self, movimentacao=None):
        self.movimentacao = movimentacao
        self.called_with = None

    def buscar_movimentacao(self, id_dispositivo):
        logger.info(f"Fake buscar_movimentacao chamado com id_dispositivo: {id_dispositivo}")
        self.called_with = id_dispositivo
        return self.movimentacao

class BuscarMovimentacaoUseCase:
    def __init__(self, movimentacao_repository):
        self.__movimentacao_repository = movimentacao_repository

    def buscar_movimentacao(self, id_dispositivo: int):
        self.__valida_id(id_dispositivo)
        movimentacao = self.__movimentacao_repository.buscar_movimentacao(id_dispositivo)
        if movimentacao:
            response = self.__formatar_resposta(movimentacao)
            return response
        return None

    @classmethod
    def __valida_id(cls, id_dispositivo: int) -> None:
        if not id_dispositivo:
            raise Exception("id da movimentacao é um campo obrigatorio")
        if not isinstance(id_dispositivo, int) or id_dispositivo < 0:
            raise Exception("o id é um campo obrigatorio inteiro positivo")

    @classmethod
    def __formatar_resposta(cls, movimentacao: FakeMovimentacao):
        return {
            "type": "Movimentacao",
            "data": {
                "id": movimentacao.id,
                "id_dispositivo": movimentacao.id_dispositivo,
                "local_origem": movimentacao.local_origem,
                "local_destino": movimentacao.local_destino,
                "data_movimentacao": movimentacao.data_movimentacao,
                "usuario_id": movimentacao.usuario_id,
                "tipo": movimentacao.tipo
            }
        }

def test_buscar_movimentacao_sucesso():
    logger.info("Iniciando teste: test_buscar_movimentacao_sucesso")
    movimentacao = FakeMovimentacao(
        id=1,
        id_dispositivo=10,
        local_origem=100,
        local_destino=150,
        data_movimentacao=datetime(2024, 6, 5, 10, 0, 0),
        usuario_id=100,
        tipo=1
    )
    repo = FakeMovimentacaoRepository(movimentacao)
    use_case = BuscarMovimentacaoUseCase(repo)
    result = use_case.buscar_movimentacao(10)
    logger.info(f"Resultado: {result}")
    assert result["type"] == "Movimentacao"
    assert result["data"]["id"] == 1
    assert result["data"]["id_dispositivo"] == 10
    assert result["data"]["local_origem"] == 100
    assert result["data"]["local_destino"] == 150
    assert result["data"]["data_movimentacao"] == datetime(2024, 6, 5, 10, 0, 0)
    assert result["data"]["usuario_id"] == 100
    assert result["data"]["tipo"] == 1

def test_buscar_movimentacao_id_vazio():
    logger.info("Iniciando teste: test_buscar_movimentacao_id_vazio")
    repo = FakeMovimentacaoRepository()
    use_case = BuscarMovimentacaoUseCase(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_movimentacao(None)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "id da movimentacao é um campo obrigatorio" in str(exc.value)

def test_buscar_movimentacao_id_negativo():
    logger.info("Iniciando teste: test_buscar_movimentacao_id_negativo")
    repo = FakeMovimentacaoRepository()
    use_case = BuscarMovimentacaoUseCase(repo)
    with pytest.raises(Exception) as exc:
        use_case.buscar_movimentacao(-1)
    logger.info(f"Exceção capturada: {exc.value}")
    assert "o id é um campo obrigatorio inteiro positivo" in str(exc.value)

def test_buscar_movimentacao_nao_encontrada():
    logger.info("Iniciando teste: test_buscar_movimentacao_nao_encontrada")
    repo = FakeMovimentacaoRepository(None)
    use_case = BuscarMovimentacaoUseCase(repo)
    result = use_case.buscar_movimentacao(99)
    logger.info(f"Resultado: {result}")
    assert result is None