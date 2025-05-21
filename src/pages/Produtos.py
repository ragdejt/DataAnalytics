import streamlit
from constants.paths import CATEGORIES
from config.page_config import page_config

produtos = page_config(title="Produtos")

if streamlit.session_state['login']:

    product_name = streamlit.text_input(
        label="Nome do produto",
        placeholder="Digite o nome do produto",
    )
    product_description = streamlit.text_input(
        label="Descrição do produto",
        placeholder="Digite a descrição do produto",
    )
    product_category = streamlit.selectbox(
        label="Tipo do produto",
        options=CATEGORIES,
        index=0,
        placeholder="Selecione o tipo de produto",
    )
    if streamlit.button(
        label="Adicionar produto",
        use_container_width=True,
    ):
        pass