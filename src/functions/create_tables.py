from decorators.timer import timer
from database.database import engine

@timer
def create_tables():
    """Cria todas tabelas necessárias no banco de dados."""
    from models.User import User
    from models.Product import Product

    User.__table__.create(bind=engine, checkfirst=True)
    Product.__table__.create(bind=engine, checkfirst=True)
