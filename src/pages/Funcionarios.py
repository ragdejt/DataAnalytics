import streamlit
from config.page_config import page_config

funcionarios = page_config(title="Funcionários")

if streamlit.session_state['login']:
    match funcionarios:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar funcionário]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar funcionários]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar funcionários]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")