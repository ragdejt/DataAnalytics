import pandas
import numpy
import streamlit
import numpy.random
from functions.graph import graph_view
from config.page_config import page_config
from functions.table import create_table
from functions.directories import create_directories
from constants.constants import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER, DAY

DataAnalytics = page_config(initial_sidebar_state="collapsed")
if streamlit.session_state['login']:
    streamlit.header(":green[Desempenho de processos logisticos]", divider="green")
    # Graficos TMD.
    graph_view(
        nome='Tempo Médio de Descarga',
        sigla='TMD',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Graficos VAM.
    graph_view(
        nome='Veiculos Atendidos por Mês',
        sigla='VAM',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TMC.
    graph_view(
        nome='Tempo Médio de Conferência',
        sigla='TMC',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico POE.
    graph_view(
        nome='Produtividade por Operador de Equipe',
        sigla='POE',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TUA.
    graph_view(
        nome='Taxa de Utilização de Agendamentos',
        sigla='TUA',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico TRP.
    graph_view(
        nome='Taxa de Retorno de Produto',
        sigla='TRP',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )
    # Grafico IDE.
    graph_view(
        nome='Indice de disponibilidade de estoque',
        sigla='IDE',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }             
        )
    )
    # Grafico TIO.
    graph_view(
        nome='Taxa de Itens Obsoletos',
        sigla='TIO',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }              
        )           
    ) 
    graph_view(
        nome='Custo de Manutenção de Estoque',
        sigla='CME',
        dataframe=pandas.DataFrame(
            data={
                'Dia': DAY,
                '01-Janeiro': numpy.random.randint(0, 100, size=30),
                '02-Fevereiro': numpy.random.randint(0, 100, size=30),
                '03-Março': numpy.random.randint(0, 100, size=30),
                '04-Abril': numpy.random.randint(0, 100, size=30),
                '05-Maio': numpy.random.randint(0, 100, size=30),
                '06-Junho': numpy.random.randint(0, 100, size=30),
                '07-Julho': numpy.random.randint(0, 100, size=30),
                '08-Agosto': numpy.random.randint(0, 100, size=30),
                '09-Setembro': numpy.random.randint(0, 100, size=30),
                '10-Outubro': numpy.random.randint(0, 100, size=30),
                '11-Novembro': numpy.random.randint(0, 100, size=30),
                '12-Dezembro': numpy.random.randint(0, 100, size=30),
            }
        )
    )       
else:
    # Create necessary directories.
    create_directories(
        SCRIPT_FOLDER,
        SQL_FOLDER,
        EXCEL_FOLDER,
        LOG_FOLDER
    )
    # Create all tables in the database.
    from models.usuario import Usuario
    from models.produto import Produto
    from models.pedido import Pedido
    from models.funcionario import Funcionario
    from models.ticket import Ticket

    create_table(Usuario)
    create_table(Produto)
    create_table(Pedido)
    create_table(Funcionario)
    create_table(Ticket)