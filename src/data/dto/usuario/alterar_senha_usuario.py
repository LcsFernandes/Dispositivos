from dataclasses import dataclass

@dataclass(frozen=True)
class AlterarSenhaUsuarioDTO:
    re: int
    senha_atual: str
    senha: str