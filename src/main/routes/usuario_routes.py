from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.usuario.criar_usuario_composer import criar_usuario_composer
from src.main.composers.usuario.buscar_usuario_composer import buscar_usuario_composer
from src.main.composers.usuario.login_usuario_composer import login_usuario_composer
from src.main.composers.usuario.alterar_senha_usuario_composer import alterar_senha_usuario_composer
from src.main.adapters.dto.usuario_dto import CriarUsuarioDTO, LoginUsuarioDTO, AlterarSenhaUsuarioDTO

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

@router.get("/{re}")
async def buscar_usuario(request: Request, re: int):
    http_response = None
    
    try:
        request.scope["path_params"] = {"re": re}
        http_response = await request_adapter(request, buscar_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.post("/login")
async def login_usuario(request: Request, body: LoginUsuarioDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, login_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.put("")
async def alterar_senha_usuario(request: Request, body: AlterarSenhaUsuarioDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, alterar_senha_usuario_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

