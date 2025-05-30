import streamlit
from config.page_config import page_config
from functions.table import edit_table
from functions.table import view_table
pedidos = page_config(title="Pedidos")

if streamlit.session_state['login']:
    match pedidos:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar pedido]", divider='green')
        case 'Editar':
            streamlit.subheader(":green[Editar pedidos]", divider='green')
            edit_table(table_name='Pedidos')
        case 'Consultar':
            streamlit.subheader(":green[Consultar pedidos]", divider='green')
            view_table(table_name='Pedidos')