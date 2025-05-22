import streamlit
from sql.database.database import SessionLocal

def view_table(table):
    """
    """
    with SessionLocal() as session:
        query = session.query(table).all()
        streamlit.table(query)