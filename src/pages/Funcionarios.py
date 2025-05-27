import streamlit
from config.page_config import page_config
from constants.constants import ESTADO_CIVIL, CARGO
funcionarios = page_config(title="Funcionários")

if streamlit.session_state['login']:
    match funcionarios:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar funcionário]", divider='green')
            streamlit.text_input(
                label='Nome',
                placeholder='Digite o nome do funcionário',
            )
            streamlit.text_input(
                label='Email',
                placeholder='Digite o email do funcionário',
            )
            streamlit.selectbox(
                label='Estado civil',
                options=ESTADO_CIVIL,
                index=0,
                placeholder='Selecione o estado civil do funcionário',
            )
            streamlit.text_input(
                label='CPF',
                placeholder='Digite o CPF do funcionário',
            )
            streamlit.text_input(
                label='RG',
                placeholder='Digite o RG do funcionário',
            )
            streamlit.date_input(
                label='Data de nascimento')
            streamlit.date_input(
                label='Data de admissão')
            streamlit.date_input(
                label='Data de demissão')
            streamlit.text_input(
                label='Endereço',
                placeholder='Digite o endereço do funcionário',
            )
            streamlit.selectbox(
                label='Cargo',
                options=CARGO,
                index=0,
                placeholder='Selecione o cargo do funcionário',
            )
            streamlit.slider(
                label='Salário',
                min_value=0,
                max_value=10000,
                value=5000,
                step=100,
            )
            streamlit.text_input(
                label='Telefone',
                placeholder='Digite o telefone do funcionário',
            )
            streamlit.text_input(
                label='Celular',
                placeholder='Digite o celular do funcionário',
            )
            streamlit.checkbox(
                label='Ativo',
                value=True,
            )
            if streamlit.button(label='Adicionar funcionário', use_container_width=True):
                streamlit.success("Funcionário adicionado com sucesso!")
                streamlit.toast("Funcionário adicionado com sucesso!")
        case 'Editar':
            streamlit.subheader(":green[Editar funcionários]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")
        case 'Consultar':
            streamlit.subheader(":green[Consultar funcionários]", divider='green')
            streamlit.info("Funcionalidade em desenvolvimento.")