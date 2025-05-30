import pandas
import numpy
import streamlit
def graph_config(dataframe:pandas.DataFrame, name):
    """
    Configura o gráfico com base no dataframe, eixo X e eixo Y.
    
    Args:
        dataframe (pandas.DataFrame): DataFrame contendo os dados a serem plotados.
        name (str): Nome do gráfico para identificação.
    """
    graph_type = streamlit.selectbox(
        label="Selecione o tipo de gráfico",
        options=['Barra', 'Area', 'Linha', 'Scatter'],
        index=0,
        placeholder="Escolha o tipo de gráfico que deseja visualizar.",
        key=f'unique_key_for_selectbox_{name}',
    )
    selected = streamlit.pills(
        label='Selecione uma ou mais colunas',
            
        options=dataframe.columns,
        selection_mode='multi',
        default=[
            'Dia',
            "01-Janeiro",
            "02-Fevereiro",
            "03-Março",
            "04-Abril",
            "05-Maio",
            "06-Junho",
            "07-Julho",
            "08-Agosto",
            "09-Setembro",
            "10-Outubro",
            "11-Novembro",
            "12-Dezembro"
        ],
        key=f'unique_key_for_pills_{name}',
    )
    if not selected:
        streamlit.subheader('``Nenhuma coluna selecionada!``')
    column1, column2, column3 = streamlit.columns(3)
    with column1:
        horizontal = streamlit.toggle(
            label='Exibir gráfico horizontal',
            value=False,
            disabled=graph_type != 'Barra',
            key=f'unique_key_for_checkbox_toggle_{name}',
        )
    with column2:
        stacked = streamlit.toggle(
            label='Exibir gráfico empilhado',
            value=True,
            disabled=graph_type not in 'Barra',
            key=f'unique_key_for_stacked_toggle_{name}',
        )
    with column3:
        if streamlit.toggle(
            label='3d',
            value=True,
            key=f'unique_key_for_3d_toggle_{name}',
            disabled=True
        ):
            pass
    match graph_type:
        case 'Barra':
            streamlit.bar_chart(
                data=dataframe[selected],
                x='Dia',
                y=selected,
                y_label=['Dia' if horizontal else 'Tempo (minutos)'],
                use_container_width=True,
                horizontal=horizontal,
                stack=stacked
            )
        case 'Area':
            streamlit.area_chart(
                dataframe[selected],
                x='Dia',
                y=selected,
                use_container_width=True,
                stack=stacked
            )
        case 'Linha':
            streamlit.line_chart(
                data=dataframe[selected],
                x='Dia',
                y=selected,
                use_container_width=True,
            )
        case 'Scatter':
            streamlit.scatter_chart(
                data=dataframe[selected],
                x='Dia',
                y=selected,
                use_container_width=True,
            )

def graph_view(nome:str, sigla:str, dataframe:pandas.DataFrame):
    """
    Exibe o gráfico com base no dataframe e nome.

    Args:
        nome (str): Nome do gráfico.
        sigla (str): Sigla do gráfico.
        dataframe (pandas.DataFrame): DataFrame contendo os dados a serem plotados.
    """
    with streamlit.expander(label=f'{nome}'):
        streamlit.subheader(f":green[``{sigla}`` - {nome}]", divider='green')

        with streamlit.container(border=True):
            streamlit.metric(
                label=f':green[``{sigla}`` - {nome}]',
                value=f'{numpy.random.randint(0, 100)}%',
                delta=f'{numpy.random.randint(0, 100)}%',
                delta_color="normal",
            )
            streamlit.metric(
                label=f':green[``{sigla}`` - {nome}]',
                value=f'{numpy.random.randint(0, 60)}min',
                delta=f'{numpy.random.randint(0, 60)}min',
                delta_color="normal",
            )
        graph_config(dataframe, nome)

