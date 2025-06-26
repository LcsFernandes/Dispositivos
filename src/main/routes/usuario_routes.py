from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.usuario.criar_usuario import criar_usuario_composer
from src.main.adapters.dto.usuario_dto import CriarUsuarioDTO

from src.errors.error_handle import handle_errors

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.post("")
async def criar_usuario(request: Request, body: CriarUsuarioDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, criar_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)