from dataclasses import dataclass

@dataclass(frozen=True)
class CriarUsuarioDTO:
    re: str
    senha: str