from src.domain.services.senha_service import SenhaServiceInterface
import bcrypt


class SenhaService(SenhaServiceInterface):
    def hash_senha(self, senha: str) -> str:
        response = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        return response

    def verificar_senha(self, senha: str, hash_armazenado: str) -> bool:
        response = bcrypt.checkpw(senha.encode(), hash_armazenado.encode()) 
        return response