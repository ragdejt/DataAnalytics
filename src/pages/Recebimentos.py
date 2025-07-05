import streamlit
from config.page_config import page_config

recebimentos = page_config(title="Recebimentos", option_sidebar=['Adicionar', 'Editar', 'Consultar']
)

if streamlit.session_state['login']:
    match recebimentos:
        case 'Adicionar':
            streamlit.text_input(
                label=''
            )
            streamlit.info("Funcionalidade em desenvolvimento.")

        case 'Editar':
            streamlit.subheader(":green[Editar recebimentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar recebimentos]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")