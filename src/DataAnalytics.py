import pandas
import numpy
import streamlit
from config.page_config import page_config
from functions.create_tables import create_tables
from functions.create_directories import create_directories
from constants.paths import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER, MONTHS
from functions.graphs import graph_config

DataAnalytics = page_config(initial_sidebar_state="collapsed")
if streamlit.session_state['login']:
    streamlit.header(":green[Desempenho de processos logisticos]", divider="green")

    # Graficos TMD.
    with streamlit.expander(label='Tempo Médio de Descarga'):
        streamlit.subheader(":green[``TMD`` - Tempo Médio de Descarga]", divider="green")
        tmd_dataframe = pandas.DataFrame(
            data={
                'Janeiro':numpy.random.randint(0, 100, size=1),
                'Fevereiro':numpy.random.randint(0, 100, size=1),
                'Março':numpy.random.randint(0, 100, size=1),
                'Abril':numpy.random.randint(0, 100, size=1),
                'Maio':numpy.random.randint(0, 100, size=1),
                'Junho':numpy.random.randint(0, 100, size=1),
                'Julho':numpy.random.randint(0, 100, size=1),
                'Agosto':numpy.random.randint(0, 100, size=1),
                'Setembro':numpy.random.randint(0, 100, size=1),
                'Outubro':numpy.random.randint(0, 100, size=1),
                'Novembro':numpy.random.randint(0, 100, size=1),
                'Dezembro':numpy.random.randint(0, 100, size=1),
            }
        )
        graph_config(dataframe=tmd_dataframe, name='TMD')
        streamlit.info("Identifica gargalos no processo de descarregamento.")

        streamlit.divider()

        streamlit.metric(
            label=':green[``TMD`` - Tempo Médio de Descarga]',
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
        )

    # Graficos VAM.
    with streamlit.expander(label='Veiculos Atendidos por Mês'):
        streamlit.subheader(":green[``VAM`` - Veículos Atendidos por Mês]", divider="green")
        vam_dataframe = pandas.DataFrame(
            data={
                'Janeiro':numpy.random.randint(0, 100, size=1),
                'Fevereiro':numpy.random.randint(0, 100, size=1),
                'Março':numpy.random.randint(0, 100, size=1),
                'Abril':numpy.random.randint(0, 100, size=1),
                'Maio':numpy.random.randint(0, 100, size=1),
                'Junho':numpy.random.randint(0, 100, size=1),
                'Julho':numpy.random.randint(0, 100, size=1),
                'Agosto':numpy.random.randint(0, 100, size=1),
                'Setembro':numpy.random.randint(0, 100, size=1),
                'Outubro':numpy.random.randint(0, 100, size=1),
                'Novembro':numpy.random.randint(0, 100, size=1),
                'Dezembro':numpy.random.randint(0, 100, size=1),
            }
        )
        graph_config(dataframe=vam_dataframe, name='VAM')
        streamlit.info("Mostra se a equipe/doca está operando em ritmo ideal.")
        streamlit.divider()

        streamlit.metric(
            label=":green[``VAM`` - Veículos Atendidos por Mês]",
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
        )

    # Grafico TMC.
    with streamlit.expander(label='Tempo Médio de Conferência'):
        streamlit.subheader(":green[``TMC`` - Tempo Médio de Conferência]", divider="green")
        tmc_dataframe = pandas.DataFrame(
            data={
                'Janeiro':numpy.random.randint(0, 100, size=1),
                'Fevereiro':numpy.random.randint(0, 100, size=1),
                'Março':numpy.random.randint(0, 100, size=1),
                'Abril':numpy.random.randint(0, 100, size=1),
                'Maio':numpy.random.randint(0, 100, size=1),
                'Junho':numpy.random.randint(0, 100, size=1),
                'Julho':numpy.random.randint(0, 100, size=1),
                'Agosto':numpy.random.randint(0, 100, size=1),
                'Setembro':numpy.random.randint(0, 100, size=1),
                'Outubro':numpy.random.randint(0, 100, size=1),
                'Novembro':numpy.random.randint(0, 100, size=1),
                'Dezembro':numpy.random.randint(0, 100, size=1),
            }
        )
        graph_config(dataframe=tmc_dataframe, name='TMC')
        streamlit.info("Pode revelar lentidão em processos de conferência")
        streamlit.divider()
        streamlit.metric(
            label=':green[``TMC`` - Tempo Médio de Conferência]',
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
        )

    # Grafico POE.
    with streamlit.expander(label='Produtividade por Operador de Equipe'):
        streamlit.subheader(":green[``POE`` - Produtividade por Operador de Equipe]", divider="green")
        poe_dataframe = pandas.DataFrame(
            data={
                'Janeiro':numpy.random.randint(0, 100, size=1),
                'Fevereiro':numpy.random.randint(0, 100, size=1),
                'Março':numpy.random.randint(0, 100, size=1),
                'Abril':numpy.random.randint(0, 100, size=1),
                'Maio':numpy.random.randint(0, 100, size=1),
                'Junho':numpy.random.randint(0, 100, size=1),
                'Julho':numpy.random.randint(0, 100, size=1),
                'Agosto':numpy.random.randint(0, 100, size=1),
                'Setembro':numpy.random.randint(0, 100, size=1),
                'Outubro':numpy.random.randint(0, 100, size=1),
                'Novembro':numpy.random.randint(0, 100, size=1),
                'Dezembro':numpy.random.randint(0, 100, size=1),
            }
        )
        graph_config(dataframe=poe_dataframe, name='POE')
        streamlit.info("Ajuda a identificar colaboradores com baixa ou alta performance.")
        streamlit.divider()
        streamlit.metric(
            label=':green[``POE`` - Produtividade por Operador de Equipe]',
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
        )

    # Grafico TUA.
    with streamlit.expander(label='Taxa de Utilização de Agendamentos'):
        streamlit.subheader(":green[``TUA`` - Taxa de Utilização de Agendamentos]", divider="green")
        tua_dataframe = pandas.DataFrame(
            data={
                'Janeiro':numpy.random.randint(0, 100, size=1),
                'Fevereiro':numpy.random.randint(0, 100, size=1),
                'Março':numpy.random.randint(0, 100, size=1),
                'Abril':numpy.random.randint(0, 100, size=1),
                'Maio':numpy.random.randint(0, 100, size=1),
                'Junho':numpy.random.randint(0, 100, size=1),
                'Julho':numpy.random.randint(0, 100, size=1),
                'Agosto':numpy.random.randint(0, 100, size=1),
                'Setembro':numpy.random.randint(0, 100, size=1),
                'Outubro':numpy.random.randint(0, 100, size=1),
                'Novembro':numpy.random.randint(0, 100, size=1),
                'Dezembro':numpy.random.randint(0, 100, size=1),
            }
        )
        graph_config(dataframe=tua_dataframe, name='TUA')
        streamlit.info("Compara agendamentos previstos com os realizados. Alta taxa pode indicar boa aderência.")
        streamlit.divider()
        streamlit.metric(
            label=':green[``TUA`` - Taxa de Utilização de Agendamentos]',
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
        )

    # Grafico TRP.
    with streamlit.expander(label='Taxa de Retorno de Produto'):
        streamlit.subheader(":green[``TRP`` - Taxa de Retorno de Produto]", divider="green")
        streamlit.info("Mostra a quantidade de produtos devolvidos em relação ao total recebido.")
        streamlit.divider()

        streamlit.metric(
        label=':green[``TRP`` - Taxa de Retorno de Produto]',
        value=f'{numpy.random.randint(0, 100)}%',
        delta=f'{numpy.random.randint(0, 100)}%',
        delta_color="normal",
    )

    with streamlit.expander(label='Taxa de Devolução de produto'):
        streamlit.subheader(":green[``TDP`` - Taxa de Devolução de produto]", divider="green")
        streamlit.info("Pode apontar falhas na conferência ou transporte.")
        streamlit.divider()
        
        streamlit.metric(
        label=':green[``TDP`` - Taxa de Devolução de produto]',
        value=f'{numpy.random.randint(0, 100)}%',
        delta=f'{numpy.random.randint(0, 100)}%',
        delta_color="normal",
    )

    with streamlit.expander(label='Tempo de Conferência por Tipo de Produto'):
        streamlit.subheader(":green[``TCxTP`` - Tempo de Conferência por Tipo de Produto]", divider="green")
        streamlit.info("Útil para entender a complexidade por categoria (Ultra congelado, Congelado, Resfriado, Seco")
        streamlit.divider()
        streamlit.metric(
            label=':green[``TCxTP`` - Tempo de Conferência por Tipo de Produto]',
            value=f'{numpy.random.randint(0, 100)}%',
            delta=f'{numpy.random.randint(0, 100)}%',
            delta_color="normal",
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
    create_tables()

