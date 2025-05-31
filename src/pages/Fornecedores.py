import streamlit
from config.page_config import page_config

fornecedores = page_config(title="Fornecedores")

if streamlit.session_state['login']:
    match fornecedores:
        case 'Adicionar':
            streamlit.text_input(
                label='Nome',
                placeholder='Digite o nome fantasia do fornecedor'
            )
            streamlit.text_input(
                label='Razão social',
                placeholder='Digite a razão social do fornecedor'
            )
            streamlit.text_input(
                label='Cadastro Nacional de Pessoa Juridica (CNPJ)',
                placeholder='Digite o CNPJ do fornecedor'
            )


        case 'Editar':
            streamlit.subheader(":green[Editar fornecedores]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar fornecedores]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")