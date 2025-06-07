import pandas
import streamlit
from decorators.timer import timer
from database.database import engine
from database.database import SessionLocal

@timer
def create_table(classe):
    """Cria as tabelas no banco de dados."""
    
    classe.__table__.create(bind=engine, checkfirst=True)

@timer
def view_table(table_name):
    """
    Retorna uma tabela do banco de dados.

    Args:
        table_name (str): Nome da tabela a ser consultada.
    """
    with SessionLocal() as session:
        query = f'SELECT * FROM {table_name}'
        df = pandas.read_sql(query, session.bind)
        return df
    
@timer
def edit_table(
    table_name:str,
):
    """
    Edita uma tabela do banco de dados.

    Args:
        table_name (str): Nome da tabela a ser editada.
    
    """
    data_table = view_table(table_name)

    new_data = streamlit.data_editor(
        data=data_table,
        use_container_width=True,
        num_rows='dynamic',
        hide_index=True,
    )
    if streamlit.button(
        label="Salvar alterações",
        use_container_width=True,
    ):
        new_data.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False
        )
        streamlit.success('Edição feita com sucesso')
        streamlit.toast('Edição feita com sucesso')