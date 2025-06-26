from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.vaga.alterar_vaga_composer import alterar_vaga_composer
from src.main.composers.vaga.buscar_vaga_by_id_composer import buscar_vaga_by_id_composer
from src.main.composers.vaga.buscar_vaga_by_identificacao_composer import buscar_vaga_by_identificacao_composer
from src.main.composers.vaga.inserir_vaga_composer import inserir_vaga_composer
from src.main.composers.vaga.listar_vaga_composer import listar_vaga_composer

from src.main.adapters.dto.vaga_dto import AlterarVagaDTO, InserirVagaDTO

from src.errors.error_handle import handle_errors

router = APIRouter(prefix="/vaga", tags=["Vaga"])


@router.get("/list")
async def listar_vagas(request: Request):
    http_response = None
    
    try:
        http_response = await request_adapter(request, listar_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.post("")
async def inserir_vaga(request: Request, body: InserirVagaDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, inserir_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.put("/{id_vaga}")
async def alterar_vaga(request: Request, id_vaga: int, body: AlterarVagaDTO):
    http_response = None
    
    try:
        request.scope["path_params"] = {"id_vaga": id_vaga}
        http_response = await request_adapter(request, alterar_vaga_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.get("/find_by_id/{id_vaga}")
async def buscar_vaga_by_id(request: Request, id_vaga: int):
    http_response = None
    
    try:
        request.scope["path_params"] = {"id_vaga": id_vaga}
        http_response = await request_adapter(request, buscar_vaga_by_id_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.get("/find_by_identificacao/{identificacao}")
async def buscar_vaga_by_identificacao(request: Request, identificacao: str):
    http_response = None
    
    try:
        request.scope["path_params"] = {"identificacao": identificacao}
        http_response = await request_adapter(request, buscar_vaga_by_identificacao_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)