import streamlit
from database.database import SessionLocal
import pandas
def view_table(table):
    """Exibe uma tabela do banco de dados."""
    with SessionLocal() as session:
        query = f'SELECT * FROM {table}'
        df = pandas.read_sql(query, session.bind)
        
        streamlit.dataframe(df)