from src.domain.services.token_service import TokenService as TokenServiceInterface
from jose import jwt
from datetime import datetime, timedelta, timezone
from src.config.jwt_config import ConfiguracaoJWT
from src.errors.types import HttpUnauthorizedError

class TokenService(TokenServiceInterface):

    def criar_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ConfiguracaoJWT.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        token_jwt = jwt.encode(
            to_encode,
            ConfiguracaoJWT.SECRET_KEY,
            algorithm=ConfiguracaoJWT.ALGORITHM
        )
        return token_jwt

    def verificar_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                ConfiguracaoJWT.SECRET_KEY,
                algorithms=[ConfiguracaoJWT.ALGORITHM]
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise HttpUnauthorizedError("Token expirado")
        except jwt.JWTClaimsError:
            raise HttpUnauthorizedError("Token invalido ou mal formado")
        except jwt.JWTError:
            raise HttpUnauthorizedError("Erro ao decodificar token")
        