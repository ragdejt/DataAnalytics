from database.database import SessionLocal
from decorators.timer import timer
from constants.constants import OK
from rich import print

@timer
def add_user(
    username:str,
    email:str,
    full_name:str,
    password:str,
    is_active:int
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


