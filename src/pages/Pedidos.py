import streamlit
from config.page_config import page_config

pedidos = page_config(title="Pedidos")

if streamlit.session_state['login']:
    match pedidos:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar pedido]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar pedidos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Remover':
            streamlit.subheader(":green[Excluir pedidos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar pedidos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")