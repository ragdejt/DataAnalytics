import os
import platform
import subprocess
from rich import print
from log.log import log
from functions.table import create_table
from functions.stock import create_stock
from constants.constants import SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER
APP = f"""
┌─────────────────────────────────┬───────────────────────────┐
│ D a t a  A n a l y t i c s  1.0 │        by r4gd3j7         │
└─────────────────────────────────┘                           │
             Isso não é futurismo é DataAnalytics!            │
┌─────────────────────────────────────────────────────────────┘
├> Nome do computador: [bold green]{platform.node()}[/bold green]
├> Sistema Operacional: [bold green]{platform.system()}[/bold green]
├> Edição do Windows: [bold green]{platform.win32_edition()}[/bold green]
├> Versão do sistema: [bold green]{platform.release()}[/bold green]
├> Versão detalhada: [bold green]{platform.version()}[/bold green]
├> Arquitetura do sistema: [bold green]{platform.architecture()}[/bold green]
├> Tipo de maquina: [bold green]{platform.machine()}[/bold green]
├> Processador: [bold green]{platform.processor()}[/bold green]
├> Versão do python: [bold green]{platform.python_version()}[/bold green]
├> Informações da build: [bold green]{platform.python_build()}[/bold green]
├> Compilador utilizado: [bold green]{platform.python_compiler()}[/bold green]
│
├> [0]: Inicia DataAnalytics.
├> [1]: Verificar arquivos/diretorios necessarios.
├> [2]: Verificar estruturas/tabelas SQL.
│"""
def main():
    print(APP)
    choice = input('├> ')
    match choice:
        case '0':
            subprocess.Popen('streamlit run DataAnalytics.py', shell=True)            
        case '1':
            print('├> Verificando diretorios necessarios [...]')
            try:
                necessary_dir = [
                    LOG_FOLDER,
                    SQL_FOLDER,
                    EXCEL_FOLDER,
                ]
                for i in necessary_dir:
                    if not i.exists():
                        i.mkdir(exist_ok=True, parents=True)
                        print(f'├> Diretorio: [green]{i}[/green]')
                        log().debug(f'Diretorio: {i} criado')
                    else:
                        print(f'├> Diretorio: [green]{i}[/green]')
                        log().debug(f'Diretorio: {i} encontrado')
            except FileNotFoundError:
                print('Erro: ')
                log().debug('Erro: ')
            except PermissionError:
                print('Erro: ')
                log().debug('Erro: ')
            else:
                print('└> Todos diretorios necessarios foram encontrados')
                log().debug('Todos diretorios necessarios foram encontrados')
            finally:
                input('')
                os.system('cls')
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