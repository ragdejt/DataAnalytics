from database.database import SessionLocal
from decorators.timer import timer
from constants.constants import OK
from rich import print
from models.produto import Produto
from sqlalchemy.exc import PendingRollbackError

@timer
def add_user(
    username: str,
    email: str,
    full_name: str,
    password: str,
    is_active: int = 1 
):
    """Adiciona um usuario ao banco de dados."""
    from models.usuario import Usuario
    try:
        with SessionLocal() as session:
            session.add(Usuario(
                username=username,
                email=email,
                full_name=full_name,
                password=password,
                is_active=is_active
            ))
    except Exception:
        session.rollback()
    else:
        print(f"{OK} Usuário {username}")
        session.commit()

@timer
def add_product(
    name,
    description,
    category,
    price,
    quantity,
    height,
    width,
    length,
    weight,
    active,
):
    """Adiciona um produto ao banco de dados."""
    try:
        with SessionLocal() as session:
            session.add(Produto(
                Nome=name,
                Descricao=description,
                Categoria=category,
                Preco=price,
                Quantidade=quantity,
                Altura=height,
                Largura=width,
                Comprimento=length,
                Peso=weight,
                Ativo=active
            ))
            session.commit()
    except PendingRollbackError:
        session.rollback()
    finally:
        session.close()

