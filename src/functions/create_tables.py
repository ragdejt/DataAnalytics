from decorators.timer import timer
from sql.database.database import engine

@timer
def create_tables():
    """Cria todas tabelas necessárias no banco de dados."""
    from sql.models.User import User
    from sql.models.Product import Product

    User.__table__.create(bind=engine, checkfirst=True)
    Product.__table__.create(bind=engine, checkfirst=True)
