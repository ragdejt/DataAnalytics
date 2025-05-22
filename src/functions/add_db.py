from sql.database.database import SessionLocal
from decorators.timer import timer
from constants.paths import OK
from rich import print
from sql.models.Product import Product

@timer
def add_user(
    username: str,
    email: str,
    full_name: str,
    password: str,
    is_active: int = 1 
):
    """Adiciona um usuario ao banco de dados."""
    from sql.models.User import User
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
    created,
    updated,
    active,
):
    """Adiciona um produto ao banco de dados."""
    try:
        with SessionLocal() as session:
            new_product = Product(
                name=name,
                description=description,
                category=category,
                price=price,
                quantity=quantity,
                height=height,
                width=width,
                length=length,
                weight=weight,
                created=created,
                updated=updated,
                active=active
            )
            session.add(new_product)
            session.commit()
    except Exception:
        session.rollback()
    else:
        print(f"{OK} Produto {name}")

