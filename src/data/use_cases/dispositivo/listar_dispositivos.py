from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.listar_dispositivos import ListarDispositivos as ListarDispositivosInterface
from typing import Dict, List
from collections import OrderedDict

class ListarDispositivo(ListarDispositivosInterface):
   
    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def listar_dispositivos(self) -> List[Dispositivo]:
        
        dispositivos = self.__dispositivo_repository.get_all_dispositivos()
    
        response = self.__formatar_resposta(dispositivos)

        return response
        
        
   
    @staticmethod
    def __formatar_resposta(dispositivos: List[Dispositivo]) -> Dict:
        lista_dispositivos = []
        for dispositivo in dispositivos or []:
            lista_dispositivos.append({
                "id": dispositivo.id,
                "codigo": dispositivo.codigo,
                "tipo": dispositivo.tipo,
                "descricao": dispositivo.descricao,
                "status": dispositivo.status,
                "data_fabricacao": dispositivo.data_fabricacao.strftime('%Y-%m-%d'),
                "cliente": dispositivo.cliente                
            })
        return {
            "type": "Dispositivos",
            "data": lista_dispositivos
        }