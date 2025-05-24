import streamlit
import plotly.express

dataframe_exemplo = plotly.express.data.iris()

# TMC - Tempo Médio de Conferência
def tmc_graph():
    """Grafico de Tempo Médio de Conferência (TMC)."""
    graph_tmc = plotly.express.scatter(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        title='Tempo Médio de Conferência',
        subtitle='TMC',
        labels={'Mês': 'Mês', 'TMC': 'Tempo Médio de Conferência'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tmc, use_container_width=True)
# POE - Produtividade por Operador de Equipe
def poe_graph():
    """Grafico de Produtividade por Operador de Equipe (POE)."""
    graph_poe = plotly.express.box(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        title='Produtividade por Operador de Equipe',
        subtitle='POE',
        labels={'Mês': 'Mês', 'POE': 'Produtividade por Operador de Equipe'},
        color_discrete_sequence=['#00FF00']
    )
    streamlit.plotly_chart(graph_poe, use_container_width=True)
# TUA - Taxa de Utilização de Agendamentos
def tua_graph():
    """Grafico de Taxa de Utilização de Agendamentos (TUA)."""
    graph_tua = plotly.express.funnel(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        title='Taxa de Utilização de Agendamentos',
        subtitle='TUA',
        labels={'Mês': 'Mês', 'TUA': 'Taxa de Utilização de Agendamentos'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tua, use_container_width=True)
# VAM - Veículos Atendidos por Mês
def vam_graph():
    """Grafico de Veículos Atendidos por Mês (VAM)."""
    graph_vam = plotly.express.line(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        title='Veículos Atendidos por Mês',
        subtitle='VAM',
        labels={'Mês': 'Mês', 'VAM': 'TVeículos Atendidos por Mês'},
        color_discrete_sequence=['#00FF00'],
        markers=True,
    )
    streamlit.plotly_chart(graph_vam, use_container_width=True)
# TMD - Tempo Médio de Descarga
def tmd_graph():
    """Grafico de Tempo Médio de Descarga (TMD)."""
    graph_tmd = plotly.express.bar(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        title='Tempo Médio de Descarga',
        subtitle='TMD',
        labels={'Mês': 'Mês', 'TMD': 'Tempo Médio de Descarga'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tmd, use_container_width=True)
#TRP - Taxa de Retorno de Produto
def trp_graph():
    """Grafico de Taxa de Retorno de Produto (TRP)."""
    graph_trp = plotly.express.pie(
        dataframe_exemplo,
        values='sepal_length',
        names='sepal_width',
        title='Taxa de Retorno de Produto',
        subtitle='TRP',
        labels={'Mês': 'Mês', 'TRP': 'Taxa de Retorno de Produto'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_trp, use_container_width=True)
#TDP - Taxa de Devolução de produto
def tdp_graph():
    """Grafico de Taxa de Devolução de produto (TDP)."""
    graph_tdp = plotly.express.line_3d(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        z='petal_length',
        title='Taxa de Devolução de produto',
        subtitle='TDP',
        labels={'Mês': 'Mês', 'TDP': 'Taxa de Devolução de produto'},
        color_discrete_sequence=['#00FF00'],
        markers=True,
    )
    streamlit.plotly_chart(graph_tdp, use_container_width=True)
#TCxTP - Tempo de Conferência por Tipo de Produto
def tcxtp_graph():
    """Grafico de Tempo de Conferência por Tipo de Produto (TCxTP)."""
    graph_tcxtp = plotly.express.scatter_3d(
        dataframe_exemplo,
        x='sepal_width',
        y='sepal_length',
        z='petal_length',
        title='Tempo de Conferência por Tipo de Produto',
        subtitle='TCxTP',
        labels={'Mês': 'Mês', 'TCxTP': 'Tempo de Conferência por Tipo de Produto'},
        color_discrete_sequence=['#00FF00'],
    )
    streamlit.plotly_chart(graph_tcxtp, use_container_width=True)