import streamlit
from config.page_config import page_config

agendamentos = page_config(title="Agendamentos")

if streamlit.session_state['login']:
    match agendamentos:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar agendamento]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Editar':
            streamlit.subheader(":green[Editar agendamentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar agendamentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")