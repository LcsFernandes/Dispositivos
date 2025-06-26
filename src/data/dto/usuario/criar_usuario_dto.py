from dataclasses import dataclass

@dataclass(frozen=True)
class CriarUsuarioDTO:
    re: str
    nome: str
    senha: str
        