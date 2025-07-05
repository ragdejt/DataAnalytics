import os
import platform
import subprocess
from rich import print
from log.log import log
from functions.table import create_table
from functions.stock import create_stock
from constants.constants import SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER
APP = f"""[bold white]
┌─────────────────────────────────┬───────────────────────────┐
│ D a t a  A n a l y t i c s  1.0 │        by r4gd3j7         │
└─────────────────────────────────┘                           │
             Isso não é futurismo é DataAnalytics!            │
┌─────────────────────────────────────────────────────────────┘
├> Nome do computador: [bold green]{platform.node()}[/bold green]
├> Sistema Operacional: [bold green]{platform.system()}[/bold green]
├> Edição do Windows: [bold green]{platform.win32_edition()}[/bold green]
├> Versão do sistema: [bold green]{platform.version()}[/bold green]
├> Arquitetura do sistema: [bold green]{platform.architecture()}[/bold green]
├> Tipo de maquina: [bold green]{platform.machine()}[/bold green]
├> Processador: [bold green]{platform.processor()}[/bold green]
├> Versão do python: [bold green]{platform.python_version()}[/bold green]
├> Informações da build: [bold green]{platform.python_build()}[/bold green]
├> Compilador utilizado: [bold green]{platform.python_compiler()}[/bold green]
│"""
def main():
    print(APP)
    choice = input('├> ')
    os.system('cls')
    match choice:
        case '1':
            try:
                necessary_dir = [
                    LOG_FOLDER,
                    SQL_FOLDER,
                    EXCEL_FOLDER,
                ]
                for i in necessary_dir:
                    if not i.exists():
                        i.mkdir(exist_ok=True, parents=True)
                        print(f'├> [green]Diretorio[/green]: {i}')
                        log().debug(f'Diretorio: {i} criado')
                    else:
                        print(f'├> [green]Diretorio[/green]: {i}')
                        log().debug(f'Diretorio: {i} encontrado')
            except FileNotFoundError:
                print('Erro: ')
                log().debug('Erro: ')
            except PermissionError:
                print('Erro: ')
                log().debug('Erro: ')
            else:
                print('├> Todos diretorios necessarios foram encontrados.')
                log().debug('Todos diretorios necessarios foram encontrados')
                print('├┐')
                input('│└> Pressione Enter para criar estruturas de tabelas SQL.')
                print('├┐')
                input('│└> Pressione Enter para criar estrutura de estoque.')
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
                create_stock()
                os.system('cls')
                main()
        case _:
            subprocess.Popen('streamlit run DataAnalytics.py', shell=True)            

main()