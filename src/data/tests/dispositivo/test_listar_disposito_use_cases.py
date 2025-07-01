import pytest
import logging
from src.data.use_cases.dispositivo.listar_dispositivo import ListarDispositivo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeDispositivo:
    def __init__(
        self,
        id,
        codigo,
        tipo,
        descricao,
        vaga,
        status,
        data_fabricacao
    ):
        self.id = id
        self.codigo = codigo
        self.tipo = tipo
        self.descricao = descricao
        self.vaga = vaga
        self.status = status
        self.data_fabricacao = data_fabricacao

class FakeDispositivoRepository:
    def __init__(self, dispositivos=None):
        self.dispositivos = dispositivos or []

    def get_all_dispositivos(self):
        logger.info("Fake get_all_dispositivos chamado")
        return self.dispositivos

def test_listar_dispositivo_cinco_dispositivos():
    logger.info("Iniciando teste: test_listar_dispositivo_cinco_dispositivos")
    dispositivos = [
        FakeDispositivo(
            id=1,
            codigo="B00001",
            tipo=1,
            descricao="Sensor de temperatura",
            vaga="A1",
            status=1,
            data_fabricacao="2025-01-01"
        ),
        FakeDispositivo(
            id=2,
            codigo="B00002",
            tipo=2,
            descricao="Atuador de pressão",
            vaga="B2",
            status=0,
            data_fabricacao="2025-01-02"
        ),
        FakeDispositivo(
            id=3,
            codigo="B00003",
            tipo=3,
            descricao="Controlador de acesso",
            vaga="C3",
            status=1,
            data_fabricacao="2025-01-03"
        ),
        FakeDispositivo(
            id=4,
            codigo="B00004",
            tipo=4,
            descricao="Gateway de rede",
            vaga="D4",
            status=2,
            data_fabricacao="2025-01-04"
        ),
        FakeDispositivo(
            id=5,
            codigo="B00005",
            tipo=5,
            descricao="Repetidor de sinal",
            vaga="E5",
            status=1,
            data_fabricacao="2025-01-05"
        ),
    ]
    repo = FakeDispositivoRepository(dispositivos)
    use_case = ListarDispositivo(repo)
    result = use_case.listar_dispositivo()
    logger.info(f"Resultado: {result}")
    assert result["type"] == "Dispositivos"
    assert len(result["data"]) == 5
    
    esperado = [
        {
            "id": 1,
            "nome": "B00001",
            "tipo": 1,
            "descricao": "Sensor de temperatura",
            "vaga": "A1",
            "status": 1,
            "data_fabricacao": "2025-01-01"
        },
        {
            "id": 2,
            "nome": "B00002",
            "tipo": 2,
            "descricao": "Atuador de pressão",
            "vaga": "B2",
            "status": 0,
            "data_fabricacao": "2025-01-02"
        },
        {
            "id": 3,
            "nome": "B00003",
            "tipo": 3,
            "descricao": "Controlador de acesso",
            "vaga": "C3",
            "status": 1,
            "data_fabricacao": "2025-01-03"
        },
        {
            "id": 4,
            "nome": "B00004",
            "tipo": 4,
            "descricao": "Gateway de rede",
            "vaga": "D4",
            "status": 2,
            "data_fabricacao": "2025-01-04"
        },
        {
            "id": 5,
            "nome": "B00005",
            "tipo": 5,
            "descricao": "Repetidor de sinal",
            "vaga": "E5",
            "status": 1,
            "data_fabricacao": "2025-01-05"
        },
    ]

    for i, dispositivo in enumerate(result["data"]):
        for campo in esperado[i]:
            assert dispositivo[campo] == esperado[i][campo], f"Falha no campo {campo} do dispositivo {i+1}"
