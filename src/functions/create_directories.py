from rich import print
from decorators.timer import timer
from constants.paths import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER, OK, RUNNING

LIST_DIRECTORIES = [
    SCRIPT_FOLDER,
    SQL_FOLDER,
    EXCEL_FOLDER,
    LOG_FOLDER
]
@timer
def create_directories():
    """Cria os diretórios necessários para o projeto funcionar."""
    for dir in LIST_DIRECTORIES:
        if dir.exists():
            print(f"{OK} {dir}\n")
        else:
            dir.mkdir(parents=True, exist_ok=True)
            print(f"{OK} Diretório criado: {dir}\n")
