import streamlit
from config.page_config import page_config

fornecedores = page_config(title="Fornecedores")

if streamlit.session_state['login']:
    match fornecedores:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar fornecedor]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar fornecedores]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar fornecedores]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")