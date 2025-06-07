import pandas
import numpy
import streamlit
import plotly.express
from graphs.graph_bar import graph_bar

graph_data = pandas.DataFrame(data={
        'Dia':range(1,31),
        'Janeiro':numpy.random.randint(low=1, high=100, size=30),
        'Fevereiro':numpy.random.randint(low=1, high=100, size=30),
        'Março':numpy.random.randint(low=1, high=100, size=30),
        'Abril':numpy.random.randint(low=1, high=100, size=30),
        'Maio':numpy.random.randint(low=1, high=100, size=30),
        'Junho':numpy.random.randint(low=1, high=100, size=30),
        'Julho':numpy.random.randint(low=1, high=100, size=30),
        'Agosto':numpy.random.randint(low=1, high=100, size=30),
        'Setembro':numpy.random.randint(low=1, high=100, size=30),
        'Outubro':numpy.random.randint(low=1, high=100, size=30),
        'Novembro':numpy.random.randint(low=1, high=100, size=30),
        'Dezembro':numpy.random.randint(low=1, high=100, size=30)
    }
)
    

def graph_config(dataframe:pandas.DataFrame, name):
    """
    Configura o gráfico com base no dataframe, eixo X e eixo Y.
    
    Args:
        dataframe (pandas.DataFrame): DataFrame contendo os dados a serem plotados.
        name (str): Nome do gráfico para identificação.
    """
    with streamlit.expander(label=f'{name}'):

        graph_type = streamlit.selectbox(
            label="Selecione o tipo de gráfico",
            options=[
                'Barra',
                'Area',
                'Linha',
                'Scatter',
            ],
            index=None,
            placeholder="Escolha o tipo de gráfico.",
            key=f'unique_key_for_selectbox_{name}',
        )
        orientacao = streamlit.selectbox(
            label='Orientação',
            options=["Horizontal", "Vertical"],
            index=None,
            placeholder='Selecione a orientação do gráfico.',
            key=f'unique_key_for_orientation_{name}'
        )
        orientation_code = None
        match orientacao:
            case "Horizontal":
                orientation_code = 'h'
            case "Vertical":
                orientation_code = 'v'

        bar_type = streamlit.selectbox(
            label='Tipo de barra',
            options=['Relativo', 'Grupo', 'Sobrepor'],
            index=None,
            placeholder='Escolha o tipo de barra.',
            key=f'unique_key_for_bartype_{name}'
        )
        bar_type_code = None
        match bar_type:
            case 'Relativo':
                bar_type_code = 'relative'
            case 'Grupo':
                bar_type_code = 'group'
            case 'Sobrepor':
                bar_type_code = 'overlay'

        match graph_type:
            case 'Barra':
                streamlit.plotly_chart(figure_or_data=graph_bar(
                    df=graph_data,
                    x='Dia',
                    xaxis_title='Dia',
                    y=['Janeiro',
                        'Fevereiro',
                        'Março',
                        'Abril',
                        'Maio',
                        'Junho',
                        'Julho',
                        'Agosto',
                        'Setembro',
                        'Outubro',
                        'Novembro',
                        'Dezembro',
                    ],
                    yaxis_title='Valor',
                    title=f'Grafico {name}',
                    subtitle='Grafico barra',
                    legend_title='Mês',
                    orientation=orientation_code,
                    barmode=bar_type_code
                    )
                )      
                column1, column2 = streamlit.columns((2))
                with column1:
                    streamlit.metric(
                        label=f':green[{name}]',
                        value=f'{numpy.random.randint(0, 100)}%',
                        delta=f'{numpy.random.randint(0, 100)}% em comparação com mês anterior',
                        delta_color="normal",
                        border=True
                    )
                with column2:
                    streamlit.metric(
                        label=f':green[{name}]',
                        value=f'{numpy.random.randint(0, 60)}min',
                        delta=f'{numpy.random.randint(0, 60)}min em comparação com mês anterior',
                        delta_color="normal",
                        border=True
                    )

            case 'Area':
                pass
            case 'Linha':
                pass
            case 'Scatter':
                pass


def graph_scatter(
    x,
    y,
    title:str,
    subtitle:str
):
    fig = plotly.express.scatter(
        x=x,
        y=y,
        title=title,
        subtitle=subtitle
    )
    streamlit.plotly_chart(
        figure_or_data=fig,
        use_container_width=True,
    )

def graph_scatter_3d(
    x,
    y,
    z,
    title:str,
    subtitle:str
):
    fig = plotly.express.scatter_3d(
        x=x,
        y=y,
        z=z,
        title=title,
        subtitle=subtitle
    )
    streamlit.plotly_chart(
        figure_or_data=fig,
        use_container_width=True,
    )

def graph_scatter_map(
    data,
    latitude,
    longitude,
    title,
    subtitle
):
    fig = plotly.express.scatter_map(
        data_frame=data,
        lat=latitude,
        lon=longitude,
        map_style='satellite',
        title=title,
        subtitle=subtitle
    )
    streamlit.plotly_chart(
        figure_or_data=fig,
        use_container_width=True,

    )

def graph_line(x, y, title, subtitle):
    fig = plotly.express.line(
        x=x,
        y=y,
        title=title,
        subtitle=subtitle
    )
    streamlit.plotly_chart(
        figure_or_data=fig,
        use_container_width=True,
    )
