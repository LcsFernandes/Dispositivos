from src.errors.types import ConfigurationError
from dotenv import load_dotenv
import os

load_dotenv()

class ConfiguracaoJWT:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    @classmethod
    def carregar_configuracoes(cls):
        if not cls.SECRET_KEY:
            raise ConfigurationError("SECRET_KEY não configurada")
        if not cls.ALGORITHM:
            raise ConfigurationError("ALGORITHM não configurado")
        if not cls.ACCESS_TOKEN_EXPIRE_MINUTES:
            raise ConfigurationError("ACCESS_TOKEN_EXPIRE_MINUTES não configurada")


ConfiguracaoJWT.carregar_configuracoes()