from pydantic import BaseModel

class CriarUsuarioDTO(BaseModel):
    re: str
    nome: str
    senha: str

    class Config:
        extra = "forbid"

class LoginUsuarioDTO(BaseModel):
    re: str
    senha: str

    class Config:
        extra = "forbid"

class AlterarSenhaUsuarioDTO(BaseModel):
    re: str
    senha_atual: str
    senha: str

    class Config:
        extra = "forbid"