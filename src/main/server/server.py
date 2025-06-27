from fastapi import FastAPI, Request
from starlette.responses import Response
from src.main.routes import dispositivo_routes
from src.main.routes import movimentacao_routes
from src.main.routes import vaga_routes
from src.main.routes import usuario_routes
from src.infra.services.token_service import TokenService
from src.presentation.middleware.auth_middleware import AuthMiddleware
from src.infra.logger.logger import get_logger
import time

app = FastAPI()

auth_middleware = AuthMiddleware(
    token_service=TokenService(),
    exclude_routes=["/usuario/login"]
)

@app.middleware("http")
def auth_middleware_endpoint(request: Request, call_next):
    return auth_middleware(request, call_next)

app.include_router(dispositivo_routes.router)
app.include_router(movimentacao_routes.router)
app.include_router(vaga_routes.router)
app.include_router(usuario_routes.router)


logger = get_logger()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    params = {}
    
    # Verificar o Content-Type primeiro
    content_type = request.headers.get("content-type", "")
    params["content_type"] = content_type
    
    try:
        if "application/json" in content_type:
            # Tentar ler o JSON apenas se for do tipo correto
            params["json"] = await request.json()
        else:
            params["json"] = None
    except Exception:
        params["json"] = None
    
    try:
        form = await request.form()
        params["form"] = dict(form)
    except Exception:
        params["form"] = None
    
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    
    # Log adicional para debugging
    logger.debug(f"Content-Type: {content_type}")
    if params["json"] is None and "application/json" in content_type:
        logger.warning("JSON não pôde ser decodificado")
    
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    response.body_iterator = iterate_in_chunks(response_body)
    
    try:
        response_text = response_body.decode("utf-8")
    except Exception:
        response_text = "<não pôde decodificar>"
    
    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Tempo: {process_time:.4f}s | "
        f"IP: {request.client.host} | "
        f"Params: {params} | "
        f"Response: {response_text}"
    )
    return response

async def iterate_in_chunks(content: bytes, chunk_size: int = 4096):
     for i in range(0, len(content), chunk_size):
        yield content[i:i+chunk_size]