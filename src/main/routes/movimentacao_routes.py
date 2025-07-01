from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.movimentacao.buscar_movimentacao_composer import buscar_movimentacao_composer
from src.main.composers.movimentacao.registar_movimentacao_composer import registrar_movimentacao_composer
from src.main.composers.movimentacao.listar_movimentacao_composer import listar_movimentacao_composer

from src.main.adapters.dto.movimentacao_dto import InserirMovimentacaoDTO

from src.errors.error_handle import handle_errors

router = APIRouter(prefix="/movimentacao", tags=["Movimentacao"])


@router.get("/list")
async def listar_movimentacoes(request: Request, page: int = 1, page_size: int = 10):
    http_response = None
    
    try:
        http_response = await request_adapter(request, listar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.post("")
async def registrar_movimentacao(request: Request, body: InserirMovimentacaoDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, registrar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.get("/find/{codigo_dispositivo}", summary="Buscar o Historico de Movimentacao de um Dispositivo Especifico")
async def buscar_movimentacao(request: Request, codigo_dispositivo: str):
    http_response = None
    
    try:
        request.scope["path_params"] = {"codigo_dispositivo": codigo_dispositivo}
        http_response = await request_adapter(request, buscar_movimentacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)