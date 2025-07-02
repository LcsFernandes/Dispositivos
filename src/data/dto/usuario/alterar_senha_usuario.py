from dataclasses import dataclass

@dataclass(frozen=True)
class AlterarSenhaUsuarioDTO:
    re: str
    senha_atual: str
    senha: str