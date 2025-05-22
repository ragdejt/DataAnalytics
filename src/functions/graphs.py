import streamlit
import plotly.express
from decorators.timer import timer

dataframe_exemplo = plotly.express.data.tips()

@timer
def tmc_graph():
    """Grafico de Tempo Médio de Conferência (TMC)."""
    graph_tmc = plotly.express.scatter(
        dataframe_exemplo,
        x='day',
        y='total_bill',
        title='Tempo Médio de Conferência',
        subtitle='TMC',
        labels={'Mês': 'Mês', 'TMC': 'Tempo Médio de Conferência'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tmc, use_container_width=True)

@timer
def poe_graph():
    """Grafico de Produtividade por Operador de Equipe (POE)."""
    graph_poe = plotly.express.box(
        dataframe_exemplo,
        x='day',
        y='total_bill',
        title='Produtividade por Operador de Equipe',
        subtitle='POE',
        labels={'Mês': 'Mês', 'POE': 'Produtividade por Operador de Equipe'},
        color_discrete_sequence=['#00FF00']
    )
    streamlit.plotly_chart(graph_poe, use_container_width=True)

@timer
def tua_graph():
    """Grafico de Taxa de Utilização de Agendamentos (TUA)."""
    graph_tua = plotly.express.funnel(
        dataframe_exemplo,
        x='day',
        y='total_bill',
        title='Taxa de Utilização de Agendamentos',
        subtitle='TUA',
        labels={'Mês': 'Mês', 'TUA': 'Taxa de Utilização de Agendamentos'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tua, use_container_width=True)

@timer
def vam_graph():
    """Grafico de Veículos Atendidos por Mês (VAM)."""
    graph_vam = plotly.express.line(
        dataframe_exemplo,
        x='day',
        y='total_bill',
        title='Veículos Atendidos por Mês',
        subtitle='VAM',
        labels={'Mês': 'Mês', 'VAM': 'TVeículos Atendidos por Mês'},
        color_discrete_sequence=['#00FF00'],
        markers=True,
    )
    streamlit.plotly_chart(graph_vam, use_container_width=True)

@timer
def tmd_graph():
    """Grafico de Tempo Médio de Descarga (TMD)."""
    graph_tmd = plotly.express.bar(
        dataframe_exemplo,
        x='day',
        y='total_bill',
        title='Tempo Médio de Descarga',
        subtitle='TMD',
        labels={'Mês': 'Mês', 'TMD': 'Tempo Médio de Descarga'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tmd, use_container_width=True)
