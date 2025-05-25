import streamlit
from config.page_config import page_config

recebimentos = page_config(title="Recebimentos")

if streamlit.session_state['login']:
    match recebimentos:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar recebimento]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar recebimentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Remover':
            streamlit.subheader(":green[Excluir recebimentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar recebimentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")