from decorators.timer import timer
from database.database import engine

@timer
def create_tables():
    """Cria todas tabelas necessárias no banco de dados."""
    from models.usuario import Usuario
    from models.produto import Produto

    Usuario.__table__.create(bind=engine, checkfirst=True)
    Produto.__table__.create(bind=engine, checkfirst=True)
