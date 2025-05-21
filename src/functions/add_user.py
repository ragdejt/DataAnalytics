# Import necessary modules.
from sql.models.User import User
from sql.database.database import SessionLocal
from decorators.timer import timer
from constants.paths import OK, RUNNING
# Funcion to add a new user to the database.
@timer
def add_user(
    username: str,
    email: str,
    full_name: str,
    password: str,
    is_active: int = 1  # Default to active
):
    """Adiciona um usuario ao banco de dados."""
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
