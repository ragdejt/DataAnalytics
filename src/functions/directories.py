from rich import print
from pathlib import Path
from decorators.timer import timer
from constants.constants import OK

@timer
def create_directories(*directories:Path):
    """
    Cria os diretórios necessários para o projeto funcionar.
    
    Args:
        directories (Path): Lista de diretórios a serem criados.
    """
    for dir in directories:
        if dir.exists():
            print(f"{OK} {dir}\n")
        else:
            dir.mkdir(parents=True, exist_ok=True)
            print(f"{OK} Diretório criado: {dir}\n")
