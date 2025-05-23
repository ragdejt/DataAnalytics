import streamlit
from sql.database.database import SessionLocal
import pandas
def view_table(table):
    """
    """
    with SessionLocal() as session:
        query = f'SELECT * FROM {table}'
        df = pandas.read_sql(query, session.bind)
        
        streamlit.dataframe(df)