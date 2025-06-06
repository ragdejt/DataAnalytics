import streamlit
from constants.constants import CATEGORIAS
from config.page_config import page_config
from functions.table import view_table
from functions.product import add_product
from functions.table import edit_table
produtos = page_config(title="Produtos")

if streamlit.session_state['login']:
    match produtos:
        case 'Adicionar':
            streamlit.subheader(":green[Adicionar produto]", divider='green')
            
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
                options=CATEGORIAS,
                index=0,
                placeholder="Selecione o tipo de produto",
                accept_new_options=True
            )
            produtct_price = streamlit.number_input(
                label="Preço do produto",
                min_value=0.0,
                step=0.5,
                placeholder="Digite o preço do produto",
            )
            product_height = streamlit.number_input(
                label="Altura do produto",
                min_value=0.0,
                step=0.5,
                placeholder="Digite a altura do produto",
            )
            product_width = streamlit.number_input(
                label="Largura do produto",
                min_value=0.0,
                step=0.5,
                placeholder="Digite a largura do produto",
            )
            product_length = streamlit.number_input(
                label="Comprimento do produto",
                min_value=0.0,
                step=0.5,
                placeholder="Digite o comprimento do produto",
            )
            product_weight = streamlit.number_input(
                label="Peso do produto",
                min_value=0.0,
                step=0.5,
                placeholder="Digite o peso do produto",
            )
            product_active = streamlit.checkbox(
                label="Produto ativo",
                value=True,
            )

            if streamlit.button(
                label="Adicionar produto",
                use_container_width=True,
            ):
                add_product(
                    name=product_name,
                    description=product_description,
                    category=product_category,
                    price=produtct_price,
                    height=product_height,
                    width=product_width,
                    length=product_length,
                    weight=product_weight,
                    active=product_active
                )
                streamlit.success(f"Produto {product_name} adicionado!")
                streamlit.toast(f"Produto {product_name} adicionado!")
        case 'Editar':
            streamlit.subheader(":green[Editar produto]", divider='green')
            edit_table(table_name='Produtos')
        case 'Consultar':
            streamlit.subheader(":green[Consultar produtos]", divider='green')
            streamlit.dataframe(view_table('Produtos'))
