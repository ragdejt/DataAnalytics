# Import necessary modules.
from sql.models.User import User
from sql.database.database import SessionLocal

# Funcion to add a new user to the database.
def add_user(
    username: str,
    email: str,
    full_name: str,
    password: str,
    is_active: int = 1  # Default to active
):
    """Add a new user to the database."""
    try:
        with SessionLocal() as session:
            session.add(User(
                username=username,
                email=email,
                full_name=full_name,
                password=password,
                is_active=is_active
            ))
            session.commit()
    except Exception:
        session.rollback()
