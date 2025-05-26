import pandas
import streamlit
from database.database import engine
from functions.view_table import view_table

def edit_table(
    table_name:str,
):
    """Edita uma tabela do banco de dados."""
    new_data = streamlit.data_editor(
        data=pandas.DataFrame(data=view_table(table_name)),
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
