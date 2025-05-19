from rich import print
from decorators.timer import timer
from sql.database.database import Base
from sql.database.database import engine

@timer
def create_tables():
    """Create all tables in the database."""

    print("Starting table creation process.\n")
    Base.metadata.create_all(bind=engine)
    print("\nTable creation process completed successfully!")
