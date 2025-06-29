from pydantic import BaseModel

class CriarUsuarioDTO(BaseModel):
    re: int
    nome: str
    senha: str

    class Config:
        extra = "forbid"

class LoginUsuarioDTO(BaseModel):
    re: int
    senha: str

    class Config:
        extra = "forbid"