import streamlit
from config.page_config import page_config
from functions.table import view_table
estoques = page_config(title='Estoques')

if streamlit.session_state['login']:
    match estoques:
        case 'Adicionar':
            streamlit.subheader(':green[Adicionar]', divider='green')
            streamlit.number_input(
                label='Estoque',
                min_value=1,
                max_value=4,
                step=1,
            )
            streamlit.number_input(
                label='Rua',
                min_value=1,
                max_value=10,
                step=1,                
            )
            streamlit.number_input(
                label='Predio',
                min_value=1,
                max_value=10,
                step=1,
            )
            streamlit.number_input(
                label='Andar',
                min_value=0,
                max_value=5,
                step=1,
            )
            streamlit.selectbox(
                label='Lado',
                options=['A', 'B'],
                placeholder='Selecione o lado',
                index=None
            )
            streamlit.number_input(
                label='Produto',
                min_value=0,
                step=1,
            )
            streamlit.number_input(
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
            streamlit.data_editor(view_table('Estoques'), hide_index=True)
        case 'Consultar':
            streamlit.dataframe(view_table('Estoques'), hide_index=True)