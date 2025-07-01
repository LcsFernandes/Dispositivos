from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.listar_dispositivos import ListarDispositivos as ListarDispositivosInterface
from typing import Dict, List
from src.data.dto.dispositivo.listar_dispositivo_dto import ListarDispositivoDTO
from src.errors.types import HttpBadRequestError
from src.infra.logger.logger import get_logger

class ListarDispositivo(ListarDispositivosInterface):
   
    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def listar_dispositivos(self, dto: ListarDispositivoDTO) -> List[Dispositivo]:
        self.__validar_page(dto.page)
        self.__validar_page_size(dto.page_size)
        
        page, page_size = self.__calcular_paginacao(dto.page, dto.page_size)
        
        dispositivos = self.__dispositivo_repository.get_all_dispositivos(page, page_size)

        if not dispositivos:
            return None
        
        response = self.__formatar_resposta(dispositivos)

        return response
        
    def __calcular_paginacao(self, page: int, page_size: int):
        
        if page == 1:
            page = 0
        else:
            page = page - 1
            page = (page * page_size)

        return page, page_size
        
    @staticmethod
    def __validar_page(page: int):
        if not isinstance(page, int) or page <= 0:
            raise HttpBadRequestError("page deve ser um numero inteiro positivo")
    
    @staticmethod
    def __validar_page_size(page_size: int):
        if not isinstance(page_size, int) or page_size <= 0:
            raise HttpBadRequestError("page_size deve ser um numero inteiro positivo")

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