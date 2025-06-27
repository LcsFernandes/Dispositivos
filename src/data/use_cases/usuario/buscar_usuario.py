from src.domain.use_cases.usuario.buscar_usuario import BuscarUsuario as BuscarUsuarioInterface
from src.data.interfaces.usuario_repository import UsuarioRepositoryInterface
from src.errors.types import HttpBadRequestError
from src.data.dto.usuario.buscar_usuario_dto import BuscarUsuarioDTO
from typing import Dict


class BuscarUsuario(BuscarUsuarioInterface):
    def __init__(self, usuario_repository: UsuarioRepositoryInterface):
        self.__usuario_repository = usuario_repository

    def buscar_usuario(self, dto: BuscarUsuarioDTO):
        self.__valida_re(dto.re)

        usuario = self.__usuario_repository.get_usuario(dto.re)

        if usuario:
            return self.__formatar_resposta(usuario.id, usuario.re, usuario.nome)
        
        return None

    @staticmethod
    def __valida_re(re: int):
        if not isinstance(re, int) or len(str(re)) > 6:
            raise HttpBadRequestError("RE deve ser um inteiro valido com ate 6 caracteres.")
    
    @staticmethod
    def __formatar_resposta(id: int, re: int, nome: str) -> Dict:
        return {
            "type": "Usuario",
            "data": {
                "id": id,
                "re": re,
                "nome": nome
            }
        }

    
    
    
        
