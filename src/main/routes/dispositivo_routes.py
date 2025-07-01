from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter

from src.main.composers.dispositivo.alterar_dispositivo_composer import alterar_dispositivo_composer
from src.main.composers.dispositivo.buscar_dispositivo_by_codigo_composer import buscar_dispositivo_by_codigo_composer
from src.main.composers.dispositivo.buscar_dispositivo_by_id_composer import buscar_dispositivo_by_id_composer
from src.main.composers.dispositivo.excluir_dispositivo_composer import excluir_dispositivo_composer
from src.main.composers.dispositivo.inserir_dispositivo_composer import inserir_dispositivo_composer
from src.main.composers.dispositivo.listar_dispositivo_composer import listar_dispositivo_composer
from src.main.composers.dispositivo.verificar_status_dispositivo_composer import verificar_status_dispositivo_composer
from src.main.composers.dispositivo.buscar_posicao_dispositivo_composer import buscar_posicao_dispositivo_composer


from src.main.adapters.dto.dispositivo_dto import InserirDispositivoDTO, AlterarDispositivoDTO, DispositivoOutputDTO, VerificarStatusDispositivoOutput

from src.errors.error_handle import handle_errors

from typing import List

router = APIRouter(prefix="/dispositivo", tags=["Dispostivo"])

@router.get("/list", response_model = DispositivoOutputDTO)
async def listar_dispositivos(request: Request):
    http_response = None
    
    try:
        http_response = await request_adapter(request, listar_dispositivo_composer())
    except Exception as exception:
        http_response =  handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.post("")
async def inserir_dispositivo(request: Request, body: InserirDispositivoDTO):
    http_response = None
    
    try:
        http_response = await request_adapter(request, inserir_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.put("/{id_dispositivo}")
async def alterar_dispositivo(request: Request, id_dispositivo: int, body: AlterarDispositivoDTO):
    http_response = None
    
    try:
        request.scope["path_params"] = {"id_dispositivo": id_dispositivo}
        http_response = await request_adapter(request, alterar_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.delete("/{codigo_dispositivo}")
async def excluir_dispositivo(request: Request, codigo_dispositivo: str):
    http_response = None
    
    try:
        request.scope["path_params"] = {"codigo_dispositivo": codigo_dispositivo}
        http_response =  await request_adapter(request, excluir_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.get("/find_by_id/{id_dispositivo}", response_model = DispositivoOutputDTO)
async def buscar_dispositivo_by_id(id_dispositivo: int, request: Request):
    http_response = None
    
    try:
        request.scope["path_params"] = {"id_dispositivo": id_dispositivo}
        http_response = await request_adapter(request, buscar_dispositivo_by_id_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@router.get("/find_by_codigo/{codigo_dispositivo}", response_model = DispositivoOutputDTO)
async def buscar_dispositivo_by_codigo(codigo_dispositivo: str, request: Request):
    http_response = None
    
    try:
        request.scope["path_params"] = {"codigo_dispositivo": codigo_dispositivo}
        http_response = await request_adapter(request, buscar_dispositivo_by_codigo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)



@router.get("/verificar_status", response_model = VerificarStatusDispositivoOutput)
async def verificar_status_dispositivo(request: Request, codigo_dispositivo: str):
    http_response = None
    
    try:
        http_response = await request_adapter(request, verificar_status_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.get("/posicao")
async def buscar_posicao_dispositivo(request: Request, codigo_dispositivo: str):
    http_response = None
    
    try:
        http_response = await request_adapter(request, buscar_posicao_dispositivo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)