from pydantic import BaseModel

class CriarUsuarioDTO(BaseModel):
    re: str
    nome: str
    senha: str

    class Config:
        extra = "forbid"