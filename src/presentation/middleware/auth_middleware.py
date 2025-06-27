from fastapi import Request
from fastapi.responses import JSONResponse
from src.presentation.http_types.http_response import HttpResponse
from src.errors.error_handle import handle_errors
from src.domain.services.token_service import TokenService
from src.errors.types import HttpUnauthorizedError
from typing import Callable

class AuthMiddleware:
    def __init__(self, token_service: TokenService, exclude_routes: list[str] = None):
        self.__token_service = token_service
        self.exclude_routes = exclude_routes or []

    async def __call__(self, request: Request, call_next: Callable) -> JSONResponse:
        if request.url.path in self.exclude_routes:
            return await call_next(request)

        try:
            token = self.__extrai_token(request)
            payload = self.__token_service.verificar_token(token)
            
            
            request.state.usuario_atual = payload.get("user_id")
            
            return await call_next(request)
            
        except Exception as exception:
            http_response: HttpResponse = handle_errors(exception)

            return JSONResponse(
                content=http_response.body,
                status_code=http_response.status_code
            )
    @staticmethod
    def __extrai_token(request: Request) -> str:
        authorization = request.headers.get("Authorization")
        
        if not authorization:
            raise HttpUnauthorizedError("Token não encontrado")
            
        token_parts = authorization.split()
        
        if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
            raise HttpUnauthorizedError("Formato de token invalido")
            
        return token_parts[1]