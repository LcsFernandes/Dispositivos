from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.listar_dispositivos import ListarDispositivos as ListarDispositivosInterface
from typing import Dict, List

class ListarDispositivo(ListarDispositivosInterface):
   
    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def listar_dispositivo(self) -> List[Dispositivo]:
        
        dispositivos = self.__dispositivo_repository.get_all_dispositivos()
        
        if dispositivos:
            response = self.__formatar_resposta(dispositivos)
            return response
        
        return []
   
    @classmethod
    def __formatar_resposta(cls, dispositivos: Dispositivo) -> Dict:
        lista_dispositivos = []
        for dispositivo in dispositivos:
            lista_dispositivos.append({
                    "id": dispositivo.id,
                    "nome": dispositivo.codigo,
                    "tipo": dispositivo.tipo,
                    "descricao": dispositivo.descricao,
                    "vaga": dispositivo.vaga,
                    "status": dispositivo.status,
                    "data_fabricacao": dispositivo.data_fabricacao
                })
             
        return {
            "type": "Dispositivos",
            "data": lista_dispositivos
        }