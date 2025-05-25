import streamlit
import pandas

def graph_config(dataframe:pandas.DataFrame, name):
    """Configura o gráfico com base no dataframe, eixo X e eixo Y."""
    column1, column2 = streamlit.columns(2)
    with column1:
        graph_type = streamlit.selectbox(
            label="Selecione o tipo de gráfico",
            options=['Barra', 'Area', 'Linha'],
            index=0,
            placeholder="Escolha o tipo de gráfico que deseja visualizar.",
            key=f'unique_key_for_selectbox_{name}',
        )
    with column2:
        selected = streamlit.multiselect(
            label='Selecione uma ou mais colunas',
            options=dataframe.columns,
            placeholder="Escolha oque deseja comparar.",
            key=f'unique_key_for_multiselect_{name}',
        )
    column3, column4 = streamlit.columns(2)
    with column3:
        horizontal = streamlit.checkbox(
            label='Exibir gráfico horizontal',
            value=True,
            disabled=False,
            key=f'unique_key_for_checkbox_{name}',
        )
    with column4:
        stacked = streamlit.checkbox(
            label='Exibir gráfico empilhado',
            value=True,
            key=f'unique_key_for_stacked_checkbox_{name}',
        )
    match graph_type:
        case 'Barra':
            graph = streamlit.bar_chart(
                data=dataframe[selected],
                x_label='Eixo X',
                y_label='Eixo Y',
                use_container_width=True,
                horizontal=horizontal,
                stack=stacked
            )
            return graph
        case 'Area':
            graph = streamlit.area_chart(
                dataframe[selected],
                use_container_width=True,
                stack=stacked
            )
            return graph
        case 'Linha':
            graph = streamlit.line_chart(
                data=dataframe[selected],
                use_container_width=True,
            )
            return graph