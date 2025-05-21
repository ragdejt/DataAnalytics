from dataclasses import dataclass

@dataclass
class Funcionario:
    """Classe Funcionario"""
    nome: str
    idade: int
    cargo: str
    salario: float

    def __post_init__(self):
        """Método chamado após a inicialização do dataclass."""
        