from database.database import SessionLocal
import pandas
def view_table(table_name):
    """Retorna uma tabela do banco de dados."""
    with SessionLocal() as session:
        query = f'SELECT * FROM {table_name}'
        df = pandas.read_sql(query, session.bind)
        return df