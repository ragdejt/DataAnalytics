import streamlit
from config.page_config import page_config

expedicoes = page_config(title="Expedições")

if streamlit.session_state['login']:
    match expedicoes:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar expedição]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar expedições]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar expedições]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")