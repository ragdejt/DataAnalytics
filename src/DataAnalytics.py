import streamlit
from config.page_config import page_config
from functions.create_tables import create_tables
from functions.create_directories import create_directories
from constants.paths import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER, LOG_FOLDER
from functions.graphs import tmc_graph, poe_graph, tua_graph, vam_graph, tmd_graph

DataAnalytics = page_config(initial_sidebar_state="collapsed")
if streamlit.session_state['login']:
    streamlit.header(":green[Desempenho de processos logisticos]", divider="green")
    with streamlit.expander("Graficos"):
        # Graficos TMD.
        streamlit.subheader(":green[``TMD`` - Tempo Médio de Descarga]", divider="green")
        tmd_graph()
        streamlit.info("Identifica gargalos no processo de descarregamento.")
        streamlit.divider()

        # Graficos VAM.
        streamlit.subheader(":green[``VAM`` - Veículos Atendidos por Mês]", divider="green")
        vam_graph()
        streamlit.info("Mostra se a equipe/doca está operando em ritmo ideal.")
        streamlit.divider()

        # Grafico TMC.
        streamlit.subheader(":green[``TMC`` - Tempo Médio de Conferência]", divider="green")
        tmc_graph()
        streamlit.info("Pode revelar lentidão em processos de conferência")
        streamlit.divider()

        # Grafico POE.
        streamlit.subheader(":green[``POE`` - Produtividade por Operador de Equipe]", divider="green")
        poe_graph()

        streamlit.info("Ajuda a identificar colaboradores com baixa ou alta performance.")
        streamlit.divider()

        # Grafico TUA.
        streamlit.subheader(":green[``TUA`` - Taxa de Utilização de Agendamentos]", divider="green")
        tua_graph()
        streamlit.info("Compara agendamentos previstos com os realizados. Alta taxa pode indicar boa aderência.")
        streamlit.divider()

        # Grafico TRP.
        streamlit.subheader(":green[``TRP`` - Taxa de Retorno de Produto]", divider="green")

        streamlit.info("Mostra a quantidade de produtos devolvidos em relação ao total recebido.")

        # Grafico TDP.
        streamlit.subheader(":green[``TDP`` - Taxa de Devolução de produto]", divider="green")

        streamlit.info("Pode apontar falhas na conferência ou transporte.")
        streamlit.divider()

        # Grafico TCxTP.
        streamlit.subheader(":green[``TCxTP`` - Tempo de Conferência por Tipo de Produto]", divider="green")

        streamlit.info("Útil para entender a complexidade por categoria (Ultra congelado, Congelado, Resfriado, Seco")
        streamlit.divider()

    with streamlit.expander('Metricas', expanded=True):
        column1, column2, column3 = streamlit.columns(3)
        with column1:
            streamlit.metric(
                label=':green[``TMC`` - Tempo Médio de Conferência]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
            streamlit.metric(
                label=':green[``TMD`` - Tempo Médio de Descarga]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
        with column2:
            streamlit.metric(
                label=':green[``POE`` - Produtividade por Operador de Equipe]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
            streamlit.metric(
                label=':green[``TUA`` - Taxa de Utilização de Agendamentos]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
            streamlit.metric(
                label=':green[``TCxTP`` - Tempo de Conferência por Tipo de Produto]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
        with column3:
            streamlit.metric(
                label=':green[``TRP`` - Taxa de Retorno de Produto]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
            streamlit.metric(
                label=':green[``TDP`` - Taxa de Devolução de produto]',
                value="00:00:00",
                delta="00:00:00",
                delta_color="normal",
            )
            streamlit.metric(
                label=":green[``VAM`` - Veículos Atendidos por Mês]",
                value="00:00:00",
                delta="00:00:00",
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

