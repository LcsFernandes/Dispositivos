from src.domain.use_cases.usuario.criar_usuario import CriarUsuario as CriarUsuarioInterface
from src.data.interfaces.usuario_repository import UsuarioRepositoryInterface
from src.domain.services.senha_service import SenhaServiceInterface
from src.errors.types import HttpBadRequestError
from src.data.dto.usuario.criar_usuario_dto import CriarUsuarioDTO
from typing import Dict

class CriarUsuario(CriarUsuarioInterface):
    def __init__(self, usuario_repository: UsuarioRepositoryInterface, senha_service: SenhaServiceInterface):
        self.__usuario_repository = usuario_repository
        self.__senha_service = senha_service

    def criar_usuario(self, dto: CriarUsuarioDTO):
        self.__valida_nome(dto.nome)
        self.__valida_re(dto.re)
        self.__valida_se_usuario_existe(dto.re)
        self.__valida_senha(dto.senha)
        senha_hash = self.hash_senha(dto.senha)

        self.__usuario_repository.criar_usuario(dto.re, dto.nome, senha_hash)


    @staticmethod
    def __valida_nome(nome: str):
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise HttpBadRequestError("Nome deve ser uma string valida")

    @staticmethod
    def __valida_re(re: int):
        if not isinstance(re, int) or len(str(re)) > 6:
            raise HttpBadRequestError("RE deve ser um inteiro valido com ate 6 caracteres.")
        
    def __valida_se_usuario_existe(self, re: str):
        usuario = self.__usuario_repository.get_usuario(re)

        if usuario:
            raise HttpBadRequestError(f"Usuario {usuario.re} ja esta cadastrado.")
    
    @staticmethod
    def __valida_senha(senha: str):
        if not isinstance(senha, str) or len(senha.strip()) < 6:
            raise HttpBadRequestError("Senha deve ser uma string valida com pelo menos 6 caracteres.")


    def hash_senha(self, senha: str):
        return self.__senha_service.hash_senha(senha)
         

    
    
    
        
