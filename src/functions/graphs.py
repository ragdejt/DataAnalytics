import pandas
import streamlit
def graph_config(dataframe:pandas.DataFrame, name):
    """Configura o gráfico com base no dataframe, eixo X e eixo Y."""
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
        default='Dia',
        key=f'unique_key_for_pills_{name}',
    )
    if not selected:
        streamlit.subheader('``Nenhuma coluna selecionada!``')
    column1, column2, column3 = streamlit.columns(3)
    with column1:
        horizontal = streamlit.toggle(
            label='Exibir gráfico horizontal',
            value=True,
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
