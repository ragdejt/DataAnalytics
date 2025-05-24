from database.database import SessionLocal
from decorators.timer import timer
from constants.paths import OK
from rich import print
from models.Product import Product
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
    from models.User import User
    try:
        with SessionLocal() as session:
            session.add(User(
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
            session.add(Product(
                name=name,
                description=description,
                category=category,
                price=price,
                quantity=quantity,
                height=height,
                width=width,
                length=length,
                weight=weight,
                active=active
            ))
            session.commit()
    except PendingRollbackError:
        session.rollback()
    finally:
        session.close()

