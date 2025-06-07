import streamlit
from config.page_config import page_config
from functions.table import view_table, edit_table
from constants.constants import CATEGORIAS

estoques = page_config(title='Estoques')

if streamlit.session_state['login']:
    match estoques:
        case 'Adicionar':
            streamlit.subheader(':green[Adicionar]', divider='green')
            streamlit.info('Funcionalidade em desenvolvimento')
            estoque = streamlit.selectbox(
                label='Estoque',
                options=CATEGORIAS
            )
            rua = streamlit.number_input(
                label='Rua',
                min_value=1,
                max_value=10,
                step=1,                
            )
            predio = streamlit.number_input(
                label='Predio',
                min_value=1,
                max_value=10,
                step=1,
            )
            andar = streamlit.number_input(
                label='Andar',
                min_value=0,
                max_value=5,
                step=1,
            )
            lado = streamlit.selectbox(
                label='Lado',
                options=['A', 'B'],
                placeholder='Selecione o lado',
            )
            produto = streamlit.number_input(
                label='Produto',
                min_value=0,
                step=1,
            )
            quantidade = streamlit.number_input(
                label='Quantidade',
                min_value=0,
                step=1,
            )
            if streamlit.button(
                label='Adicionar',
                use_container_width=True,
            ):
                pass
        case 'Editar':
            streamlit.subheader(':green[Editar estoque]', divider='green')
            edit_table('Estoques')
        case 'Consultar':
            streamlit.dataframe(view_table('Estoques'), hide_index=True)