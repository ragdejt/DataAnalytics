import sys
import platform
import subprocess
from rich import print
from log.log import log
from functions.table import create_table
from functions.stock import create_stock
from constants.constants import SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER
APP = f"""
┌─────────────────────────────────┐───────────────────────────┐
│ D a t a  A n a l y t i c s  1.0 │        by r4gd3j7         │
└─────────────────────────────────┘                           │
             Isso não é futurismo é DataAnalytics!            │
┌─────────────────────────────────────────────────────────────┘
└> Sistema Operacional: [bold cyan]{platform.system()}[/bold cyan]              
└> Versão do sistema: [bold cyan]{platform.release()}[/bold cyan]                
└> Versão detalhada: [bold cyan]{platform.version()}[/bold cyan]
└> Arquitetura do sistema: [bold cyan]{platform.architecture()}[/bold cyan]              
└> Tipo de maquina: [bold cyan]{platform.machine()}[/bold cyan]
└> Processador: [bold cyan]{platform.processor()}[/bold cyan]                
└> Edição do Windows: [bold cyan]{platform.win32_edition()}[/bold cyan]
└> Nome do computador: [bold cyan]{platform.node()}[/bold cyan]
└> Python: {platform.python_implementation()}
└> Versão do python: {platform.python_version()}
└> Informações da build: {platform.python_build()}
└> Compilador utilizado: {platform.python_compiler()}

"""

def main():
    print(APP)
    choice = input('-> ')
    match choice:
        case '0':
            sys.exit()
        case '1':
            print('Verificando diretorios necessarios [...]')
            try:
                necessary_dir = [
                    LOG_FOLDER,
                    SQL_FOLDER,
                    EXCEL_FOLDER,
                ]
                for i in necessary_dir:
                    if not i.exists():
                        i.mkdir(exist_ok=True, parents=True)
                        print(f'[yellow]Diretorio[/yellow]: [green]{i}[/green]')
                        log().debug(f'Diretorio: {i} criado')
                    else:
                        print(f'[yellow]Diretorio[/yellow]: [green]{i}[/green]')
                        log().debug(f'Diretorio: {i} encontrado')
            except FileNotFoundError:
                print('Erro: ')
                log().debug('Erro: ')
            except PermissionError:
                print('Erro: ')
                log().debug('Erro: ')
            else:
                print('Todos diretorios necessarios foram encontrados')
                log().debug('Todos diretorios necessarios foram encontrados')
            finally:
                main()
        case '2':
            try:
                print('Verificando tabelas SQL [...]')
                # Create all tables in the database.
                from models.usuario import Usuario
                from models.produto import Produto
                from models.pedido import Pedido
                from models.funcionario import Funcionario
                from models.ticket import Ticket    
                from models.estoque import Estoque
                create_table(Usuario)
                create_table(Produto)
                create_table(Pedido)
                create_table(Funcionario)
                create_table(Ticket)
                create_table(Estoque)
            except Exception:
                print('')
                log().debug('')
            else:
                print(
                """
                Deseja criar a estrutura de estoque ?
                [0]:[Sair]
                [1]:[Criar estoque]
                """)
                stock = input('-> ')
                match stock:
                    case 0:
                        main()
                    case '1':
                        create_stock()
                        main()
        case _:
            subprocess.Popen('streamlit run DataAnalytics.py', shell=True)

main()