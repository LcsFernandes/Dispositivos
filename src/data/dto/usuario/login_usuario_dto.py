from dataclasses import dataclass

@dataclass(frozen=True)
class LoginUsuarioDTO:
    re: str
    senha: str