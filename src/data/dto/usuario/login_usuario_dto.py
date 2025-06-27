from dataclasses import dataclass

@dataclass(frozen=True)
class LoginUsuarioDTO:
    re: int
    senha: str