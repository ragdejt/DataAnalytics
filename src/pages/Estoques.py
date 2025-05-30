import streamlit
from config.page_config import page_config

estoques = page_config(title="Estoques")

if streamlit.session_state['login']:
    match estoques:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar estoque]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar estoques]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar estoques]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
